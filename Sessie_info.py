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

	cursor.execute("SELECT sessie_id FROM sessies WHERE klant_id="+str(klantid))

	# retrieve the records from the database
	records1 = cursor.fetchall()

	records1=list(records1)
	orig=[]
	for i in records1:
		sessie=list(i)
		item=sessie[0]
		orig.append(item)

	maxid=str(max(orig))

	# execute our Query
	cursor.execute("SELECT * FROM sessies WHERE klant_id="+klantid+" AND sessie_id="+maxid)

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
	print("\nU heeft tijdens deze sessie de volgende activiteiten gedaan: "+activiteiten+"\n"+"U heeft in totaal "+sessieduur+" uur aan deze activiteiten besteed."+"\n"+"Dit houdt in dat u vandaag in totaal "+calorie+" heeft verbrand.")

toon_huidige_sessie()
