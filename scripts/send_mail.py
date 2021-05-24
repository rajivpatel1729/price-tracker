import os
import smtplib
from email.mime.text import MIMEText
#from threading import Thread

def send_email(clients, product_name, curr_price):
    s = smtplib.SMTP('smtp.gmail.com')
    s.starttls()
    s.login(os.environ["USER_EMAIL"], os.environ["USER_PASS"])
    msg = MIMEText("Task Completed : " + product_name + " price dropped to" + str(curr_price))
    sender = os.environ["USER_EMAIL"]
    msg['Subject'] = "Project Price Checker"
    msg['From'] = sender

    for recipients in clients:
        s.sendmail(sender, recipients, msg.as_string())
    s.quit()
