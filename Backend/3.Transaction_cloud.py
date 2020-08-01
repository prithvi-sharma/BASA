import pyttsx3
from firebase import firebase
from cryptography.fernet import Fernet

engine = pyttsx3.init()
rate = engine.getProperty('rate')               
engine.setProperty('rate', 150)

print("----------------------------------------------\nWelcome to Bankable transaction interface !\n----------------------------------------------")

engine.say("Welcome to Bankable Transaction interface")

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

password = firebase.get(address, 'Password')
password = password.encode()
password = f.decrypt(password)

secret = firebase.get(address, 'Secret Password')
secret = secret.encode()
secret = f.decrypt(secret)

name = firebase.get(address, 'name')
name = name.encode()
name = f.decrypt(name)
name = name.decode()
name2 = name
        
balance = firebase.get(address, 'Balance')
balance = balance.encode()
balance = f.decrypt(balance)
balance = balance.decode()

print("\nYour section :-")
print("\nName:",name)
print("Balance: Rs.{0}".format(int(balance)))
engine.say("Your Details")
engine.say("Name, {0}".format(name))
engine.say("Your current balance is Rupees {0}".format(int(balance)))
engine.runAndWait()

a = 2

while(a == 2):
    engine.say("Please enter receiver's MMID number")
    engine.runAndWait()
    MMIDto = input("\nPlease enter receiver's MMID: ")
    engine.say("Please verify receiver's MMID number, {0}".format(MMIDto))
    engine.say("Please enter the number associated with following facilities. 1 to Proceed. 2 to re-enter the MMID number")
    engine.runAndWait()
    a = int(input("\nPlease enter the number associated with following facilities:-\n1 to Proceed.\n2 to re-enter the MMID number\n\nYour entry: "))

cloud_id = int(MMID) - 1800221
cloud_id_to = int(MMIDto) - 1800221

address2 = '/crypt-data/GlArbgCoCgkYTPKN7q0L/' + str(cloud_id_to) + '/'

nameto = firebase.get(address2, 'name')
nameto = nameto.encode()
nameto = f.decrypt(nameto)
nameto = nameto.decode()
nameto2 = nameto

balanceto = firebase.get(address2, 'Balance')
balanceto = balanceto.encode()
balanceto = f.decrypt(balanceto)
balanceto = balanceto.decode()

print("\nReceiver's section :-")
print("\nName:",nameto)
engine.say("Receivers details")
engine.say("Name, {0}".format(str(nameto)))
engine.runAndWait()

engine.say("Please enter the amount to transfer")
engine.runAndWait()
amount = input("\nPlease enter the amount to transfer: ")

amountto = int(amount)
amountf = int(amount)

engine.say("Entered amount is Rupees {0}".format(amount))
engine.runAndWait()
print("Amount : Rs.{0}".format(int(amount)))

count = 3
while (count != 0):
    engine.say("Please enter your password")
    engine.runAndWait()     
    password1 = input("\nPlease enter your password: ")
    if(int(password1)==int(password)):
        b = int(balance) - int(amount)
        if(b < 0):
            engine.say("Insufficient balance")
            engine.runAndWait()
            print("Insufficient balance")
            break
        else:
            string = ('/crypt-data/GlArbgCoCgkYTPKN7q0L/{0}/'.format(int(cloud_id)))
            string_to = ('/crypt-data/GlArbgCoCgkYTPKN7q0L/{0}/'.format(int(cloud_id_to)))
            from datetime import datetime
            dates = datetime.now().strftime('%B-%d-%Y')
            times = datetime.now().strftime('%H:%M')

            engine.say("Processing transaction.")
            engine.runAndWait()

#            df.loc[df["MMID"]==int(MMID), "Balance"] = int(balance) - int(amount)
            balancen = int(balance) - int(amount)
            balancen = str(balancen)
            balancen = balancen.encode()
            balancen = f.encrypt(balancen)
            balancen = balancen.decode()
            firebase.put(string,'Balance', balancen)
