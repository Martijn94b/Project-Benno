import psycopg2
import datetime
from tkinter import *
from tkinter.messagebox import showinfo

root = Tk()
# voer de velden in die in de database moeten komen te zitten.
velden = 'Voornaam', 'Achternaam', 'Woonplaats', 'E-mail', 'Wachtwoord', 'Wachtwoord opn.', 'geboortedatum', 'datum', 'Abonnementtype', 'Abonnementduur'

def registreer(velden):

    TextLijst = []
    lijst2 = []

    for entry in velden:
        #ophalen van het veld
        velden = entry[0]
        #ophalen van de tekst
        text  = entry[1].get()
        TextLijst.append(text)
        lijst2.append(velden)

    date= str(datetime.datetime.today().strftime("%d-%m-%Y"))

    naam = TextLijst[0]
    achternaam = TextLijst[1]
    Woonplaats = TextLijst[2]
    email = TextLijst[3]
    wachtwoord = TextLijst[4]
    wachtwoord2 = TextLijst[5]
    datum = TextLijst[6]
    abtype = TextLijst[7]
    abduur0 = TextLijst[8]
    abduur  = abduur0 + " " + date

    if wachtwoord != wachtwoord2:
        bericht = 'De wachtwoorden moeten overeen komen!'
        showinfo(title='Error', message=bericht)
    else:
        bericht = 'De registratie is voltooid!'
        showinfo(title='popup', message=bericht)
        root.withdraw()
        return naam,achternaam,Woonplaats,email,wachtwoord,wachtwoord2,datum,abtype,abduur

# maak de velden aan die worden in gevoerd in variable 'velden'

def Maak_veld(root, velden):
    entries = []
    for veld in velden:
        datum = date=datetime.datetime.today().strftime("%Y-%m-%d")
        rij = Frame(root)
        Tekst = Label(rij, width=15, text=veld, anchor='w')
        #De ingevoerde tekst in de GUI
        ingevoerd = Entry(rij)
        rij.pack(side=TOP, fill=X, padx=5, pady=5)
        Tekst.pack(side=LEFT)
        ingevoerd.pack(side=RIGHT, expand=YES, fill=X)
        # hier nog even naar kijken //  kijken hoe datum erin kan worden verwerkt.
        if entries == 'Abonnementduur':
            entries.append((veld, ingevoerd, datum))
        else:
            entries.append((veld, ingevoerd))
    return entries

if __name__ == '__main__':


    Ingevoerde_Tekst = Maak_veld(root, velden)
    root.bind('<Return>', (lambda event, e=Ingevoerde_Tekst: registreer(e)))

    # knop dat het ophalen activeert  /  haalt ingevoerde tekst op

    Show_Knop = Button(root, text='Register',
          command=(lambda e=Ingevoerde_Tekst: registreer(e)))
    Show_Knop.pack(side=LEFT, padx=5, pady=5)


    #knop om window te sluiten
    Quit_Knop = Button(root, text='Quit', command=root.quit)
    Quit_Knop.pack(side=LEFT, padx=5, pady=5)

    root.mainloop()

