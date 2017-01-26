import psycopg2
import sys
import smtplib
import random
import datetime
import matplotlib.pyplot as plt
from time import strftime

def registreer():
    conn_string = "host='localhost' dbname='Sportschool' user='postgres' password='Burdeos1'"
    # print the connection string we will use to connect

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

    naam=input("\nWat is uw naam: ")
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
    print("Uw klant ID is: "+str(nieuw))
    print("U bent succesvol ingeschreven bij Benno's Sportschool!")

def registreer_zakelijk():

    conn_string = "host='localhost' dbname='Sportschool' user='postgres' password='Burdeos1'"
    # print the connection string we will use to connect

    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()

    auth=input("\nVul de medewerkerauthenticatiecode in: ")
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

def upgrade_ab():
    conn_string = "host='localhost' dbname='Sportschool' user='postgres' password='Burdeos1'"
	# print the connection string we will use to connect

	# get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

	# conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()

    klantid=input("\nVoer uw klant_ID in: ")
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


def insert():
    conn_string = "host='localhost' dbname='Sportschool' user='postgres' password='Burdeos1'"
    # print the connection string we will use to connect

    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()

    # execute our Query
    cursor.execute("SELECT sessie_id FROM sessies")

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

    klantid=input("\nVoer uw klant ID in: ")
    wacht=input("Voer uw wachtwoord in: ")

    cursor.execute("SELECT wachtwoord FROM klanten WHERE klant_id="+str(klantid))

    passw = cursor.fetchall()
    passw=list(passw)
    for i in passw:
        lijst=list(i)
        password=lijst[0]


    if wacht==password:
        cursor.execute("SELECT abonnementsduur, abonnementstype FROM klanten WHERE klant_id="+klantid)

        # retrieve the records from the database
        records = cursor.fetchall()

        records=list(records)
        for i in records:
            sessie=list(i)
            expire=str(sessie[0])
            abtype=sessie[1]

        nu=strftime("%Y-%m-%d")
        d1=datetime.datetime.strptime(nu, "%Y-%m-%d").date()
        d2 = datetime.datetime.strptime(expire, "%Y-%m-%d").date()
        if d1<d2 and abtype=="Luxe":
            gewicht=int(input("Wat is uw huidige gewicht: "))

            cursor.execute("SELECT naam, achternaam FROM klanten WHERE klant_id="+str(klantid))
            gegevens=cursor.fetchall()
            for i in gegevens:
                lijst=list(i)
                naam=lijst[0]
                achternaam=lijst[1]

            verbrand=0
            sessieduur=0
            activ=[]
            keus=input("Wilt u een activiteit registreren Ja/Nee")
            while keus not in ["Ja", "ja", 'Nee', "nee"]:
                keus=input("Wilt u een activiteit registreren Ja/Nee")
            while keus=="Ja" or keus=="ja":
                # get a connection, if a connect cannot be made an exception will be raised here
                conn = psycopg2.connect(conn_string)

                # conn.cursor will return a cursor object, you can use this cursor to perform queries
                cursor = conn.cursor()

                act=input("Voer een activiteit in: ")
                aantal=int(input("Hoeveel minuten heeft u aan deze activiteit besteed: "))
                activ.append(act)

                cursor.execute("SELECT calorie FROM activiteiten WHERE activiteit='"+act+"'")

                # retrieve the records from the database
                records1 = cursor.fetchall()
                records1=list(records1)
                sessieduur+=aantal
                string=""
                string+=(act+", ")
                for i in records1:
                    calorie=list(i)
                    item=calorie[0]*aantal*gewicht
                    verbrand+=item

                keus=input("Wilt u een activiteit registreren Ja/Nee")
                while keus not in ["Ja", "ja", 'Nee', "nee"]:
                    keus=input("Wilt u nog een activiteit registreren Ja/Nee")
            if keus=="Nee" or keus=="nee" and verbrand==0:
                print("Activiteit registratie geannuleerd")
            elif keus=="Nee" or keus=="nee" and verbrand>0:
                activstr=str(activ)
                activ2 = activstr.replace("[", "")
                activ3 = activ2.replace("]", "")
                activfinal =activ3.replace("'","")
                date=datetime.datetime.today().strftime("%Y-%m-%d")

                #insert data into databese
                cursor.execute("INSERT INTO sessies(sessie_id, klant_id, naam, achternaam, activiteiten, sessieduur, calorie, gewicht, datum) VALUES ("+str(nieuw)+", "+str(klantid)+", '"+naam+"', '"+achternaam+"', '"+activfinal+"', "+str(sessieduur)+", "+str(verbrand)+", "+str(gewicht)+", '"+str(date)+"')")
                conn.commit()
                verbrand=round(verbrand,2)
                print("\nU heeft tijdens deze sessie "+str(verbrand)+" kilocalorieen verbrand")
                print("Uw sessie is succesvol opgeslagen in de database.")

                cursor.execute("SELECT aantal_bezoeken FROM klanten")

                # retrieve the records from the database
                records2 = cursor.fetchall()

                records2=list(records2)
                for i in records2:
                    lijst2=list(i)
                    aantalbez=lijst2[0]

                nieuw=aantalbez+1
                #Apply changes
                cursor.execute("UPDATE klanten SET aantal_bezoeken="+str(nieuw)+", gewicht="+str(gewicht)+" WHERE klant_id="+str(klantid))
                conn.commit()
        else:
            print("Uw Luxe abonnement is verlopen; verleng uw abonnement als u wilt blijven sporten bij Benno's Sportschool")
            cursor.execute("UPDATE klanten SET abonnementstype='Geen' WHERE klant_id="+klantid)
    else:
        print("U heeft het verkeerde wachtwoord ingevuld; het proces wordt afgebroken.")


