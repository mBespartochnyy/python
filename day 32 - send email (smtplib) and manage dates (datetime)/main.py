from datetime import datetime
import pandas as pd, os, random, smtplib, keyring

# config
HOST = 'smtp.gmail.com'
PORT = 587
USER = 'monitoring@howdash.com'
PWD = keyring.get_password('Monitoring', USER)
LETTERS_DIR = 'letter_templates/'
letters = []

# get data
birthdays = pd.read_csv('data/birthdays.csv')

# 2. Check if today matches a birthday in the birthdays.csv
current_month = datetime.now().month
current_day = datetime.now().day

filtered_birthdays = birthdays[(birthdays['month'] == current_month) & (birthdays['day'] == current_day)]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
with os.scandir(LETTERS_DIR) as files:
	for file in files:
		with open(LETTERS_DIR + file.name) as letter:
			content = letter.read()
			letters.append(content)

# 4. Send the letter generated in step 3 to that person's email address.
if len(filtered_birthdays):
	for i, row in filtered_birthdays.iterrows():
		name = row['name']
		email = row['email']
		letter = random.choice(letters).replace('[NAME]', name)
		with smtplib.SMTP(host=HOST, port=PORT) as connection:
			connection.starttls()
			connection.login(user=USER, password=str(PWD))
			connection.sendmail(from_addr=USER, to_addrs=email, msg=f"Subject:Happy Birthday, {name}\n\n{letter}")
