from tkinter import *
import datetime
from tkinter.messagebox import showinfo

velden = 'Klant-ID', 'Wachtwoord'
sec = 0
counter = 0


def registreer(velden):
    lijst = []
    global Klant_id, Wachtwoord
    for entry in velden:
        #ophalen van het veld

        veld = entry[0]
        #ophalen van de tekst
        text  = entry[1].get()

        lijst.append(text)
    global Klant_id, Wachtwoord

    Klant_id = lijst[0]
    Wachtwoord = lijst[1]
    print(Klant_id)
    print(Wachtwoord)
    Combinatie_Login_Gegevens = Klant_id + ' ' + Wachtwoord
                    # Er moet gekeken worden of het klant-ID overeenkomt met het wachtwoord dat er aan gegeven is.
    #Data = ID_Database + ' ' + DataBaseWachtwoord
    #if Data == Combinatie_Login_Gegevens:
    #   Je wordt ingelogd

    #if Data != Combinatie_Login_Gegevens
        #ErrorBericht = 'Het ingevoerde klant-ID of wachtwoord komt niet overeen met het klant-ID.'
        #showinfo(title='popup', message=ErrorBericht)

    return Klant_id,Wachtwoord



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
###############################
root = Tk()

def toonVenster(velden):
    lijst = []
    global Klant_id, Wachtwoord
    for entry in velden:
        #ophalen van het veld

        veld = entry[0]
        #ophalen van de tekst
        text  = entry[1].get()

        lijst.append(text)
    global Klant_id, Wachtwoord

    Klant_id = lijst[0]
    Wachtwoord = lijst[1]
    print(Klant_id)
    print(Wachtwoord)
    Combinatie_Login_Gegevens = Klant_id + ' ' + Wachtwoord
    ################# Er moet gekeken worden of het klant-ID en wachtwoord van de GUI overeenkomt met het klant ID en wachtwoord dat in de database staat.##############
    #Data = ID_Database + ' ' + DataBaseWachtwoord
    #if Data == Combinatie_Login_Gegevens:
    #   Je wordt ingelogd


    #if Data != Combinatie_Login_Gegevens
        #ErrorBericht = 'Het ingevoerde klant-ID of wachtwoord komt niet overeen met het klant-ID.'
        #showinfo(title='popup', message=ErrorBericht)
        #subwindow.withdraw()











    #dan moet dit achter de eerste if statement
    def close():
        subwindow.withdraw()

    subwindow = Toplevel(master=root)

    # hier komt de code voor het tweede scherm


        # nu de Verbrande_Calorieën in de database zetten en tonen als nodig.

# de timer functie en de uitlog + start knop
    def Calorieën():
        global counter
        global Verbrande_Calorieën
        calorieën_per_Uur = 570
        Calorieën_Per_Sec = calorieën_per_Uur/3600
        Verbrande_Calorieën = sec*Calorieën_Per_Sec


        if counter == 0:
            label2 = Label(master=subwindow,text='Verbrande Calorieen:',height=2)
            label2.pack()
            label = Label(master=subwindow,text='Je hebt {} seconden getraind, in deze tijd heb je {:.2f} calorieen verbrand.'.format(sec,Verbrande_Calorieën),height=2)
            label.pack()
            counter+=1
            return counter, Verbrande_Calorieën
        elif counter > 0:
            label = Label(master=subwindow,text='Je hebt {} seconden getraind, in deze tijd heb je {:.2f} calorieen verbrand.'.format(sec,Verbrande_Calorieën),height=2)
            label.pack()
            counter+=1
            return counter, Verbrande_Calorieën

    def tick():
        global sec
        sec += 1
        time['text'] = 'Je bent nu {} seconden aan het trainen.'.format(sec)
        # per seconden weer de functie tick uitvoeren
        time.after(1000, tick)
        return sec

    def uitloggen():

        bericht = 'Je hebt in totaal {:.2f} calorieen verbrand'.format(Verbrande_Calorieën)
        showinfo(title='popup', message=bericht)
        subwindow.withdraw()

    time = Label(master=subwindow,
                      text=sec)
    time.pack()

    Button(master=subwindow, text='Start met oefenen', command=tick).pack()
    button2 = Button(master=subwindow, text='Uitloggen', command=uitloggen)
    button2.pack(padx=10, pady=10)

    button3 = Button(master=subwindow, text='Bereken het aantal verbrande calorieen', command=Calorieën)
    button3.pack(padx=10, pady=10)




Ingevoerde_Tekst = Maak_veld(root, velden)
root.bind('<Return>', (lambda event, e=Ingevoerde_Tekst: toonVenster(e)))

# knop dat het ophalen activeert  /  haalt ingevoerde tekst op
Show_Knop = Button(root, text='Inloggen',
    command=(lambda e=Ingevoerde_Tekst: toonVenster(e)))

Show_Knop.pack(side=LEFT, padx=5, pady=5)
#knop om window te sluiten
Quit_Knop = Button(root, text='Quit', command=root.quit)
Quit_Knop.pack(side=LEFT, padx=5, pady=5)





root.mainloop()
