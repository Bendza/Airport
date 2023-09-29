from tkinter import *
from tkinter import ttk
import baza


def login_screen():
    global screen
    screen=Tk()

    global username
    global password
    username = StringVar()
    password = StringVar()

    screen.geometry("300x250")
    screen.title("Login forma")
    Label(screen, text="").pack()
    Label(screen, text="Unesite vase login podatke",font= ("Calibri",14)).pack()
    Label(screen, text = "").pack()
    Label(screen, text="Username: ",font= ("Calibri",14)).pack()
    Entry(screen, textvariable=username).pack()
    Label(screen, text="Password :",font= ("Calibri",14)).pack()
    Entry(screen, textvariable=password).pack()
    Label(screen, text = "").pack()
    Button(screen, text = "Log In",font= ("Calibri",14),width = 20,command=loging).pack()
    screen.mainloop()

def loging():
    if baza.login_check(username.get(),password.get()):
        global radnik
        radnik = username.get()
        if baza.radnomesto_check(username.get()) == "Menadzer":
            screen.destroy()
            menadzer_screen()
        else:
            screen.destroy()
            prodavac_screen()
    else:
        Label(screen,text = "Greska!",font=("Calibri",14),foreground="red").pack()

def menadzer_screen():
    screen1 = Tk()
    screen1.geometry("610x310")
    screen1.title("Menadzer")

    global tabControl
    tabControl = ttk.Notebook(screen1)

    tab1_screen()
    tab2_screen()
    tab3_screen()

    tabControl.pack(expan = 1, fill = "both")

    screen1.mainloop()

def tab1_screen():
    tab1 = ttk.Frame(tabControl)
    tabControl.add(tab1, text = "Karte")
    l1 = Label(tab1,text="ID Leta:",font= ("Calibri",14))
    l1.grid(row=0,column=6)
    l2 = Label(tab1, text="Ime:",font= ("Calibri",14))
    l2.grid(row=2, column=6)
    l3 = Label(tab1, text="Prezime:",font= ("Calibri",14))
    l3.grid(row=4, column=6)
    l4 = Label(tab1, text="Prodavac:",font= ("Calibri",14))
    l4.grid(row=6, column=6)
    l5 = Label(tab1, text="Cena:",font= ("Calibri",14))
    l5.grid(row=8, column=6)

    global idleta_text
    global ime_text
    global prezime_text
    global prodavac_text
    global cena_text
    global e1
    global e2
    global e3
    global e4
    global e5
    idleta_text=StringVar()
    e1=Entry(tab1,textvariable=idleta_text)
    e1.grid(row=1,column=6)
    ime_text = StringVar()
    e2 = Entry(tab1, textvariable=ime_text)
    e2.grid(row=3, column=6)
    prezime_text = StringVar()
    e3 = Entry(tab1, textvariable=prezime_text)
    e3.grid(row=5, column=6)
    prodavac_text = StringVar()
    e4 = Entry(tab1, textvariable=prodavac_text)
    e4.grid(row=7, column=6)
    cena_text = StringVar()
    e5 = Entry(tab1, textvariable=cena_text)
    e5.grid(row=9, column=6)

    global list1
    list1=Listbox(tab1, height=15,width=73)
    list1.grid(row=0,column=0,rowspan=10,columnspan=5)

    sb1=Scrollbar(tab1,width=20)
    sb1.grid(row=2,column=5,rowspan=6)

    list1.configure(yscrollcommand=sb1.set)
    list1.bind('<<ListboxSelect>>',get_selected)
    sb1.configure(command=list1.yview)

    b1=Button(tab1,text="Prikazi Sve",width=10,font= ("Calibri",10),command=prikazi_karte)
    b1.grid(row=12,column=0,pady=5,padx=5)
    b5 = Button(tab1, text="Pretrazi", width=10, font=("Calibri", 10),command=search_karte)
    b5.grid(row=12, column=1, pady=5, padx=5)
    b2 = Button(tab1, text="Dodaj",width=10,font= ("Calibri",10),command=dodaj_kartu)
    b2.grid(row=12, column=2,pady=5,padx=5)
    b3 = Button(tab1, text="Izmeni",width=10,font= ("Calibri",10),command=izmeni_kartu)
    b3.grid(row=12, column=3,pady=5,padx=5)
    b4 = Button(tab1, text="Izbrisi",width=10,font= ("Calibri",10),command=izbrisi_kartu)
    b4.grid(row=12, column=4,pady=5,padx=5)

    prikazi_karte()

