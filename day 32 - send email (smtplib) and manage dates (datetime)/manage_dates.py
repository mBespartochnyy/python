import datetime as dt, random, smtplib, keyring

# config
HOST = 'smtp.gmail.com'
PORT = 587
USER = 'monitoring@howdash.com'
PWD = keyring.get_password('Monitoring', USER)
MSG = """Subject: Testing Email From Server\n\nThis is <strong>third</strong> test"""

# get quote
with open('data/quotes.txt') as file:
	quotes = [quote.strip() for quote in file]
	quote_of_the_day = random.choice(quotes)

# identify day of week
now = dt.datetime.now()
# year = now.year
# month = now.month
day_of_week = now.weekday()

# send quote on thursday
if day_of_week == 3:
	print(quote_of_the_day)

	# message
	with smtplib.SMTP(host=HOST, port=PORT) as connection:
		connection.starttls()
		connection.login(user=USER, password=str(PWD))
		connection.sendmail(from_addr=USER, to_addrs=USER, msg=f"Subject:Quote of the Day\n\n{quote_of_the_day}")