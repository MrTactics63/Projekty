import customtkinter
from tkinter import *
from tkinter import ttk 
import tkinter as tk 
from tkinter import messagebox
import bazadanych 

customtkinter.set_appearance_mode("dark")  # Ustawienia trybu ciemnego, jeśli potrzebne
customtkinter.set_default_color_theme("dark-blue")  # Ustawienia motywu kolorystycznego

app = customtkinter.CTk()
app.title('Baza ewidencji uczniów')
app.geometry('1750x600')
app.resizable(False, False)

font1 = ('Roboto', 20)
font2 = ('Roboto', 12)

def dodaj_to_treeview():
    uczniowie = bazadanych.fetch_uczniowie()
    tree.delete(*tree.get_children())
    for uczen in uczniowie:
        tree.insert('', END, values=uczen)

def clear(*clicked):
    if clicked:
        tree.selection_remove(tree.focus())
    id_entry.delete(0, END)
    imie_entry.delete(0, END)
    nazwisko_entry.delete(0, END)
    klasa_entry.delete(0, END)
    PESEL_entry.delete(0, END)
    imie_nazwisko_matki_entry.delete(0, END)
    numer_matki_entry.delete(0, END)
    imie_nazwisko_ojca_entry.delete(0, END)
    numer_ojca_entry.delete(0, END)
    adres_entry.delete(0, END)

def display_data(event):
    selected_item = tree.focus()
    if selected_item:
        row = tree.item(selected_item)['values']
        clear()
        id_entry.insert(0, row[0])
        imie_entry.insert(0, row[1])
        nazwisko_entry.insert(0, row[2])
        klasa_entry.insert(0, row[3])
        PESEL_entry.insert(0, row[4])
        imie_nazwisko_matki_entry.insert(0, row[5])
        numer_matki_entry.insert(0, row[6])
        imie_nazwisko_ojca_entry.insert(0, row[7])
        numer_ojca_entry.insert(0, row[8])
        adres_entry.insert(0, row[9])
    else:
        pass

def delete():
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showerror('Błąd', 'Wybierz ucznia')
    else:
        id = id_entry.get()
        bazadanych.delete_uczen(id)
        dodaj_to_treeview()
        clear()
        messagebox.showinfo('Pomyślnie usunięto dane ucznia')

def update():
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showerror('Błąd', 'Wybierz ucznia')
    else:
        id = id_entry.get()
        imie = imie_entry.get()
        nazwisko = nazwisko_entry.get()
        klasa = klasa_entry.get()
        PESEL = PESEL_entry.get()
        imie_nazwisko_matki = imie_nazwisko_matki_entry.get()
        numer_matki = numer_matki_entry.get()
        imie_nazwisko_ojca = imie_nazwisko_ojca_entry.get()
        numer_ojca = numer_ojca_entry.get()
        adres = adres_entry.get()
        print("Zaktualizowane dane ucznia:")
        print(f"ID: {id}, Imię: {imie}, Nazwisko: {nazwisko}, Klasa: {klasa}, PESEL: {PESEL}, Imię i nazwisko matki: {imie_nazwisko_matki}, Numer matki: {numer_matki}, Imię i nazwisko ojca: {imie_nazwisko_ojca}, Numer ojca: {numer_ojca}, Adres: {adres}")
        bazadanych.update_uczen(imie, nazwisko, klasa, PESEL, imie_nazwisko_matki, numer_matki, imie_nazwisko_ojca, numer_ojca, adres,id)
        dodaj_to_treeview()
        clear()
        messagebox.showinfo('Pomyślnie zaktualizowano dane ucznia')

def insert():
    id = id_entry.get()
    imie = imie_entry.get()
    nazwisko = nazwisko_entry.get()
    klasa = klasa_entry.get()
    PESEL = PESEL_entry.get()
    imie_nazwisko_matki = imie_nazwisko_matki_entry.get()
    numer_matki = numer_matki_entry.get()
    imie_nazwisko_ojca = imie_nazwisko_ojca_entry.get()
    numer_ojca = numer_ojca_entry.get()
    adres = adres_entry.get()
    if not (id and imie and nazwisko and klasa and PESEL and imie_nazwisko_matki and numer_matki and imie_nazwisko_ojca and numer_ojca and adres):
        messagebox.showerror('Błąd', 'Uzupełnij wszystkie pola')
    elif bazadanych.id_exists(id):
        messagebox.showerror('Błąd', 'Takie ID już istnieje w bazie danych')
    else:
        bazadanych.insert_uczen(id, imie, nazwisko, klasa, PESEL, imie_nazwisko_matki, numer_matki, imie_nazwisko_ojca, numer_ojca, adres)
        dodaj_to_treeview()
        messagebox.showinfo("Pomyślnie dodano ucznia")

id_label = customtkinter.CTkLabel(app, font=font1, text='ID:')
id_label.place(x=20, y=20)
id_entry = customtkinter.CTkEntry(app, font=font1, width=180)
id_entry.place(x=240, y=20)

imie_label = customtkinter.CTkLabel(app, font=font1, text='Imię:')
imie_label.place(x=20, y=60)
imie_entry = customtkinter.CTkEntry(app, font=font1, width=180)
imie_entry.place(x=240, y=60)

