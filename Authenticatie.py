import psycopg2
import smtplib
import random

def random_with_N_digits(n):
    range_start = 10**(4-1)
    range_end = (10**4)-1
    randint(range_start, range_end)

def authentication():
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

    passmail = cursor.fetchall()
    passmail=list(passmail)
    for i in passmail:
        lijst=list(i)
        password=lijst[0]
        email=lijst[1]
        print (password)

    if wacht==password:
        randomint=random.randrange(1000,9999)
        text="U heeft ons recentelijk geprobeerd om in te loggen bij Benno's Sportschool\nDe benodigde authenticatiecode is: "+str(randomint)+"\n\nWas u dit niet? Neem dan contact op met onze klantenservice\n\nBedankt voor uw geduld en graag tot ziens,\nKlantenservice Benno's Sportschool"

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

        check=0
        auth=input("Voer de authenticatiecode in die naar u is gestuurd: ")
        if auth!=randomint:
            while check<4:
                check+=1
                auth=input("Voer de authenticatiecode in die naar u is gestuurd: ")