def sessie_info():
	conn_string = "host='localhost' dbname='Sportschool' user='postgres' password='Burdeos1'"
	# print the connection string we will use to connect

	# get a connection, if a connect cannot be made an exception will be raised here
	conn = psycopg2.connect(conn_string)

	# conn.cursor will return a cursor object, you can use this cursor to perform queries
	cursor = conn.cursor()

	klantid=input("\nVoer uw klant_ID in: ")
	wacht=input("Voer uw wachtwoord in: ")

	cursor.execute("SELECT wachtwoord FROM klanten WHERE klant_id="+str(klantid))

	passw = cursor.fetchall()
	passw=list(passw)
	for i in passw:
		lijst=list(i)
		password=lijst[0]

	if wacht==password:

		try:
			sessieid=input("Voer een sessie_ID in: ")

			# execute our Query
			cursor.execute("SELECT * FROM sessies WHERE klant_id="+klantid+" AND sessie_id="+sessieid)

			# retrieve the records from the database
			records = cursor.fetchall()
			records=list(records)
			for i in records:
				lijst=list(i)
				activiteiten=lijst[4]
				sessieduur=lijst[5]
				calorie=lijst[6]
				calorie=str(calorie)
				sessieduur=str(sessieduur)
			print("\nU heeft tijdens deze sessie de volgende activiteiten gedaan: "+activiteiten+"\n"+"U heeft in totaal "+sessieduur+" minuten aan deze activiteiten besteed."+"\n"+"Dit houdt in dat u in totaal "+calorie+" kilocalorieen heeft verbrand.")
		except UnboundLocalError:
			print("Er zijn geen resultaten voor uw ingevulde klant ID en sessie ID.")
	else:
		print("Uw ingevulde ingeloggegevens zijn niet correct; het proces is afgebroken.")


