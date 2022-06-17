"""Template robot with Python."""
from ShopifyApp import Shopify
from mail import SendEmail
def main():
    shopify=Shopify()
    shopify.open_login_window()
    shopify.login()
    list_activity=shopify.open_workplace()
    installation_mail=open("InstallationMail.txt","r").read()
    uninstallation_mail=open("UninstallationMail.txt","r").read()
    cancel_recurring_charge=open("CancelMail.txt","r").read()
    mail=SendEmail()
    for mail_to in list_activity['Installed']:
        print(mail_to)
        subject="Thank you for joining our club"
        file=None
        to_="hrushikeshsonake@gmail.com"
        msg=mail.create_msg(file, installation_mail ,subject,to_)
        mail.send_mail(msg)
        
    for mail_to in list_activity['Uninstalled']:
        print(mail_to)
        subject='Let’s stay in touch!'
        file=None
        to_="hrushikeshsonake@gmail.com"
        msg=mail.create_msg(file, uninstallation_mail, subject,to_)
        mail.send_mail(msg)
        
    for mail_to in list_activity['Recurring charge cancelled']:
        print(mail_to)
        subject="Canceled?"
        file=None
        to_="vaishrishika@gmail.com"
        msg=mail.create_msg(file, cancel_recurring_charge, subject,to_)
        mail.send_mail(msg)

def minimal_task():
    print("Done.")


if __name__ == "__main__":
    minimal_task()
    main()