nazwisko_label = customtkinter.CTkLabel(app, font=font1, text='Nazwisko:')
nazwisko_label.place(x=20, y=100)
nazwisko_entry = customtkinter.CTkEntry(app, font=font1, width=180)
nazwisko_entry.place(x=240, y=100)

klasa_label = customtkinter.CTkLabel(app, font=font1, text='Klasa:')
klasa_label.place(x=20, y=140)
klasa_entry = customtkinter.CTkEntry(app, font=font1, width=180)
klasa_entry.place(x=240, y=140)

PESEL_label = customtkinter.CTkLabel(app, font=font1, text='PESEL:')
PESEL_label.place(x=20, y=180)
PESEL_entry = customtkinter.CTkEntry(app, font=font1, width=180)
PESEL_entry.place(x=240, y=180)

imie_nazwisko_matki_label = customtkinter.CTkLabel(app, font=font1, text='Imię i nazwisko matki:')
imie_nazwisko_matki_label.place(x=20, y=220)
imie_nazwisko_matki_entry = customtkinter.CTkEntry(app, font=font1, width=180)
imie_nazwisko_matki_entry.place(x=240, y=220)

numer_matki_label = customtkinter.CTkLabel(app, font=font1, text='Numer matki:')
numer_matki_label.place(x=20, y=260)
numer_matki_entry = customtkinter.CTkEntry(app, font=font1, width=180)
numer_matki_entry.place(x=240, y=260)

imie_nazwisko_ojca_label = customtkinter.CTkLabel(app, font=font1, text='Imię i nazwisko ojca:')
imie_nazwisko_ojca_label.place(x=20, y=300)
imie_nazwisko_ojca_entry = customtkinter.CTkEntry(app, font=font1, width=180)
imie_nazwisko_ojca_entry.place(x=240, y=300)

numer_ojca_label = customtkinter.CTkLabel(app, font=font1, text='Numer ojca:')
numer_ojca_label.place(x=20, y=340)
numer_ojca_entry = customtkinter.CTkEntry(app, font=font1, width=180)
numer_ojca_entry.place(x=240, y=340)

adres_label = customtkinter.CTkLabel(app, font=font1, text='Adres:')
adres_label.place(x=20, y=380)
adres_entry = customtkinter.CTkEntry(app, font=font1, width=180)
adres_entry.place(x=240, y=380)

dodaj_button = customtkinter.CTkButton(app, font=font1, text='Dodaj dane ucznia', command=insert, cursor='hand2', corner_radius=15, width=260, height=60)
dodaj_button.place(x=250, y=500)

nowy_button = customtkinter.CTkButton(app, command=lambda: clear(True), font=font1, text='Wyczyść dane', cursor='hand2', corner_radius=15, width=260, height=60)
nowy_button.place(x=550, y=500)

usun_button = customtkinter.CTkButton(app, font=font1, text='Usuń dane ucznia', command=delete, cursor='hand2', corner_radius=15, width=260, height=60)
usun_button.place(x=850, y=500)

update_button = customtkinter.CTkButton(app, font=font1, text='Zaktualizuj dane ucznia', command=update, cursor='hand2', corner_radius=15, width=260, height=60)
update_button.place(x=1150, y=500)

style = ttk.Style(app)
style.theme_use('clam')
style.configure('Treeview', font=font2, foreground='#fff', background='#000', fieldbackground='#313837')
style.map('Treeview', background=[('selected', '#1A8F2D')])

tree = ttk.Treeview(app, height=15)
tree['columns'] = ('id', 'imie', 'nazwisko', 'klasa', 'PESEL', 'imie_nazwisko_matki', 'numer_matki', 'imie_nazwisko_ojca', 'numer_ojca', 'adres')
tree.column('#0', width=0, stretch=tk.NO)
tree.column('id', anchor=tk.CENTER, width=30)
tree.column('imie', anchor=tk.CENTER, width=120)
tree.column('nazwisko', anchor=tk.CENTER, width=120)
tree.column('klasa', anchor=tk.CENTER, width=60)
tree.column('PESEL', anchor=tk.CENTER, width=120)
tree.column('imie_nazwisko_matki', anchor=tk.CENTER, width=200)
tree.column('numer_matki', anchor=tk.CENTER, width=120)
tree.column('imie_nazwisko_ojca', anchor=tk.CENTER, width=200)
tree.column('numer_ojca', anchor=tk.CENTER, width=120)
tree.column('adres', anchor=tk.CENTER, width=200)

tree.heading('id', text="ID:")
tree.heading('imie', text='Imię:')
tree.heading('nazwisko', text='Nazwisko:')
tree.heading('klasa', text='Klasa:')
tree.heading('PESEL', text='PESEL:')
tree.heading('imie_nazwisko_matki', text='Imię i nazwisko matki:')
tree.heading('numer_matki', text='Numer matki:')
tree.heading('imie_nazwisko_ojca', text='Imię i nazwisko ojca:')
tree.heading('numer_ojca', text='Numer ojca:')
tree.heading('adres', text='Adres:')

tree.place(x=450, y=60)
tree.bind('<ButtonRelease-1>', display_data)

dodaj_to_treeview()
app.mainloop()
