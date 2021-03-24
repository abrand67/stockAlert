import ssl
import getpass
import smtplib
import requests
import traceback

status = 'Back-In-Stock'
r = requests.get('https://bravocompanyusa.com/bcm-standard-9-enhanced-fluted-300-blackout-barrel-stripped/')
gmail_user = 'user@gmail.com'

sent_from = gmail_user
to = ['user@gmail.com', 'phonenumber@mms.att.net']
subject = 'BCM 9" 300 Blackout Barrel Back In Stock'
body = 'https://bravocompanyusa.com/bcm-standard-9-enhanced-fluted-300-blackout-barrel-stripped/'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

if __name__ == '__main__':
		gmail_password = getpass.getpass()
		if status not in r.text:
			try:
				context = ssl.create_default_context()
				with smtplib.SMTP('smtp.gmail.com', 587) as server:
					server.starttls(context=context)
					server.login(gmail_user, gmail_password)
					server.sendmail(sent_from, to, email_text)
			except Exception:
				print(traceback.format_exc())
		else:
			print('Still not available')
