import smtplib

user = input('Enter your gmail ')
password = input('Enter your password ')
receiver = input('Enter the receiver ')
msg = input('Enter the message ')
#num = input('Enter the number of emails you want to send ')
#x = 0
#x = int()
#num = int()
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(user, password)
server.sendmail(user, receiver, msg)
#x = x + 1
server.quit()
print("Successfully sent email")
