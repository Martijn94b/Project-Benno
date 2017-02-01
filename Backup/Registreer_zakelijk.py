import psycopg2
import datetime
from time import strftime
import sys

def registreer_zakelijk():

    conn_string = "host='localhost' dbname='Sportschool' user='postgres' password='Burdeos1'"
    # print the connection string we will use to connect
    print ("Connecting to database\n	->%s" % (conn_string))

    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()

    auth=input("Vul de medewerkerauthenticatiecode in: ")
    if auth != "06070":
        sys.exit("Uw heeft een verkeerde code ingevuld; het proces wordt afgebroken.")

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
    try:
        maxn=max(orig)
        nieuw=maxn+1
    except:
        ValueError()
        nieuw=1

    naam=input("Wat is uw naam: ")
    achternaam=input("Wat is uw achternaam: ")
    woonplaats=input("Wat is uw woonplaats: ")
    email=input("Wat is uw emailadres: ")
    wachtwoord=input("Voer een wachtwoord in: ")
    wachtwoord2=input("Voer uw wachtwoord opnieuw in: ")
    while wachtwoord!=wachtwoord2:
        print("De wachtwoorden zijn niet hetzelfde; probeer het opnieuw.")
        wachtwoord=input("Voer een wachtwoord in: ")
        wachtwoord2=input("Voer uw wachtwoord opnieuw in: ")
    while '@' not in email:
        print("Uw ingevulde emailadres is niet geldig. Probeer het opnieuw.")
        email=input("Voer een emailadres in: ")
    geboortedatum=input("Wat is uw geboortedatum: ")
    datum=datetime.datetime.strptime(geboortedatum, "%Y-%m-%d").date()
    term=int(input("Kies de gewenste duur (in maanden) van uw Luxe abonnement: "))
    aantal_dag=term*30

    start_date=strftime("%Y-%m-%d")
    date_1 = datetime.datetime.strptime(start_date, "%Y-%m-%d")

    end_date = date_1 + datetime.timedelta(days=aantal_dag)
    end_date=str(end_date)

    end_date = end_date.replace(' ', '')[:10].upper()
    date=datetime.datetime.today().strftime("%Y-%m-%d")
    abtype="Luxe"
    gewicht=int(input("Wat is uw huidige gewicht: "))


    cursor.execute("INSERT INTO klanten(klant_id, naam, achternaam, woonplaats, geboortedatum, aanmeldingsdatum, abonnementstype, aantal_bezoeken, wachtwoord, email, gewicht, begingewicht, abonnementsduur) VALUES ("+str(nieuw)+", '"+naam+"', '"+achternaam+"', '"+woonplaats+"', '"+str(datum)+"', '"+str(date)+"', '"+abtype+"', "+str(0)+", '"+wachtwoord+"', '"+email+"', "+str(gewicht)+", "+str(gewicht)+", '"+str(end_date)+"')")
    conn.commit()
    print("Uw klant ID is: "+str(nieuw))
    print("U bent succesvol ingeschreven bij Benno's Sportschool!")
registreer_zakelijk()