def progress():
    conn_string = "host='localhost' dbname='Sportschool' user='postgres' password='Burdeos1'"
    # print the connection string we will use to connect

    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    klantid=int(input("\nVoer uw klant ID in: "))
    wacht=input("Voer uw wachtwoord in: ")

    cursor.execute("SELECT wachtwoord FROM klanten WHERE klant_id="+str(klantid))

    passw = cursor.fetchall()
    passw=list(passw)
    for i in passw:
        lijst=list(i)
        password=lijst[0]

    if wacht==password:

    # execute our Query
        cursor.execute("SELECT gewicht, sessie_id  FROM sessies WHERE klant_id="+str(klantid))

    # retrieve the records from the database
        records = cursor.fetchall()

        records=list(records)
        orig=[]
        orig2=[]
        orig3=[]
        for i in records:
            sessie=list(i)
            gewicht=sessie[0]
            sessieid=sessie[1]
            orig.append(gewicht)
            orig2.append(sessieid)

        for x in range(0,len(orig2),1):
            orig3.append(x)

        plt.figure()

        #create some data
        x_series = orig3
        y_series_1 = [x*1 for x in orig]

        #plot the two lines
        plt.plot(x_series, y_series_1)

        #add in labels and title
        plt.xlabel("Sessie nummer")
        plt.ylabel("Gewicht in kg")
        plt.title("Gewicht voortgang")

        #add limits to the x and y axis
        plt.xlim(0,(len(orig3)+1),1)
        plt.ylim(50, 150)

        #save figure


        voortg=    cursor.execute("SELECT begingewicht FROM klanten WHERE klant_id="+str(klantid))

        # retrieve the records from the database
        records1 = cursor.fetchall()

        records1=list(records1)
        for i in records1:
            lijst=list(i)
            gewicht=lijst[0]

        cursor.execute("SELECT sessie_id FROM sessies WHERE klant_id="+str(klantid))

        # retrieve the records from the database
        records2 = cursor.fetchall()

        records2=list(records2)
        for i in records2:
            lijst2=list(i)
            maxses=max(lijst2)

        cursor.execute("SELECT gewicht FROM sessies WHERE sessie_id="+str(maxses))

        records3 = cursor.fetchall()

        records3=list(records3)
        for i in records3:
            lijst=list(i)
            gewicht1=lijst[0]

        print("Uw gewicht bij uw aanmelding was: "+str(gewicht)+" kilo.")
        print("Uw huidige gewicht is: "+str(gewicht1)+" kilo")
        print("Dit houdt in dat u gedurende uw abonnement bij onze sportschool "+str(gewicht-gewicht1)+" kilo bent afgevallen.")

        plt.savefig("example.png")
        print("\nUw voortgangsgrafiek is succesvol opgeslagen.")

    else:
        print("Uw ingevulde ingeloggegevens zijn niet correct; het proces is afgebroken.")


def prive_info():
    conn_string = "host='localhost' dbname='Sportschool' user='postgres' password='Burdeos1'"
	# print the connection string we will use to connect

	# get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

	# conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()

    klantid=input("\nVoer uw klant_ID in: ")
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


    cursor.execute("SELECT aanmeldingsdatum, abonnementstype, abonnementsduur, aantal_bezoeken FROM klanten WHERE klant_id="+klantid)

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

#keuze engine

print("Welkom bij Benno's Sportschool")
print("Selecteer 1 van de volgende opties:")
print("     1. Registreren bij onze Sportschool.")
print("     2. Uw abonnement wijzigen.")
print("     3. Uw sportsessie vastleggen.")
print("     4. Informatie over uw sportsessies opvragen.")
print("     5. Informatie over uw voortgang opvragen.")
print("     6. Uw prive informatie opvragen.")
print("     7. Annuleren")

keuze=input("\nVoer uw keuze in: ")
while keuze not in ["1","2","3","4","5","6","7"]:
            print("U heeft geen geldig antwoord gegeven; probeer het opnieuw.")
            keuze=input("Voer uw keuze in: ")
