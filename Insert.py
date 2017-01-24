import psycopg2
import datetime
def insert():
    conn_string = "host='localhost' dbname='Sportschool' user='postgres' password='Burdeos1'"
    # print the connection string we will use to connect
    print ("Connecting to database\n	->%s" % (conn_string))

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

    klantid=input("Wat is uw klant ID: ")
    wacht=input("Voer uw wachtwoord in: ")

    cursor.execute("SELECT wachtwoord FROM klanten WHERE klant_id="+str(klantid))

    passw = cursor.fetchall()
    passw=list(passw)
    for i in passw:
        lijst=list(i)
        password=lijst[0]


    if wacht==password:
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
        print("U heeft het verkeerde wachtwoord ingevuld; het proces wordt afgebroken.")


insert()
