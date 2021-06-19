import smtplib

sender = 'notification@dryicehcl.com'
receivers = ['prateek_srivastava@hcl.com']


message = """From: notification@dryicehcl.com <notification@dryicehcl.com>
To: MTaaS Team <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   s = smtplib.SMTP('10.1.1.61')
   # s.starttls()
   s.sendmail(sender, receivers, message)         
   print ("Successfully sent email")

except Exception as e:
	print(str(e))
	print ("Error: unable to send email")