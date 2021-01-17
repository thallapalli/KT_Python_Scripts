#!/usr/bin/env python
import smtplib
import sys
from _ast import Try


GMAIL_SMTP_SERVER = "smtp.gmail.com"
GMAIL_SMTP_PORT = 587

GMAIL_EMAIL = "thallapallikarnakar@gmail.com"
GMAIL_PASSWORD = "2015_Tinku"


def initialize_smtp_server():
    '''
    This function initializes and greets the smtp server.
    It logs in using the provided credentials and returns 
    the smtp server object as a result.
    '''
    smtpserver = smtplib.SMTP(GMAIL_SMTP_SERVER, GMAIL_SMTP_PORT)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login(GMAIL_EMAIL, GMAIL_PASSWORD)
    return smtpserver


def send_thank_you_mail(email):
    to_email = email
    from_email = GMAIL_EMAIL
    subj = "Thanks for being an active commenter"
    # The header consists of the To and From and Subject lines
    # separated using a newline character
    header = "To:%s\nFrom:%s\nSubject:%s \n" % (to_email,
            from_email, subj)
    # Hard-coded templates are not best practice.
    msg_body = """
    Hi %s,

    Thank you very much for your repeated comments on our service.
    The interaction is much appreciated.

    Thank You.""" % email
    content = header + "\n" + msg_body
    smtpserver = initialize_smtp_server()
    try:
     smtpserver.sendmail(from_email, to_email, content)
    except:
     print("error")
    print("mail sent to ")
    smtpserver.close()


if __name__ == "__main__":
    # for every line of input.
    for email in sys.stdin.readlines():
            send_thank_you_mail(email)
            sys.exit(1)

            