def tab2_screen():
    tab2 = ttk.Frame(tabControl)
    tabControl.add(tab2, text = "Radnici")

    l1 = Label(tab2, text="Username:", font=("Calibri", 14))
    l1.grid(row=0, column=6)
    l2 = Label(tab2, text="Password:", font=("Calibri", 14))
    l2.grid(row=2, column=6)
    l3 = Label(tab2, text="Radnomesto:", font=("Calibri", 14))
    l3.grid(row=4, column=6)


    global e111
    global e222
    global c1
    global username_text
    global password_text
    global radnomesto_text

    username_text=StringVar()
    e111 = Entry(tab2, textvariable=username_text)
    e111.grid(row=1,column=6)
    password_text=StringVar()
    e222 = Entry(tab2, textvariable=password_text)
    e222.grid(row=3,column=6)
    radnomesto_text=StringVar()
    c1 = ttk.Combobox(tab2,values=["Prodavac","Menadzer",""],width=17,textvariable=radnomesto_text)
    c1.grid(row=5,column=6)

    global list3

    list3 = Listbox(tab2,height=10,width=73)
    list3.grid(row=0,column=0,rowspan=6,columnspan=5)

    sb3=Scrollbar(tab2,width=20)
    sb3.grid(row=1,column=5,rowspan=6)

    list3.configure(yscrollcommand=sb3.set)
    list3.bind('<<ListboxSelect>>',get_selected3)
    sb3.configure(command=list1.yview)

    b1 = Button(tab2, text="Prikazi Sve", width=10, font=("Calibri", 10), command=prikazi_radnike)
    b1.grid(row=7, column=0, pady=5, padx=5)
    b2 = Button(tab2, text="Pretrazi", width=10, font=("Calibri", 10), command=search_radnike)
    b2.grid(row=7, column=1, pady=5, padx=5)
    b3 = Button(tab2, text="Dodaj", width=10, font=("Calibri", 10), command=dodaj_radnika)
    b3.grid(row=7, column=2, pady=5, padx=5)
    b4 = Button(tab2, text="Izmeni", width=10, font=("Calibri", 10), command=izmeni_radnika)
    b4.grid(row=7, column=3, pady=5, padx=5)
    b5 = Button(tab2, text="Izbrisi", width=10, font=("Calibri", 10), command=izbrisi_radnika)
    b5.grid(row=7, column=4, pady=5, padx=5)

    prikazi_radnike()

def tab3_screen():
    global tab3
    tab3 = ttk.Frame(tabControl)
    tabControl.add(tab3, text = "Izvestaji")

    ukupna = 0
    for karta in baza.karte:
        ukupna = ukupna + float(karta.cena)

    l1 = Label(tab3,text="Ukupna vrednost prodatih karata:",font=("Calibri",14))
    l1.grid(row=0,column=0,columnspan=2)

    l2 = Label(tab3,text="",font=("Calibri",14))
    l2.grid(row=0,column=2)
    l2.config(text=ukupna)

    l3 = Label(tab3,text="")
    l3.grid(row=1,column=0)

    l4 = Label(tab3,text="Izaberite Radnika:",font=("Calibri",14),width=20)
    l4.grid(row=2,column=0)
    
    l5 = Label(tab3,text="")
    l5.grid(row=3,column=0)

    radnici = []
    for user in baza.users:
        radnici.append(user.username)

    global combo_text
    combo_text = StringVar()
    c1 = ttk.Combobox(tab3,textvariable=combo_text,values=radnici,width=20)
    c1.grid(row=2,column=1)
    b1 = Button(tab3,text="Potvrdi",command=izvestaj)
    b1.grid(row=2,column=2)

