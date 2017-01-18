import psycopg2

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

    maxn=max(orig)
    nieuw=maxn+1
    klantid=input("Wat is uw klant ID: ")

    cursor.execute("SELECT naam, achternaam FROM klanten WHERE klant_id="+str(klantid))
    gegevens=cursor.fetchall()
    for i in gegevens:
        lijst=list(i)
        naam=lijst[0]
        achternaam=lijst[1]

    activiteit=input("Wat waren uw activiteiten deze sessie: ")
    sessieduur=input("Hoe lang duurde deze sessie: ")
    calorie=input("Hoeveel calorieen heeft u verbrand: ")

    cursor.execute("INSERT INTO sessies(sessie_id, klant_id, naam, achternaam, activiteiten, sessieduur, calorie) VALUES ("+str(nieuw)+", "+str(klantid)+", '"+naam+"', '"+achternaam+"', '"+activiteit+"', "+str(sessieduur)+", "+str(calorie)+")")
    conn.commit()

insert()
