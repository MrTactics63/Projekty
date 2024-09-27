#Po refaktoryzacji kodu

import customtkinter
import sys
from tkinter import messagebox, filedialog
from tkinter import ttk
import bazadanych


if 'bdist_wheel' in sys.argv:
    install_requires = [f'numpy=={pd.__version__}']
    import pandas as pd
class App:
    def __init__(self):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.app = customtkinter.CTk()
        self.app.title('Baza ewidencji studentów')
        self.app.geometry('1750x800')
        self.app.resizable(False, False)

        self.font1 = ('Roboto', 20)
        self.font2 = ('Roboto', 12)

        self.create_treeview()
        self.create_widgets()
        self.app.mainloop()

    def create_treeview(self):
        self.style = ttk.Style(self.app)
        self.style.theme_use('clam')
        self.style.configure('Treeview', font=self.font2, foreground='#141414', background='#9fbec2')

        self.tree = ttk.Treeview(self.app, columns=('ID', 'nazwa_konta', 'waznosc'), show='headings')
        self.tree.column('ID', width=50)
        self.tree.column('nazwa_konta', width=150)
        self.tree.column('waznosc', width=150)
        self.tree.heading('ID', text='ID')
        self.tree.heading('nazwa_konta', text='Login')
        self.tree.heading('waznosc', text='Ważność')
        self.tree.place(x=80, y=250, width=1550, height=400)
        self.tree.bind('<ButtonRelease-1>', self.display_data)

        self.add_to_treeview()

    def create_widgets(self):
        self.nazwa_konta = self.create_label_entry('Login:', 20, 60)
        self.waznosc_entry = self.create_label_entry('Ważność:', 20, 100)
        self.search_entry = self.create_label_entry('Szukaj:', 700, 20)

        self.create_buttons()

    def create_label_entry(self, label_text, x, y):
        label = customtkinter.CTkLabel(self.app, font=self.font1, text=label_text)
        label.place(x=x, y=y)
        entry = customtkinter.CTkEntry(self.app, font=self.font1, width=180)
        entry.place(x=x + 160, y=y)
        return entry

    def create_buttons(self):
        button_configs = [
            ("Filtruj", self.filter_data, 1100, 20),
            ("Dodaj dane studenta", self.insert, 400, 20),
            ("Wyczyść dane", lambda: self.clear(True), 400, 70),
            ("Usuń dane studenta", self.delete, 400, 120),
            ("Zaktualizuj dane studenta", self.update, 400, 170),
            ("Załaduj CSV", self.load_csv, 1450, 20, 260, 60),
            ("Eksportuj do CSV", self.export_csv, 1450, 90, 260, 60)
        ]
        
        for text, command, x, y, *size in button_configs:
            width, height = (180, 40) if not size else size
            button = customtkinter.CTkButton(self.app, font=self.font1, text=text, command=command,
                                               cursor='hand2', corner_radius=15, width=width, height=height)
            button.place(x=x, y=y)

    def add_to_treeview(self, data=None):
        if data is None:
            data = bazadanych.fetch_studenty()
        self.tree.delete(*self.tree.get_children())
        for student in data:
            self.tree.insert('', 'end', values=student)

    def clear(self, *clicked):
        if clicked:
            self.tree.selection_remove(self.tree.focus())
        self.nazwa_konta.delete(0, 'end')
        self.waznosc_entry.delete(0, 'end')

    def display_data(self, event):
        selected_item = self.tree.focus()
        if selected_item:
            row = self.tree.item(selected_item)['values']
            self.clear()
            self.nazwa_konta.insert(0, row[1])
            self.waznosc_entry.insert(0, row[2])

    def delete(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showerror('Błąd', 'Wybierz studenta')
            return

        id = self.tree.item(selected_item)['values'][0]
        bazadanych.delete_student(id)
        self.add_to_treeview()
        self.clear()
        messagebox.showinfo('Sukces', 'Pomyślnie usunięto dane studenta')

    def update(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showerror('Błąd', 'Wybierz studenta')
            return

        id = self.tree.item(selected_item)['values'][0]
        nazwa_konta_value = self.nazwa_konta.get()
        waznosc_value = self.waznosc_entry.get()
        
        bazadanych.update_student(nazwa_konta_value, waznosc_value, id)
        self.add_to_treeview()
        self.clear()
        messagebox.showinfo('Sukces', 'Pomyślnie zaktualizowano dane studenta')

    def insert(self):
        nazwa_konta_value = self.nazwa_konta.get()
        waznosc_value = self.waznosc_entry.get()

        if not (nazwa_konta_value and waznosc_value):
            messagebox.showerror('Błąd', 'Uzupełnij wszystkie pola')
            return

        bazadanych.insert_student(nazwa_konta_value, waznosc_value)
        self.add_to_treeview()
        self.clear()
        messagebox.showinfo("Sukces", "Pomyślnie dodano studenta")

    def load_csv(self):
        filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if filename:
            bazadanych.load_from_csv(filename)
            self.add_to_treeview()
            messagebox.showinfo("Sukces", "Pomyślnie zaimportowano dane z pliku CSV")

    def export_csv(self):
        filename = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if filename:
            studenty = bazadanych.fetch_studenty()
            df = pd.DataFrame(studenty, columns=['ID', 'nazwa_konta', 'waznosc'])
            df.to_csv(filename, index=False)
            messagebox.showinfo("Sukces", "Pomyślnie wyeksportowano dane do pliku CSV")

    def filter_data(self):
        phrase = self.search_entry.get()
        all_data = bazadanych.fetch_studenty()
        filtered_data = [student for student in all_data if phrase.lower() in str(student).lower()]
        self.add_to_treeview(filtered_data)

if __name__ == "__main__":
    App()
