import smtplib
#from decouple import config
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import tkinter as tk
from tkinter import simpledialog
application_window = tk.Tk()

class SendEmail:
    #loading login credentials 
    def __init__(self):
        self.gmail_user = simpledialog.askstring("Input", "MailID?",parent=application_window)
        print(self.gmail_user)
        self.gmail_password =  simpledialog.askstring("Input", "Password", parent=application_window)
        print(self.gmail_password)

    #for appple mail make changes here
    def create_msg(self,file,msg_html,subject,to_):
        self.to_=to_
        msgRoot = MIMEMultipart('related')
        msgRoot['From'] = self.gmail_user
        msgRoot['To'] = self.to_
        msgRoot['Subject'] = subject
        message =MIMEMultipart('alternative')
        message.attach(MIMEText(msg_html,_subtype='html'))
        msgRoot.attach(message)
        return msgRoot
    
    def send_mail(self,msgRoot,):
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(self.gmail_user, self.gmail_password) #Login to SMTP server
            smtp.send_message(msgRoot, self.gmail_user,self.to_)
