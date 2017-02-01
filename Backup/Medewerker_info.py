import psycopg2
import sys

def beheer():
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
    cursor.execute("SELECT klant_id FROM klanten")

    aantal_geb=cursor.fetchall()
    aantal_geb=list(aantal_geb)
    geblijst=[]
    for i in aantal_geb:
        lijst=list(i)
        aantal=lijst[0]
        geblijst.append(aantal)
    hoeveelheidgeb=len(geblijst)
    print("Er zijn op dit moment "+str(hoeveelheidgeb)+" gebruikers geregistreerd.")

    cursor.execute("SELECT klant_id FROM klanten WHERE abonnementstype='Basis'")

    aantal_geb=cursor.fetchall()
    aantal_geb=list(aantal_geb)
    geblijst=[]
    for i in aantal_geb:
        lijst=list(i)
        aantal=lijst[0]
        geblijst.append(aantal)
    hoeveelheidgeb1=len(geblijst)
    print("\nEr zijn op dit moment "+str(hoeveelheidgeb1)+" gebruikers met een Basis abonnement geregistreerd.")
    perc=float(hoeveelheidgeb1/hoeveelheidgeb*100)
    perc=round(perc,2)
    print("Dit betekent dat "+str(perc)+"% van de gebruikers een Basis abonnement heeft.")

    cursor.execute("SELECT klant_id FROM klanten WHERE abonnementstype='Luxe'")

    aantal_geb=cursor.fetchall()
    aantal_geb=list(aantal_geb)
    geblijst=[]
    for i in aantal_geb:
        lijst=list(i)
        aantal=lijst[0]
        geblijst.append(aantal)
    hoeveelheidgeb1=len(geblijst)
    print("\nEr zijn op dit moment "+str(hoeveelheidgeb1)+" gebruikers met een Luxe abonnement geregistreerd.")
    perc=float(hoeveelheidgeb1/hoeveelheidgeb*100)
    perc=round(perc,2)
    print("Dit betekent dat "+str(perc)+"% van de gebruikers een Luxe abonnement heeft.")


beheer()


