#
# Simple smtplib implementation to send an e-mail
# (SMTP stands for "Simple Mail Transfer Protocol")
#

# import the smtp e-mail library
import smtplib

# import base64 for simple obfuscation
import base64

# create the smtp object
server = smtplib.SMTP('smtp.gmail.com', 587)

# define "from" and "to" addresses
from_address = "ulas.demirdag.test@gmail.com"
to_address = "ulas.demirdag@gmail.com"


def login():
    server.starttls()
    #obfuscated_password = base64.b64encode(bytes(u'PiRiL6__uLaS39', "utf-8"))
    obfuscated_password = 'UGlSaUw2X191TGFTMzk='
    print(obfuscated_password)
    server.login(from_address, base64.b64decode(obfuscated_password).decode("utf-8", "ignore"))

def send_email():
    msg = "" \
          "Hello - with obfuscation - 2!"
    server.sendmail(from_address, to_address, msg)

# define the main function
def main():

    # login
    login()

    # send e-mail
    send_email()

# call the main() function
if __name__ == '__main__':
    main()