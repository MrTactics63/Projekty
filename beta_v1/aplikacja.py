
import customtkinter
import sys
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import bazadanych

if 'bdist_wheel' in sys.argv:
    # Require the same numpy version used when building
    import pandas as pd
    install_requires = ['numpy=={}'.format(pd.__version__)]

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.title('Baza ewidencji studentów')
app.geometry('1750x800')
app.resizable(False, False)

font1 = ('Roboto', 20)
font2 = ('Roboto', 12)

def add_to_treeview(data=None):
    """ Populate Treeview with student data """
    if data is None:
        data = bazadanych.fetch_studenty()  # Fetch from database
    tree.delete(*tree.get_children())  # Clear previous data
    for student in data:
        tree.insert('', END, values=student)

def clear(*clicked):
    """ Clear input fields """
    if clicked:
        tree.selection_remove(tree.focus())
    nazwa_konta.delete(0, END)
    waznosc_entry.delete(0, END)

def display_data(event):
    """ Display selected student data in entry fields """
    selected_item = tree.focus()
    if selected_item:
        row = tree.item(selected_item)['values']
        clear()
        # row[0] is ID, row[1] is Login, row[2] is Waznosc
        nazwa_konta.insert(0, row[1])  # Login
        waznosc_entry.insert(0, row[2])  # Waznosc

def delete():
    """ Delete selected student """
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showerror('Błąd', 'Wybierz studenta')
    else:
        row = tree.item(selected_item)['values']
        id = row[0]  # Correct ID retrieval
        bazadanych.delete_student(id)
        add_to_treeview()  # Refresh Treeview
        clear()  # Clear input fields
        messagebox.showinfo('Sukces', 'Pomyślnie usunięto dane studenta')

def update():
    """ Update selected student data """
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showerror('Błąd', 'Wybierz studenta')
    else:
        row = tree.item(selected_item)['values']
        id = row[0]  # Correct ID retrieval
        nazwa_konta_value = nazwa_konta.get()
        waznosc_value = waznosc_entry.get()
        
        # Update student in the database
        bazadanych.update_student(nazwa_konta_value, waznosc_value, id)
        add_to_treeview()  # Refresh Treeview
        clear()
        messagebox.showinfo('Sukces', 'Pomyślnie zaktualizowano dane studenta')

def insert():
    """ Insert new student into the database """
    nazwa_konta_value = nazwa_konta.get()
    waznosc_value = waznosc_entry.get()

    if not (nazwa_konta_value and waznosc_value):
        messagebox.showerror('Błąd', 'Uzupełnij wszystkie pola')
    else:
        # Insert new student
        bazadanych.insert_student(nazwa_konta_value, waznosc_value)
        add_to_treeview()  # Refresh Treeview
        clear()
        messagebox.showinfo("Sukces", "Pomyślnie dodano studenta")

def load_csv():
    """ Load student data from CSV """
    filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if filename:
        bazadanych.load_from_csv(filename)
        add_to_treeview()  # Refresh Treeview
        messagebox.showinfo("Sukces", "Pomyślnie zaimportowano dane z pliku CSV")

def export_csv():
    """ Export student data to CSV """
    filename = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if filename:
        studenty = bazadanych.fetch_studenty()
        df = pd.DataFrame(studenty, columns=['ID', 'nazwa_konta', 'waznosc'])
        df.to_csv(filename, index=False)
        messagebox.showinfo("Sukces", "Pomyślnie wyeksportowano dane do pliku CSV")

def filter_data():
    """ Filter student data by search term """
    phrase = search_entry.get()
    all_data = bazadanych.fetch_studenty()
    filtered_data = [student for student in all_data if phrase.lower() in str(student).lower()]
    add_to_treeview(filtered_data)

# UI Elements (Labels, Entries, Buttons)
nazwa_konta_label = customtkinter.CTkLabel(app, font=font1, text='Login:')
nazwa_konta_label.place(x=20, y=60)
nazwa_konta = customtkinter.CTkEntry(app, font=font1, width=180)
nazwa_konta.place(x=180, y=60)

waznosc_label = customtkinter.CTkLabel(app, font=font1, text='Wazność:')
waznosc_label.place(x=20, y=100)
waznosc_entry = customtkinter.CTkEntry(app, font=font1, width=180)
waznosc_entry.place(x=180, y=100)

search_label = customtkinter.CTkLabel(app, font=font1, text='Szukaj:')
search_label.place(x=800, y=20)
search_entry = customtkinter.CTkEntry(app, font=font1, width=180)
search_entry.place(x=900, y=20)

search_button = customtkinter.CTkButton(app, font=font1, text='Filtruj', command=filter_data, cursor='hand2', corner_radius=15, width=180, height=40)
search_button.place(x=1100, y=20)

dodaj_button = customtkinter.CTkButton(app, font=font1, text='Dodaj dane studenta', command=insert, cursor='hand2', corner_radius=15, width=180, height=40)
dodaj_button.place(x=400, y=20)

nowy_button = customtkinter.CTkButton(app, command=lambda: clear(True), font=font1, text='Wyczyść dane', cursor='hand2', corner_radius=15, width=180, height=40)
nowy_button.place(x=400, y=70)

usun_button = customtkinter.CTkButton(app, font=font1, text='Usuń dane studenta', command=delete, cursor='hand2', corner_radius=15, width=180, height=40)
usun_button.place(x=400, y=120)

update_button = customtkinter.CTkButton(app, font=font1, text='Zaktualizuj dane studenta', command=update, cursor='hand2', corner_radius=15, width=180, height=40)
update_button.place(x=400, y=170)

load_csv_button = customtkinter.CTkButton(app, font=font1, text='Załaduj CSV', command=load_csv, cursor='hand2', corner_radius=15, width=260, height=60)
load_csv_button.place(x=1450, y=20)

export_csv_button = customtkinter.CTkButton(app, font=font1, text='Eksportuj do CSV', command=export_csv, cursor='hand2', corner_radius=15, width=260, height=60)
export_csv_button.place(x=1450, y=90)

style = ttk.Style(app)
style.theme_use('clam')
style.configure('Treeview', font=font2, foreground='#141414', background='#9fbec2')

tree = ttk.Treeview(app, columns=('ID', 'nazwa_konta', 'waznosc'), show='headings')
tree.column('ID', width=50)
tree.column('nazwa_konta', width=150)
tree.column('waznosc', width=150)
tree.heading('ID', text='ID')
tree.heading('nazwa_konta', text='Login')
tree.heading('waznosc', text='Wazność')
tree.place(x=80, y=250, width=1550, height=400)
tree.bind('<ButtonRelease-1>', display_data)

add_to_treeview()

app.mainloop()
