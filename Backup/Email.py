import smtplib

email=input('Wat is uw emailadres: ')
if '@' not in email:
    email=input('Wat is uw emailadres: ')

probleem=input('Wat is uw probleem: ')
text="U heeft ons recentelijk een mail gestuurd betreffende het volgende probleem:"+"\n"+"\n"+probleem+"\n"+"\n"+"Wij zullen kijken wat wij voor u kunnen betekenen en hopen dit probleem dan ook snel te hebben opgelost"+"\n"+"\n"+"Bedankt voor uw geduld en graag tot ziens, "+"\n"+"Klantenservice Benno's Sportschool"

fromaddr = 'bennossportschool1@gmail.com'
toaddrs  = email
msg = 'Subject: %s\n\n%s' % ("Klantenservice probleemoplossing", text)


# Credentials (if needed)
username = 'bennossportschool1'
password = 'januari2017'

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()

