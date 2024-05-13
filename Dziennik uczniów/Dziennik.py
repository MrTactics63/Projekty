import tkinter as tk
from tkinter import messagebox
import sqlite3

class DziennikUczniow:
    def __init__(self, master):
        self.master = master
        self.master.title("Dziennik Uczniów")

        # Połączenie z bazą danych
        self.conn = sqlite3.connect("uczniowie.db")
        self.c = self.conn.cursor()

        # Interfejs użytkownika
        self.klasa_label = tk.Label(master, text="Wybierz klasę:")
        self.klasa_label.pack()
        self.klasa_var = tk.StringVar()
        self.klasa_menu = tk.OptionMenu(master, self.klasa_var, *self.get_classes(), command=self.update_students_menu)
        self.klasa_menu.pack()

        self.uczniowie_label = tk.Label(master, text="Wybierz ucznia:")
        self.uczniowie_label.pack()
        self.uczniowie_var = tk.StringVar()
        self.uczniowie_menu = tk.OptionMenu(master, self.uczniowie_var, ())
        self.uczniowie_menu.pack()

        self.semestr_label = tk.Label(master, text="Wybierz semestr:")
        self.semestr_label.pack()
        self.semestr_var = tk.StringVar()
        self.semestr_menu = tk.OptionMenu(master, self.semestr_var, "Semestr 1", "Semestr 2")
        self.semestr_menu.pack()

        self.wybierz_button = tk.Button(master, text="Wybierz", command=self.display_grades)
        self.wybierz_button.pack()

    def get_classes(self):
        self.c.execute("SELECT DISTINCT klasa FROM uczniowie")
        return [row[0] for row in self.c.fetchall()]

    def get_students(self, klasa):
        self.c.execute("SELECT imie, nazwisko FROM uczniowie WHERE klasa=?", (klasa,))
        return [f"{row[0]} {row[1]}" for row in self.c.fetchall()]

    def display_grades(self):
        klasa = self.klasa_var.get()
        uczniowie = self.uczniowie_var.get()
        semestr = self.semestr_var.get()

        uczniowie_split = uczniowie.split()
        if len(uczniowie_split) >= 2:
            imie = uczniowie_split[0]
            nazwisko = uczniowie_split[1]
            self.c.execute("SELECT matematyka, matematyka_ocena, polski, polski_ocena, angielski, angielski_ocena FROM uczniowie WHERE imie=? AND nazwisko=? AND semestr=?",
                            (imie, nazwisko, int(semestr[-1])))
            oceny = self.c.fetchone()

            if oceny:
                przedmioty = [oceny[i] for i in range(len(oceny)) if i % 2 == 0 and oceny[i]]
                oceny_przedmiotow = [oceny[i] for i in range(len(oceny)) if i % 2 != 0]
                
                for przedmiot, ocena in zip(przedmioty, oceny_przedmiotow):
                    result_text += {przedmiot},{ocena}
                self.show_grades_window(result_text)
            else:
                messagebox.showinfo("Brak ocen", "Brak ocen dla wybranego ucznia i semestru.")
        else:
            messagebox.showerror("Błąd", "Niepoprawna nazwa ucznia.")

    def update_students_menu(self, *args):
        klasa = self.klasa_var.get()
        self.uczniowie_menu['menu'].delete(0, 'end')
        for student in self.get_students(klasa):
            self.uczniowie_menu['menu'].add_command(label=student, command=tk._setit(self.uczniowie_var, student))

    def show_grades_window(self, grades):
        grades_window = tk.Toplevel(self.master)
        grades_window.title("Oceny ucznia")

        grades_label = tk.Label(grades_window, text=grades)
        grades_label.pack()

root = tk.Tk()
dziennik = DziennikUczniow(root)
root.mainloop()
