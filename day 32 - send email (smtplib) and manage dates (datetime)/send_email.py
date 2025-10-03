import smtplib, keyring

# config
HOST = 'smtp.gmail.com'
PORT = 587
USER = 'monitoring@howdash.com'
PWD = keyring.get_password('Monitoring', USER)
MSG = """Subject: Testing Email From Server\n\nThis is <strong>third</strong> test"""

# message
with smtplib.SMTP(host=HOST, port=PORT) as connection:
	connection.starttls()
	connection.login(user=USER, password=str(PWD))
	connection.sendmail(from_addr=USER, to_addrs=USER, msg=MSG)