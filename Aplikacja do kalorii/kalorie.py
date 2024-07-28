import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox

class Kalorie:
    def __init__(self, master):
        self.master = master
        self.master.title('Kalkulator kalorii')
        
        # Set appearance and color theme
        ctk.set_appearance_mode("system")  # Modes: system (default), light, dark
        ctk.set_default_color_theme("blue")
        
        self.create_widgets()
        
    def create_widgets(self):
        # Wprowadzanie danych
        ctk.CTkLabel(self.master, text="Wiek:").pack(pady=(10, 0))
        self.wiek_entry = ctk.CTkEntry(self.master)
        self.wiek_entry.pack(pady=(0, 10))

        ctk.CTkLabel(self.master, text="Wzrost (cm):").pack(pady=(10, 0))
        self.wzrost_entry = ctk.CTkEntry(self.master)
        self.wzrost_entry.pack(pady=(0, 10))

        ctk.CTkLabel(self.master, text="Waga (kg):").pack(pady=(10, 0))
        self.waga_entry = ctk.CTkEntry(self.master)
        self.waga_entry.pack(pady=(0, 10))

        ctk.CTkLabel(self.master, text="Płeć:").pack(pady=(10, 0))
        self.plec_var = tk.StringVar(value="Mężczyzna")
        self.plec_men = ctk.CTkRadioButton(self.master, text="Mężczyzna", variable=self.plec_var, value="Mężczyzna")
        self.plec_women = ctk.CTkRadioButton(self.master, text="Kobieta", variable=self.plec_var, value="Kobieta")
        self.plec_men.pack()
        self.plec_women.pack(pady=(0, 10))

        ctk.CTkLabel(self.master, text="Współczynnik aktywności:").pack(pady=(10, 0))
        self.aktywnosc_entry_var = tk.StringVar(value="1.0")
        self.aktywnosc_entry = ctk.CTkOptionMenu(self.master, variable=self.aktywnosc_entry_var, values=("1.0", "1.2", "1.4", "1.6", "1.8", "2.0"))
        self.aktywnosc_entry.pack(pady=(0, 10))

        # Przycisk do obliczania
        self.oblicz_btn = ctk.CTkButton(self.master, text="Oblicz zapotrzebowanie", command=self.oblicz_kcal)
        self.oblicz_btn.pack(pady=(20, 10))

        # Wyświetlanie wyników
        self.wynik_label_utrzymanie = ctk.CTkLabel(self.master, text="Kalorie na utrzymanie:")
        self.wynik_label_utrzymanie.pack(pady=(10, 0))

        self.wynik_label_schudniecie = ctk.CTkLabel(self.master, text="Kalorie na schudnięcie:")
        self.wynik_label_schudniecie.pack(pady=(10, 0))

        self.wynik_label_przytycie = ctk.CTkLabel(self.master, text="Kalorie na przytycie:")
        self.wynik_label_przytycie.pack(pady=(10, 20))

    def oblicz_kcal(self):
        try:
            wiek = int(self.wiek_entry.get())
            wzrost = int(self.wzrost_entry.get())
            waga = float(self.waga_entry.get())
            plec = self.plec_var.get()
            aktywnosc = float(self.aktywnosc_entry_var.get())

            if plec == 'Mężczyzna':
                bmr = 10 * waga + 6.25 * wzrost - 5 * wiek + 5
            else:
                bmr = 10 * waga + 6.25 * wzrost - 5 * wiek - 161

            # Kalorie dla utrzymania wagi
            kalorie_utrzymanie = bmr * aktywnosc

            # Kalorie na schudnięcie (deficyt 300 kcal)
            kalorie_schudniecie = kalorie_utrzymanie - 300

            # Kalorie na przytycie (nadwyżka 300 kcal)
            kalorie_przytycie = kalorie_utrzymanie + 300

            self.wynik_label_utrzymanie.configure(text=f"Kalorie na utrzymanie: {kalorie_utrzymanie:.0f} kcal")
            self.wynik_label_schudniecie.configure(text=f"Kalorie na schudnięcie: {kalorie_schudniecie:.0f} kcal")
            self.wynik_label_przytycie.configure(text=f"Kalorie na przytycie: {kalorie_przytycie:.0f} kcal")
        except ValueError:
            messagebox.showerror("Błąd", "Proszę wprowadzić poprawne dane")

# Uruchomienie aplikacji
app = ctk.CTk()
app.geometry("400x600")
dziennik = Kalorie(app)
app.mainloop()
