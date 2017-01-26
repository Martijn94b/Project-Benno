import psycopg2
import sys
import smtplib
import random
import datetime
from time import strftime

def upgrade_ab():
    conn_string = "host='localhost' dbname='Sportschool' user='postgres' password='Burdeos1'"
	# print the connection string we will use to connect
    print ("Connecting to database\n	->%s" % (conn_string))

	# get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

	# conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()

    klantid=input("Voer een klant_ID in: ")
    wacht=input("Voer uw wachtwoord in: ")
    cursor.execute("SELECT wachtwoord, email FROM klanten WHERE klant_id="+str(klantid))

    passmail = cursor.fetchall()
    passmail=list(passmail)
    for i in passmail:
        lijst=list(i)
        password=lijst[0]
        email=lijst[1]

    if wacht==password:
        randomint=random.randrange(1000,9999)
        text="U heeft recentelijk geprobeerd om in te loggen bij Benno's Sportschool\nDe benodigde authenticatiecode is: "+str(randomint)+"\n\nWas u dit niet? Neem dan contact op met onze klantenservice\n\nBedankt voor uw geduld en graag tot ziens,\nKlantenservice Benno's Sportschool"

        fromaddr = 'bennossportschool1@gmail.com'
        toaddrs  = email
        msg = 'Subject: %s\n\n%s' % ("Authenticatiecode", text)

        # Credentials (if needed)
        username = 'bennossportschool1'
        password = 'januari2017'

        # The actual mail send
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username,password)
        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()

        count=0
        auth=int(input("Voer de authenticatiecode in die naar u is gestuurd: "))

        while auth!=randomint:
            if count<2:
                auth=int(input("Voer de authenticatiecode in die naar u is gestuurd: "))
                if auth!=randomint:
                    count+=1
                    print(count)
        if count>=2:
            sys.exit("U heeft 3 keer de verkeerde code ingevoerd, het proces wordt nu afgebroken")
        abtype=input("Kies uw gewenste abonnementstype (Basis/Luxe): ")
        while abtype not in ["Basis","Luxe"]:
                abtype=input("Kies uw gewenste abonnementstype (Basis/Luxe): ")
                if abtype=="":
                    sys.exit("Ongeldige invoer; proces wordt afgebroken.")
        term=int(input("Kies de gewenste duur (in maanden) van uw Luxe abonnement: "))
        aantal_dag=term*30

        start_date=strftime("%Y-%m-%d")
        date_1 = datetime.datetime.strptime(start_date, "%Y-%m-%d")

        end_date = date_1 + datetime.timedelta(days=aantal_dag)
        end_date=str(end_date)

        end_date = end_date.replace(' ', '')[:10].upper()

        if abtype=="Basis":
            prijs=term*20
        if abtype=="Luxe":
            prijs=term*40
        print("U wordt doorverwezen naar de betalingspagina van uw bank.")
        print("De kosten van uw gekozen tijdsduur zijn "+str(prijs)+" euro.")
        print("U wordt nu doorverwezen naar de betaalpagina van uw bank.")
        gesl=input("Is de betaling gelukt (placeholder):")
        if gesl in ["Ja", "ja"]:
                cursor.execute("UPDATE klanten SET abonnementstype='"+abtype+"', abonnementsduur='"+str(end_date)+"' WHERE klant_id="+str(klantid))
                conn.commit()
                print("Uw abonnement is succesvol gewijzigd.")
        else:
            print("Betaling mislukt; proces wordt afgebroken.")

upgrade_ab()
