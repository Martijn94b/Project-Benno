import psycopg2

def toon_huidige_sessie():
    conn_string = "host='localhost' dbname='Sportschool' user='postgres' password='Burdeos1'"
	# print the connection string we will use to connect
    print ("Connecting to database\n	->%s" % (conn_string))

	# get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

	# conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()

    klantid=input("Voer een klant_ID in: ")

    cursor.execute("SELECT aanmeldingsdatum, abonnementstype, abonnementsduur, aantal_bezoeken FROM klanten WHERE klant_id="+str(klantid))

	# retrieve the records from the database
    records = cursor.fetchall()
    records=list(records)
    for i in records:
        lijst=list(i)
        aandate=str(lijst[0])
        abtype=lijst[1]
        abduur=str(lijst[2])
        aantal_bezoek=str(lijst[3])

    print("\nU bent bij Benno's Sportschool geregistreerd sinds: "+aandate+"\nUw huidige abonnementstype is: "+abtype+"\nUw abonnement is geldig tot: "+abduur+"\nU heeft onze sportschool nu "+aantal_bezoek+" keer bezocht.")

toon_huidige_sessie()
