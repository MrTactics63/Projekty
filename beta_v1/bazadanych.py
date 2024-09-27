import sqlite3
import csv

def create_table():
    conn = sqlite3.connect('studenty.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS studenty (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nazwa_konta TEXT NOT NULL,
            waznosc TEXT NOT NULL
        )
    ''')
   
    conn.commit()
    conn.close()

def fetch_studenty():
    conn = sqlite3.connect('studenty.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM studenty')
    studenty = cursor.fetchall()
    conn.close()
    return studenty

def insert_student(nazwa_konta, waznosc):
    conn = sqlite3.connect('studenty.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO studenty (nazwa_konta, waznosc) VALUES (?,?)',
                   (str(nazwa_konta), str(waznosc)))
    conn.commit()
    conn.close()

def delete_student(id):
    conn = sqlite3.connect('studenty.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM studenty WHERE id=?', (id,))
    conn.commit()
    conn.close()
    
def update_student(nazwa_konta, waznosc, id):
    conn = sqlite3.connect('studenty.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE studenty SET nazwa_konta=?, waznosc=? WHERE id = ?',
                   (str(nazwa_konta), str(waznosc), int(id)))
    conn.commit()
    conn.close()

def id_exists(id):
    conn = sqlite3.connect('studenty.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM studenty WHERE id = ?', (int(id),))
    result = cursor.fetchone()
    conn.close()
    return result[0] > 0

def load_from_csv(filename):
    conn = sqlite3.connect('studenty.db')
    cursor = conn.cursor()
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute('INSERT INTO studenty (nazwa_konta, waznosc) VALUES (?,?)',
                           (row['nazwa_konta'], row['waznosc']))
    conn.commit()
    conn.close()

# Create the table
create_table()
