import pyttsx3
from firebase import firebase
from cryptography.fernet import Fernet

engine = pyttsx3.init()
rate = engine.getProperty('rate')               
engine.setProperty('rate', 150)


print("----------------------------------------------\nWelcome to Bankable OTP interface !\n----------------------------------------------")
engine.say("Welcome to Bankable OTP interface")
engine.runAndWait()
a = 2

while(a == 2):
    engine.say("Please enter your MMID number")
    engine.runAndWait()
    MMID = input("\nPlease enter your MMID: ")
    engine.say("Please verify your MMID number, {0}".format(MMID))
    engine.say("Please enter the number associated with following facilities. 1 to Proceed. 2 to re-enter the MMID number")
    engine.runAndWait()
    a = int(input("\nPlease enter the number associated with following facilities:-\n1 to Proceed.\n2 to re-enter the MMID number\n\nYour entry: "))

place = int(MMID) - int(1800221)

firebase = firebase.FirebaseApplication('https://crpyto-bank.firebaseio.com/')
address = '/crypt-data/GlArbgCoCgkYTPKN7q0L/' + str(place) + '/'
data = firebase.get(address, None)

chabi = "pBJ-07AfIo7RXhsS-32jmAfFm5hF0gz2YUm0n9Tp4a4="
f = Fernet(chabi)

email = firebase.get(address, 'Email')
email = email.encode()
emaildec = f.decrypt(email)
emailss = emaildec.decode()


import math, random,smtplib
def generateOTP() :
    string = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    OTP = ""
    length = len(string)
    for i in range(6):
        OTP += string[math.floor(random.random() * length)]
    return OTP

if __name__ == "__main__" :
    ans= generateOTP()
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("BASA.OTP@gmail.com", "Banking@App")
    subject = "Requested OTP : "
    body = "The requested otp is : "
    message = f'Subject :{subject}\n\n{body+ans}'
    s.sendmail(emailss,emailss, message)
    s.quit()
    otp=input("Enter the received OTP:")
    if otp == ans:
      print("OTP is correct")
    else:
      print("OTP is wrong :(")
