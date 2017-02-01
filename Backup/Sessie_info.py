import psycopg2

def toon_sessie():
	conn_string = "host='localhost' dbname='Sportschool' user='postgres' password='Burdeos1'"
	# print the connection string we will use to connect
	print ("Connecting to database\n	->%s" % (conn_string))

	# get a connection, if a connect cannot be made an exception will be raised here
	conn = psycopg2.connect(conn_string)

	# conn.cursor will return a cursor object, you can use this cursor to perform queries
	cursor = conn.cursor()

	klantid=input("Voer een klant_ID in: ")
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

toon_sessie()
