import smtplib

sender = 'samihir123@gmail.com'
receivers = ['samihir123@gmail.com']

message = """From: From Person <samihir123@gmail.com>
To: To Person <samihir123@gmail.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print "Successfully sent email"
except SMTPException:
   print "Error: unable to send email"