from tkinter import *
import datetime
from tkinter.messagebox import showinfo
#from gpiozero import *
#from time import sleep

velden = 'Klant-ID', 'Wachtwoord'
sec = 0
counter = 0
#green_led = LED()
#red_led = LED()


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
# openen GUI
root = Tk()
def toonVenster(velden):
    #ingevoerde tekst wordt hier opgehaald in een lijst gezet en dan in variabelen gezet
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
    Combinatie_Login_Gegevens = Klant_id + ' ' + Wachtwoord

    ################# Er moet gekeken worden of het klant-ID en wachtwoord van de GUI overeenkomt met het klant ID en wachtwoord dat in de database staat.##############

    #Data = ID_Database + ' ' + DataBaseWachtwoord
    #if Data == Combinatie_Login_Gegevens:
    #   Je wordt ingelogd
    # green_led.on()
    # sleep(5)
    # green_led.off()

    #if Data != Combinatie_Login_Gegevens
        #ErrorBericht = 'Het ingevoerde klant-ID of wachtwoord komt niet overeen met het klant-ID.'
        #showinfo(title='popup', message=ErrorBericht)
        #red_led.on()
        #sleep(5)
        #red_led.off()
        #subwindow.withdraw()

    #dan moet dit achter de eerste if statement
    def close():
        subwindow.withdraw()

    subwindow = Toplevel(master=root)

    # hier komt de code voor het tweede scherm


        # nu de Verbrande_Calorieën in de database zetten en tonen als nodig.

# Hier wordt er berekend hoeveel Calorieën er zijn verbrandt
    def Calorieën():
        global counter
        global Verbrande_Calorieën
        calorieën_per_Uur = 700
        Calorieën_Per_Sec = calorieën_per_Uur/3600
        Verbrande_Calorieën = sec*Calorieën_Per_Sec
# Hier staat wat er gebeurd als je op de bereken knop drukt
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
# hier staat de functie voor de timer en wat er in moet staan
    def tick():
        global sec
        sec += 1
        time['text'] = 'Je bent nu {} seconden aan het trainen.'.format(sec)
        # per seconden weer de functie tick uitvoeren
        time.after(1000, tick)
        return sec
# dit is de functie voor het uitloggen en wat er dan gebeurd
    def uitloggen():
        bericht = 'Je hebt in totaal {:.2f} calorieen verbrand'.format(Verbrande_Calorieën)
        showinfo(title='popup', message=bericht)
        subwindow.withdraw()

    #label voor de timer
    time = Label(master=subwindow,text=sec)
    time.pack()
    # knop om de timer te starten
    Button(master=subwindow, text='Start met oefenen', command=tick).pack()
    # knop voor het uitloggen
    Uitlog_Button = Button(master=subwindow, text='Uitloggen', command=uitloggen)
    Uitlog_Button.pack(padx=10, pady=10)
    # bereken knop
    Bereken_Cal_Knop = Button(master=subwindow, text='Bereken het aantal verbrande calorieen', command=Calorieën)
    Bereken_Cal_Knop.pack(padx=10, pady=10)

Ingevoerde_Tekst = Maak_veld(root, velden)
root.bind('<Return>', (lambda event, e=Ingevoerde_Tekst: toonVenster(e)))

# knop die het inloggen start
Inlog_Knop = Button(root, text='Inloggen',
    command=(lambda e=Ingevoerde_Tekst: toonVenster(e)))
Inlog_Knop.pack(side=LEFT, padx=5, pady=5)

#knop om window te sluiten
Quit_Knop = Button(root, text='Quit', command=root.quit)
Quit_Knop.pack(side=LEFT, padx=5, pady=5)
# einde GUI
root.mainloop()
