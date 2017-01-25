import psycopg2
import datetime
from tkinter import *


# voer de velden in die in de database moeten komen te zitten.
velden = 'Voornaam', 'Achternaam', 'Woonplaats', 'E-mail', 'Wachtwoord', 'Wachtwoord opn.', 'geboortedatum', 'datum', 'Abonnementtype', 'Abonnementduur'

def registreer(velden):
    conn_string = "host='localhost' dbname='Sportschool' user='postgres' password='Burdeos1'"
    # print the connection string we will use to connect
    print ("Connecting to database\n	->%s" % (conn_string))

    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()

    # execute our Query
    cursor.execute("SELECT klant_id FROM klanten")

    # retrieve the records from the database
    records = cursor.fetchall()

    records=list(records)
    orig=[]
    for i in records:
        sessie=list(i)
        item=sessie[0]
        orig.append(item)


    maxn=max(orig)
    nieuw=maxn+1

    for entry in velden:
        #ophalen van het veld
        velden = entry[0]
        #ophalen van de tekst
        text  = entry[1].get()
        # hier wordt het ingevoerde opgehaald en geprint met het veld ervoor.
        # als het het laatste veld is wordt ook ook nog de datum automatisch achtergeplaatst
        Goed = True
        if velden == 'Voornaam':
            naam = text
            print('%s: %s' % (velden, text))
        if velden == 'Achternaam':
            achternaam = text
            print('%s: %s' % (velden, text))
            print(achternaam)
        if velden == 'Woonplaats':
            achternaam = text
            print('%s: %s' % (velden, text))
        if velden == 'E-mail':
            email = text
            print('%s: %s' % (velden, text))
        if velden == 'Wachtwoord':
            wachtwoord = text
            print('%s: %s' % (velden, text))
        if velden == 'Wachtwoord opn.':
            wachtwoord = text
            print('%s: %s' % (velden, text))
        if velden == 'geboortedatum':
            datum = text
            print('%s: %s' % (velden, text))
        if velden == 'Abonnementtype':
            abtype = text
            print('%s: %s' % (velden, text))
        if velden == 'Abonnementduur':
            # tijd in variable
            date= str(datetime.datetime.today().strftime("%d-%m-%Y"))
            print('%s: %s %s' % (velden, text, date))
            abduur = text + " " + date


    cursor.execute("INSERT INTO klanten(klant_id, naam, achternaam, woonplaats, geboortedatum, aanmeldingsdatum, abonnementstype, abonnementsduur, aantal_bezoeken, wachtwoord, email) VALUES ("+str(nieuw)+", '"+naam+"', '"+achternaam+"', '"+woonplaats+"', '"+str(datum)+"', '"+str(date)+"', '"+abtype+"', "+str(abduur)+", "+str(0)+", '"+wachtwoord+"', '"+email+"')")
    conn.commit()

registreer()


# voer de velden in die in de database moeten zitten.
velden = 'Voornaam', 'Achternaam', 'Woonplaats', 'E-mail', 'Wachtwoord', 'Wachtwoord opn.', 'geboortedatum', 'datum', 'Abonnementtype', 'Abonnementduur'


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
   root = Tk()
   Ingevoerde_Tekst = Maak_veld(root, velden)
   root.bind('<Return>', (lambda event, e=Ingevoerde_Tekst: ophalen(e)))

   # knop dat het ophalen activeert  /  haalt ingevoerde tekst op
   Show_Knop = Button(root, text='Show',
          command=(lambda e=Ingevoerde_Tekst: ophalen(e)))

   Show_Knop.pack(side=LEFT, padx=5, pady=5)
   #knop om window te sluiten
   Quit_Knop = Button(root, text='Quit', command=root.quit)
   Quit_Knop.pack(side=LEFT, padx=5, pady=5)

   root.mainloop()