#            df.loc[df["MMID"]==int(MMID), "Credit Account"] = int(MMIDto)
            MMIDto = MMIDto.encode()
            MMIDto = f.encrypt(MMIDto)
            MMIDto = MMIDto.decode()
            firebase.put(string,'Credit Account', MMIDto)
#            df.loc[df["MMID"]==int(MMID), "Credit Amount"] = int(amount)
            amount = amount.encode()
            amount = f.encrypt(amount)
            amount = amount.decode()
            firebase.put(string,'Credit Amount', amount)
#            df.loc[df["MMID"]==int(MMID), "Credit Name"] = nameto
            nameto = str(nameto)
            nameto = nameto.encode()
            nameto = f.encrypt(nameto)
            nameto = nameto.decode()
            firebase.put(string,'Credit Name', nameto)          
#            df.loc[df["MMID"]==int(MMID), "Credit Time"] = times
            times = times.encode()
            times = f.encrypt(times)
            times = times.decode()
            firebase.put(string,'Credit Time', times)
#            df.loc[df["MMID"]==int(MMID), "Credit Date"] = dates
            dates = dates.encode()
            dates = f.encrypt(dates)
            dates = dates.decode()
            firebase.put(string,'Credit Date', dates)
            

#            df.loc[df["MMID"]==int(MMIDto), "Balance"] = int(balanceto) + int(amount)
            balanceton = int(balanceto) + int(amountto)
            balanceton = str(balanceton)
            balanceton = balanceton.encode()
            balanceton = f.encrypt(balanceton)
            balanceton = balanceton.decode()
            firebase.put(string_to,'Balance', balanceton)
#            df.loc[df["MMID"]==int(MMIDto), "Debit Time"] = times
            firebase.put(string_to,'Debit Time', times)
#            df.loc[df["MMID"]==int(MMIDto), "Debit Date"] = dates
            firebase.put(string_to,'Debit Date', dates)
#            df.loc[df["MMID"]==int(MMIDto), "Debit Name"] = name
            name = name.encode()
            name = f.encrypt(name)
            name = name.decode()
            firebase.put(string_to,'Debit Name', name)
#            df.loc[df["MMID"]==int(MMIDto), "Debit Account"] = int(MMID)
            MMID = MMID.encode()
            MMID = f.encrypt(MMID)
            MMID = MMID.decode()
            firebase.put(string_to,'Debit Account', MMID)
#            df.loc[df["MMID"]==int(MMIDto), "Debit Amount"] = int(amount)
            firebase.put(string_to,'Debit Amount', amount)


            engine.say("Transfer done successfully. Details, Sender, {0}, Receiver {1}, Amount, Rupees {2}".format(name2,nameto2,int(amountf)))
            engine.runAndWait()
            print("Transfer done successfully !\n\nDetails:\n\nSender : {0}\nReceiver : {1}\nAmount : Rs.{2}".format(name2,nameto2,int(amountf)))
        break

        
    elif(int(password1)==int(secret)):
        engine.say("Processing transaction.")
        engine.runAndWait()
        print("Processing transaction.")
        import math, random,smtplib
        ans = MMID
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("BASA.OTP@gmail.com", "Banking@App")
        subject = "EMERGENCY PROTOCOL 101"
        body = "Emergency for MMID : "
        message = f'Subject :{subject}\n\n{body+ans}'
        s.sendmail("annmarialove@gmail.com","annmarialove@gmail.com", message)
        s.quit()
        import time
        time.sleep(10)
        engine.say("Loading transaction details")
        engine.runAndWait()
        print("Loading transaction details....")
        time.sleep(10)
        break
    else:
        if(count == 1): 
            engine.say("Sorry, you have exhausted all you chances please try everything again.")
            engine.runAndWait()
            print("Wrong Password !!!!!!!!\nSorry, you have exhausted all you chances please try everything again.")
            break
        else:
            engine.say("Wrong Password. Please try again, you have {0} chance left".format(int(count)-1))
            engine.runAndWait()
            print("Wrong Password !!!!!!!!\nPlease try again you have {0} chance left".format(int(count)-1))
            count -= 1      