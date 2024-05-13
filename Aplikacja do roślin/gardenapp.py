import tkinter as tk
from tkinter import messagebox
import sqlite3

class GardenApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Moja ogrodowa aplikacja")
        
        # Połączenie z bazą danych
        self.conn = sqlite3.connect('garden_plants.db')
        self.c = self.conn.cursor()
        
        # Interfejs użytkownika
        self.label = tk.Label(master, text="Wybierz typ rośliny:")
        self.label.pack()

        self.radio_var = tk.StringVar()
        self.radio_var.set("Jednoroczne")

        self.radio1 = tk.Radiobutton(master, text="Jednoroczne", variable=self.radio_var, value="Jednoroczna")
        self.radio1.pack()

        self.radio2 = tk.Radiobutton(master, text="Wieloletnie", variable=self.radio_var, value="Wieloletnia")
        self.radio2.pack()

        self.submit_button = tk.Button(master, text="Pokaż rośliny", command=self.show_plants)
        self.submit_button.pack()

    def show_plants(self):
        plant_type = self.radio_var.get()
        
        try:
            self.c.execute("SELECT * FROM plants WHERE type=?", (plant_type,))
            plants = self.c.fetchall()

            if plants:
                plant_list = "\n".join([f"{plant[1]} - Okres wysiewu: {plant[3]}\nUwagi: {plant[4]}" for plant in plants])
                messagebox.showinfo("Lista roślin", plant_list)
            else:
                messagebox.showinfo("Lista roślin", "Brak roślin w bazie danych.")
        except sqlite3.Error as e:
            messagebox.showerror("Błąd", f"Błąd wykonania zapytania SQL: {e}")

    def __del__(self):
        self.conn.close()

# Uruchomienie aplikacji
root = tk.Tk()
app = GardenApp(root)
root.mainloop()