herhaal="ja"
while keuze!="7" or herhaal not in ["nee","Nee"]:
    if keuze=="1":
        doorv=input("Bent u doorverwezen door een professional? Ja/Nee")
        while doorv not in ["ja","Ja","nee","Nee"]:
            print("U heeft geen geldig antwoord gegeven; probeer het opnieuw.")
            doorv=input("Bent u doorverwezen door een professional? Ja/Nee")
        if doorv in ["ja", "Ja"]:
            registreer_zakelijk()
        else:
            registreer()
        herhaal=input("Wilt u gebruikmaken van een andere optie? Ja/Nee")
        while herhaal not in ["ja","Ja","nee","Nee"]:
            print("U heeft geen geldig antwoord gegeven; probeer het opnieuw.")
            herhaal=input("Wilt u gebruikmaken van een andere optie? Ja/Nee")
        if herhaal=="ja" or herhaal=="Ja":
            keuze=input("Voer uw keuze in: ")
            while keuze not in ["1","2","3","4","5","6","7"]:
                print("U heeft geen geldig antwoord gegeven; probeer het opnieuw.")
                keuze=input("Voer uw keuze in: ")
        if herhaal=="nee" or herhaal=="Nee":
            keuze="7"

    if keuze=="2":
        upgrade_ab()
        herhaal=input("Wilt u gebruikmaken van een andere optie? Ja/Nee")
        while herhaal not in ["ja","Ja","nee","Nee"]:
            print("U heeft geen geldig antwoord gegeven; probeer het opnieuw.")
            herhaal=input("Wilt u gebruikmaken van een andere optie? Ja/Nee")
        if herhaal=="ja" or herhaal=="Ja":
            keuze=input("Voer uw keuze in: ")
            while keuze not in ["1","2","3","4","5","6","7"]:
                print("U heeft geen geldig antwoord gegeven; probeer het opnieuw.")
                keuze=input("Voer uw keuze in: ")
        if herhaal=="nee" or herhaal=="Nee":
            keuze="7"

    if keuze=="3":
        insert()
        herhaal=input("Wilt u gebruikmaken van een andere optie? Ja/Nee")
        while herhaal not in ["ja","Ja","nee","Nee"]:
            print("U heeft geen geldig antwoord gegeven; probeer het opnieuw.")
            herhaal=input("Wilt u gebruikmaken van een andere optie? Ja/Nee")
        if herhaal=="ja" or herhaal=="Ja":
            keuze=input("Voer uw keuze in: ")
            while keuze not in ["1","2","3","4","5","6","7"]:
                print("U heeft geen geldig antwoord gegeven; probeer het opnieuw.")
                keuze=input("Voer uw keuze in: ")
        if herhaal=="nee" or herhaal=="Nee":
            keuze="7"

    if keuze=="4":
        sessie_info()
        herhaal=input("Wilt u gebruikmaken van een andere optie? Ja/Nee")
        while herhaal not in ["ja","Ja","nee","Nee"]:
            print("U heeft geen geldig antwoord gegeven; probeer het opnieuw.")
            herhaal=input("Wilt u gebruikmaken van een andere optie? Ja/Nee")
        if herhaal=="ja" or herhaal=="Ja":
            keuze=input("Voer uw keuze in: ")
            while keuze not in ["1","2","3","4","5","6","7"]:
                print("U heeft geen geldig antwoord gegeven; probeer het opnieuw.")
                keuze=input("Voer uw keuze in: ")
        if herhaal=="nee" or herhaal=="Nee":
            keuze="7"

    if keuze=="5":
        progress()
        herhaal=input("Wilt u gebruikmaken van een andere optie? Ja/Nee")
        while herhaal not in ["ja","Ja","nee","Nee"]:
            print("U heeft geen geldig antwoord gegeven; probeer het opnieuw.")
            herhaal=input("Wilt u gebruikmaken van een andere optie? Ja/Nee")
        if herhaal=="ja" or herhaal=="Ja":
            keuze=input("Voer uw keuze in: ")
            while keuze not in ["1","2","3","4","5","6","7"]:
                print("U heeft geen geldig antwoord gegeven; probeer het opnieuw.")
                keuze=input("Voer uw keuze in: ")
        if herhaal=="nee" or herhaal=="Nee":
            keuze="7"

    if keuze=="6":
        prive_info()
        herhaal=input("Wilt u gebruikmaken van een andere optie? Ja/Nee")
        while herhaal not in ["ja","Ja","nee","Nee"]:
            print("U heeft geen geldig antwoord gegeven; probeer het opnieuw.")
            herhaal=input("Wilt u gebruikmaken van een andere optie? Ja/Nee")
        if herhaal=="ja" or herhaal=="Ja":
            keuze=input("Voer uw keuze in: ")
            while keuze not in ["1","2","3","4","5","6","7"]:
                print("U heeft geen geldig antwoord gegeven; probeer het opnieuw.")
                keuze=input("Voer uw keuze in: ")
        if herhaal=="nee" or herhaal=="Nee":
            keuze="7"

    if keuze=="7":
        print("Bedankt en tot ziens!")
        break
