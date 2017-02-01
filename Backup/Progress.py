import matplotlib.pyplot as plt
import psycopg2

def progress():
    conn_string = "host='localhost' dbname='Sportschool' user='postgres' password='Burdeos1'"
    # print the connection string we will use to connect
    print ("Connecting to database\n	->%s" % (conn_string))

    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    klantid=int(input("Wat is uw klant ID: "))
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

progress()