def izvestaj():
    global labela
    suma = 0
    for karta in baza.karte:
        if karta.prodavac == combo_text.get():
            suma = suma + karta.cena

    labela = Label(tab3,text=f"Radnik {combo_text.get()} je prodao karti u vrednosti od: {suma}",font=("Calibri",14),width=50)
    labela.grid(row=4, column=0,columnspan=4)



def prodavac_screen():
    screen2 = Tk()
    screen2.title("Prodavac")
    screen2.geometry("400x300")

    global list2
    list2 = Listbox(screen2,height=15,width=40)
    list2.grid(row=0,column=0,rowspan=11)

    l1 = Label(screen2, text="ID Leta:", font=("Calibri", 14))
    l1.grid(row=0, column=3)
    l2 = Label(screen2, text="Ime:", font=("Calibri", 14))
    l2.grid(row=2, column=3)
    l3 = Label(screen2, text="Prezime:", font=("Calibri", 14))
    l3.grid(row=4, column=3)
    l4 = Label(screen2, text="Cena:", font=("Calibri", 14))
    l4.grid(row=6, column=3)

    global e11
    global e22
    global e33
    global e44
    global idleta_text_prodavac
    global ime_text_prodavac
    global prezime_text_prodavac
    global cena_text_prodavac

    idleta_text_prodavac = StringVar()
    e11 = Entry(screen2, textvariable=idleta_text_prodavac)
    e11.grid(row=1, column=3)
    ime_text_prodavac = StringVar()
    e22 = Entry(screen2, textvariable=ime_text_prodavac)
    e22.grid(row=3, column=3)
    prezime_text_prodavac = StringVar()
    e33 = Entry(screen2, textvariable=prezime_text_prodavac)
    e33.grid(row=5, column=3)
    cena_text_prodavac = StringVar()
    e44 = Entry(screen2, textvariable=cena_text_prodavac)
    e44.grid(row=7, column=3)

    sb1 = Scrollbar(screen2, width=20)
    sb1.grid(row=2, column=2, rowspan=6)

    list2.configure(yscrollcommand=sb1.set)
    list2.bind('<<ListboxSelect>>', get_selected2)
    sb1.configure(command=list2.yview)

    b1 = Button(screen2, text = "Potrvdi",font=("Calibri",14),height=1,width=10,command=dodaj_kartu_prodavac)
    b1.grid(row=8,column=3,pady=5)

    global l11
    l11 = Label(screen2, text="", font=("Calibri", 14), foreground="green")
    l11.grid(rows=9, column=3)
    prikazi_letove()

    screen2.mainloop()


def prikazi_karte():
    list1.delete(0,END)
    for i in baza.karte:
        list1.insert(END,i)

def prikazi_letove():
    for i in baza.letovi:
        list2.insert(END,i)

def prikazi_radnike():
    list3.delete(0,END)
    for i in baza.users:
        list3.insert(END,i)

def search_karte():
    list1.delete(0,END)
    for karta in baza.karte:
        if ((idleta_text.get() == "" or idleta_text.get() == karta.idleta) and (ime_text.get() == "" or ime_text.get() == karta.ime) and (prezime_text.get() == "" or prezime_text.get() == karta.prezime) and (prodavac_text.get() == "" or prodavac_text.get() == karta.prodavac) and (cena_text.get() == str(karta.cena) or cena_text.get() == "")):
            list1.insert(END,karta)

def search_radnike():
    list3.delete(0,END)
    for user in baza.users:
        if ((username_text.get() == "" or username_text.get() == user.username) and (password_text.get() == "" or password_text.get() == user.password) and (radnomesto_text.get() == "" or radnomesto_text.get() == user.radnomesto)):
            list3.insert(END,user)

