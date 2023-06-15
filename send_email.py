import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders

# Generate and send email with weather and COVID-19 information
def send_email(email, password, recipient, subject, message): 
    gmail_user = email
    gmail_app_password = password
    
    sent_from = gmail_user
    sent_to = [recipient, recipient]
    
    sent_subject = subject
    
    sent_body = message.encode('ascii', 'ignore').decode('ascii')
    
    email_text = """\
                From: %s
                To: %s
                Subject: %s

                %s
                """ % (sent_from, ", ".join(sent_to), sent_subject, sent_body)
    
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_app_password)
        server.sendmail(sent_from, sent_to, email_text)
        server.close()

        print('Email sent!')
        
    except Exception as exception:
        print("Error: %s!\n\n" % exception)
