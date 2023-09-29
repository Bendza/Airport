import sqlite3
from klase import *

letovi = []
users = []
karte = []

def connect():
    conn = sqlite3.connect("baza.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS letovi (id INTEGER PRIMARY KEY, mestop text, mestos text, cena float)")
    cur.execute("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password text, radnomesto text)")
    cur.execute("CREATE TABLE IF NOT EXISTS karte (id INTEGER PRIMARY KEY,idleta text, ime text, prezime text, prodavac text, cena float)")
    conn.commit()

    cur.execute("SELECT * FROM karte")
    rows = cur.fetchall()
    for tuple in rows:
        karte.append(karta(tuple[0],tuple[1],tuple[2],tuple[3],tuple[4],tuple[5]))

    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    for tuple in rows:
        users.append(user(tuple[0],tuple[1],tuple[2]))

    cur.execute("SELECT * FROM letovi")
    rows = cur.fetchall()
    for tuple in rows:
        letovi.append(let(tuple[0],tuple[1],tuple[2],tuple[3]))

    conn.close()


def insert_karta(idleta,ime,prezime,prodavac,cena):
    conn = sqlite3.connect("baza.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO karte(idleta,ime,prezime,prodavac,cena) VALUES (?,?,?,?,?)", (idleta,ime,prezime,prodavac,cena))
    conn.commit()
    conn.close()


def insert_user(username,password,radnomesto):
    conn = sqlite3.connect("baza.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO users VALUES (?,?,?)", (username, password, radnomesto))
    conn.commit()
    conn.close()

def insert_let(mestop,mestos,cena):
    conn = sqlite3.connect("baza.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO letovi(mestop,mestos,cena) VALUES (?,?,?)",(mestop, mestos, cena))
    conn.commit()
    conn.close()

def update_karta(id,idleta,ime,prezime,prodavac,cena):
    conn = sqlite3.connect("baza.db")
    cur = conn.cursor()
    cur.execute("UPDATE karte SET idleta=?, ime=?, prezime=?, prodavac=?, cena=? WHERE id=?",(idleta,ime,prezime,prodavac,float(cena),int(id)))
    conn.commit()
    conn.close()

def update_user(username,password,radnomesto,stari_username):
    conn = sqlite3.connect("baza.db")
    cur = conn.cursor()
    cur.execute("UPDATE users SET username=?, password=?, radnomesto=? WHERE username=?",(username,password,radnomesto,stari_username))
    conn.commit()
    conn.close()

def delete_karta(id):
    conn = sqlite3.connect("baza.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM karte WHERE id=?",(id,))
    conn.commit()
    conn.close()

def delete_user(username):
    conn = sqlite3.connect("baza.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE username=?",(username,))
    conn.commit()
    conn.close()

def login_check(username,password):
    conn = sqlite3.connect("baza.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username=?",(username,))
    conn.commit()
    rows = cur.fetchall()
    conn.close()
    try:
        if rows[0][1] == password:
            return True
        else:
            return False
    except:
        return False

def radnomesto_check(username):
    conn = sqlite3.connect("baza.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username=?",(username,))
    conn.commit()
    rows = cur.fetchall()
    return rows[0][2]


#insert_user("Belmin","123","Menadzer")
#insert_user("Belmin1","123","Prodavac")
# insert_let("Beograd","Nis",20)
# insert_let("London","Nis",100)
# insert_let("Beograd","Tokyo",200)
# insert_let("Beograd","Skoplje",30)
# insert_let("NewYork","Beograd",250)
# insert_let("Beograd","Pristina",20)
# insert_let("London","NewYork",150)
# insert_let("Beograd","Lisabon",100)
# insert_let("Sarajevo","Berlin",50)
# insert_let("Bec","Nis",50)
# insert_let("Beograd","Milano",50)
# insert_let("Beograd","Madrid",20)
# insert_let("Sarajevo","Berlin",50)
# insert_let("Bec","Nis",50)
# insert_let("Beograd","Milano",50)
# insert_let("Beograd","Madrid",20)
# insert_let("London","NewYork",150)
# insert_let("Beograd","Lisabon",100)
# insert_let("Sarajevo","Berlin",50)
# insert_let("Bec","Nis",50)
# insert_karta("2","Belmin","Kurtanovic","Belmin1",50)


connect()