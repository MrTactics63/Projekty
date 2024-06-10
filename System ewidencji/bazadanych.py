import sqlite3

def create_table():
    conn = sqlite3.connect('uczniowie.db')
    conn.commit()
    conn.close()

def fetch_uczniowie():
    conn = sqlite3.connect('uczniowie.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM uczniowie')
    uczniowie = cursor.fetchall()
    conn.close()
    return uczniowie

def insert_uczen(id, imie, nazwisko, klasa, PESEL, imie_nazwisko_matki, numer_matki, imie_nazwisko_ojca, numer_ojca, adres):
    conn = sqlite3.connect('uczniowie.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO uczniowie (id, imie, nazwisko, klasa, PESEL, imie_nazwisko_matki, numer_matki, imie_nazwisko_ojca, numer_ojca, adres) VALUES (?,?,?,?,?,?,?,?,?,?)',
                (id, imie, nazwisko, klasa, PESEL, imie_nazwisko_matki, numer_matki, imie_nazwisko_ojca, numer_ojca, adres))
    conn.commit()
    conn.close()

def delete_uczen(id):
    conn = sqlite3.connect('uczniowie.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM uczniowie WHERE id=?',(id,))
    conn.commit()
    conn.close()
    
def update_uczen(nowe_imie, nowe_nazwisko, nowa_klasa, nowy_PESEL, nowe_imie_nazwisko_matki, nowy_numer_matki, nowe_imie_nazwisko_ojca, nowy_numer_ojca, nowy_adres, id):
    conn = sqlite3.connect('uczniowie.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE uczniowie SET imie = ?, nazwisko = ?, klasa = ?, PESEL = ?,imie_nazwisko_matki = ?, numer_matki = ? , imie_nazwisko_ojca = ?, numer_ojca = ? , adres = ? WHERE id = ?',
                  (nowe_imie, nowe_nazwisko, nowa_klasa, nowy_PESEL, nowe_imie_nazwisko_matki, nowy_numer_matki, nowe_imie_nazwisko_ojca, nowy_numer_ojca, nowy_adres, id))
    conn.commit()
    conn.close()

def id_exists(id):
    conn = sqlite3.connect('uczniowie.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM uczniowie WHERE id = ?', (id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] > 0

create_table()