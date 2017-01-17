import smtplib

email=input('Wat is uw emailadres: ')
if '@' not in email:
    email=input('Wat is uw emailadres: ')

subject=input('Wat is uw probleem: ')

fromaddr = 'bennossportschool1@gmail.com'
toaddrs  = email
text="This message was sent with Python's smtplib"
msg = 'Subject: %s\n\n%s' % (subject, text)


# Credentials (if needed)
username = 'bennossportschool1'
password = 'januari2017'

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
