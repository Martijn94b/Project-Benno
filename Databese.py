import psycopg2
import sys
import pprint

def toon_data():
	conn_string = "host='localhost' dbname='Sportschool' user='postgres' password='Burdeos1'"
	# print the connection string we will use to connect
	print ("Connecting to database\n	->%s" % (conn_string))

	# get a connection, if a connect cannot be made an exception will be raised here
	conn = psycopg2.connect(conn_string)

	# conn.cursor will return a cursor object, you can use this cursor to perform queries
	cursor = conn.cursor()

	klantid=input("Voer een klant_ID in: ")

	# execute our Query
	cursor.execute("SELECT * FROM klanten WHERE klant_id="+klantid)

	# retrieve the records from the database
	records = cursor.fetchall()

	# print out the records using pretty print
	# note that the NAMES of the columns are not shown, instead just indexes.
	# for most people this isn't very useful so we'll show you how to return
	# columns as a dictionary (hash) in the next example.
	pprint.pprint(records)

def toon_huidige_sessie():
	try:
		conn_string = "host='localhost' dbname='Sportschool' user='postgres' password='Burdeos1'"
		# print the connection string we will use to connect
		print ("Connecting to database\n	->%s" % (conn_string))

		# get a connection, if a connect cannot be made an exception will be raised here
		conn = psycopg2.connect(conn_string)

		# conn.cursor will return a cursor object, you can use this cursor to perform queries
		cursor = conn.cursor()

		klantid=input("Voer een klant_ID in: ")
		sessieid=input("Voer uw sessie ID in: ")

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
		print("\nU heeft tijdens deze sessie de volgende activiteiten gedaan: "+activiteiten+"\n"+"U heeft in totaal "+sessieduur+" uur aan deze activiteiten besteed."+"\n"+"Dit houdt in dat u vandaag in totaal "+calorie+" heeft verbrand.")
	except UnboundLocalError:
		print ("\nEr is geen sessie gevonden voor uw ingevoerde gegevens.\nProbeer het opnieuw.")

toon_huidige_sessie()

