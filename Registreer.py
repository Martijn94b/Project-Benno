import psycopg2
import datetime

def registreer():
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
    date=datetime.datetime.today().strftime("%Y-%m-%d")
    abtype=input("Kies een abonnementstype: ")
    abduur=input("Kies een termijn voor uw abonnement: ")
    gewicht=int(input("Wat is uw huidige gewicht: "))


    cursor.execute("INSERT INTO klanten(klant_id, naam, achternaam, woonplaats, geboortedatum, aanmeldingsdatum, abonnementstype, abonnementsduur, aantal_bezoeken, wachtwoord, email, gewicht, begingewicht) VALUES ("+str(nieuw)+", '"+naam+"', '"+achternaam+"', '"+woonplaats+"', '"+str(datum)+"', '"+str(date)+"', '"+abtype+"', "+str(abduur)+", "+str(0)+", '"+wachtwoord+"', '"+email+"', "+str(gewicht)+", "+str(gewicht)+")")
    conn.commit()
registreer()