def dodaj_kartu():
    i = len(baza.karte)+1
    baza.karte.append(baza.karta(i,idleta_text.get(),ime_text.get(),prezime_text.get(),prodavac_text.get(),cena_text.get()))
    baza.insert_karta(idleta_text.get(),ime_text.get(),prezime_text.get(),prodavac_text.get(),cena_text.get())
    prikazi_karte()
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)

def dodaj_radnika():
    a = 0
    for user in baza.users:
        if user.username == username_text.get():
            a = 1
    if a == 0:
        baza.users.append(baza.user(username_text.get(),password_text.get(),radnomesto_text.get()))
        baza.insert_user(username_text.get(),password_text.get(),radnomesto_text.get())
        prikazi_radnike()
        e111.delete(0,END)
        e222.delete(0,END)
        c1.delete(0,END)

def dodaj_kartu_prodavac():
    if (e11.get() != "" and e22.get() != "" and e33.get() != "" and e44.get() != ""):
        i=len(baza.karte)+1
        baza.karte.append(baza.karta(i,idleta_text_prodavac.get(),ime_text_prodavac.get(),prezime_text_prodavac.get(),radnik,cena_text_prodavac.get()))
        baza.insert_karta(idleta_text_prodavac.get(),ime_text_prodavac.get(),prezime_text_prodavac.get(),radnik,cena_text_prodavac.get())
        e11.delete(0,END)
        e22.delete(0,END)
        e33.delete(0,END)
        e44.delete(0,END)
        l11.config(text="Uspesno!",foreground="green")
    else:
        l11.config(text="Neuspesno!",foreground="red")





def get_selected(event):
    global index
    if (len(list1.curselection()) > 0):
        index=list1.curselection()[0]
        karta = baza.karte[index]
        e1.delete(0,END)
        e1.insert(END,karta.idleta)
        e2.delete(0, END)
        e2.insert(END,karta.ime)
        e3.delete(0, END)
        e3.insert(END,karta.prezime)
        e4.delete(0, END)
        e4.insert(END,karta.prodavac)
        e5.delete(0, END)
        e5.insert(END,str(karta.cena))

def get_selected2(event):
    global index2
    if (len(list2.curselection()) > 0):
        index2=list2.curselection()[0]
        i = baza.letovi[index2]
        e11.delete(0,END)
        e11.insert(END,i.id)
        l11.config(text="")

def get_selected3(event):
    global index3
    if (len(list3.curselection()) > 0):
        index3=list3.curselection()[0]
        i = baza.users[index3]
        e111.delete(0,END)
        e111.insert(END,i.username)
        e222.delete(0, END)
        e222.insert(END, i.password)
        if baza.users[index3].radnomesto == "Prodavac":
            c1.current(0)
        else:
            c1.current(1)

def izmeni_kartu():
    trid = baza.karte[index].id
    baza.karte.remove(baza.karte[index])
    baza.karte.insert(index,baza.karta(trid,idleta_text.get(),ime_text.get(),prezime_text.get(),prodavac_text.get(),cena_text.get()))
    baza.update_karta(trid,idleta_text.get(),ime_text.get(),prezime_text.get(),prodavac_text.get(),cena_text.get())
    prikazi_karte()

def izmeni_radnika():
    stari_username = baza.users[index3].username
    baza.users.remove(baza.users[index3])
    baza.users.insert(index3,baza.user(username_text.get(),password_text.get(),radnomesto_text.get()))
    baza.update_user(username_text.get(),password_text.get(),radnomesto_text.get(),stari_username)
    prikazi_radnike()

def izbrisi_kartu():
    for karta in baza.karte:
        if (karta.id == baza.karte[index].id):
            baza.karte.remove(karta)
            baza.delete_karta(karta.id)
    prikazi_karte()
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)

def izbrisi_radnika():
    for user in baza.users:
        if (user.username == baza.users[index3].username):
            baza.users.remove(user)
            baza.delete_user(user.username)
        prikazi_radnike()
        e111.delete(0,END)
        e222.delete(0,END)
        c1.delete(0,END)


login_screen()