import pickle #To write in dictionary
import os #Using to clear screen using defined clear() function
import time #Slow down execution using sleep()
clear = lambda: os.system('cls')
def fileWrite(filename,data):#Universal function to write to any mentioned file
    with open(filename,'wb') as file:
        pickle.dump(data,file)
def fileRead(filename):
    with open(filename,'rb') as file:
         data=pickle.load(file)
         return data
def register(): #Adds new user account
    usn=input("Enter a username:\n")
    usn=usn.strip()
    usn=usn+'e'
    accounts=fileRead("UserAcc")
    if usn in accounts:
        print("Account already exists!")
    else:
        pass1=input("Enter a password:\n")
        pass1=pass1.strip()
        while True:
         pass2=input("Confirm password:\n")
         pass2=pass2.strip()
         if pass2==pass1:
             accounts.update({usn:pass1})
             fileWrite('UserAcc',accounts)
             print('User account successfully created! You will now be redirected to the login page')
             break
         else:
             print("Oops password doesn't match! Try again:")
def master():
    mastchoice1=input("What would you like to do?\n1)Add provider\n2)Delete provider\n3)Manage User Accounts\n4)Logout\n")
    if mastchoice1=='1':
        mastchoice2=input("Which service would you like to edit?\n1)Restaurant\n2)Hotel\n3)Bus\n4)Spa\n5)Bicycle Repair\n")#Add other services here
        if mastchoice2=='1' or mastchoice2=='2' or mastchoice2=='3':
            if mastchoice2=='1':
                tempname="restaurant"
                try:
                    service=fileRead(tempname)
                except:
                    fileWrite(tempname,{})
                    service=fileRead(tempname)
            elif mastchoice2=='2':
                tempname="hotel"
                try:
                    service=fileRead(tempname)
                except:
                    fileWrite(tempname,{})
                    service=fileRead(tempname)
            elif mastchoice2=='3':
                tempname="bus"
                try:
                    service=fileRead(tempname)
                except:
                    fileWrite(tempname,{})
                    service=fileRead(tempname)
            while True:
                try:
                    npname,npseat=input("Enter Name\Available Slots\n").split('\\')
                except:
                    print("Incorrect number of inputs received")
                    time.sleep(3)
                    clear()
                    master()
                if npname in service:
                    print("Entry already exists!")
                    time.sleep(3)
                else:
                    service.update({npname:npseat})
                    break
            fileWrite(tempname,service)
            clear()
            print("Provider successfully added!")
            time.sleep(3)
            master()
        elif mastchoice2=='4' or mastchoice2=='5':
            if mastchoice2=='4':
                tempname="spa"
                try:
                    service=fileRead(tempname)
                except:
                    fileWrite(tempname,{})
                    service=fileRead(tempname)
            elif mastchoice2=='5':
                tempname="cycle"
                try:
                    service=fileRead(tempname)
                except:
                    fileWrite(tempname,{})
                    service=fileRead(tempname)
            while True:
                try:
                    if mastchoice2=='5':
                        nptype='cycle'
                        npname,npexp=input("Enter Name\Experience\n").split('\\')
                    else:
                        npname,nptype,npexp=input("Enter Name\Expertise\Experience\n").split('\\')
                except:
                    print("Incorrect number of inputs received")
                    time.sleep(3)
                    clear()
                    master()
                if npname in service:
                    ynchoice=input("Entry already exists! Do you want to add another provider?(y/n)\n")
                    if ynchoice=='n':
                        master()
                else:
                    service.update({npname:[npexp,nptype]})
                    break
            fileWrite(tempname,service)
            clear()
            print("Provider successfully added!")
            t=fileRead(tempname)
            print(t)
            input()
            time.sleep(3)
            master()    
    elif mastchoice1=='3':
        accounts = fileRead("UserAcc")
        print("Which account do you wish to manage?")
        for key in accounts:
            if key != "Mastere":
                print(key)  
        edchoice = input()
        if edchoice in accounts and edchoice[-1] == 'e':
            print(f"Do you wish to disable {edchoice}(y/n)?")
            yncheck = input()
            if yncheck == 'y':
                accounts[edchoice[0:-1]+'d'] = accounts[edchoice]
                del accounts[edchoice]
        elif edchoice in accounts and edchoice[-1] == 'd':
            print(f"Do you wish to enable {edchoice}?(y/n)")
            yncheck = input()
            if yncheck == 'y':
                accounts[edchoice[0:-1]+'e'] = accounts[edchoice]
                del accounts[edchoice]
        else:
            print("Account doesnt exist! Try again!")
            time.sleep(3)
            master()
        fileWrite("UserAcc",accounts)
    elif mastchoice1=='4':
        clear()
        print("Logging out");time.sleep(0.5);clear()
        print("Logging out.");time.sleep(0.5);clear()
        print("Logging out..");time.sleep(0.5);clear()
        print("Logging out...");time.sleep(0.5);clear()
        login()
def login(): #Checks and logs in user
    n=5
    accounts=fileRead("UserAcc")
    bool=True
    for key in accounts:
        if key[-1]=='e':
            print(key[0:-1])
        elif key[-1]=='d':
            print(key[0:-1],"(disabled)")
    usnchoice=input("Select an account\n")
    for key in accounts:
        if key.startswith(usnchoice) and key[-1]=='e':
            usnchoice = usnchoice + key[-1]
            bool=True
        elif key.startswith(usnchoice) and key[-1]=='d':
            usnchoice = usnchoice + key[-1]
            bool=False
    if usnchoice=="Mastere":
        loginpass=input("Enter your password\n")
        if loginpass==accounts[usnchoice]:
            master()
    elif usnchoice in accounts and bool==True:
        while n>=0:
            loginpass=input("Enter your password\n")
            if loginpass==accounts[usnchoice]:
                clear()
                print("Welcome ",usnchoice[0:-1],"!\nLoading");time.sleep(0.5);clear()
                print("Welcome ",usnchoice[0:-1],"!\nLoading.");time.sleep(0.5);clear()
                print("Welcome ",usnchoice[0:-1],"!\nLoading..");time.sleep(0.5);clear()
                print("Welcome ",usnchoice[0:-1],"!\nLoading...");time.sleep(0.5);clear()
                return True
            else:
                n=n-1
                if n!=0:
                    print("Incorrect Password. Try again!\nYou have ",n," tries remaining:")
                else:
                    print("Too many failed attempts. You will now be redirected to the login page")
                    accounts[usnchoice[0:-1]+'d']=accounts[usnchoice]
                    del accounts[usnchoice]
                    fileWrite('UserAcc',accounts)
                    return  False   
    elif usnchoice in accounts and bool==False:
        print("This account is disabled. Kindly contact the admin to re-enable your account")
        return False
    else:
        print("This user doesn't exist!")
        login()
'''#def hotres():
    
def booking():#Shows available services
    bookchoice=input("Choose a service:\n1)Hotel Bookings\n2)Restaurant Bookings\n3)Home Spa\n4)Bike Repair\n5)Tickets\n")
    if bookchoice==1 or bookchoice==2:
        hotres()     
    elif bookchoice==3:
       # print("Voucher page here")
    elif bookchoice==4:
        #print("Settings page here")
    else:
        print("Invalid Input")
        time.sleep(2)
        clear()
        booking()'''
def home():#Home page
    homechoice=input("What would you like to do today?\n1)Make a Booking\n2)Booking History\n3)Vouchers\n4)Settings\n")
    if homechoice==1:
        print("bookings page here")
    elif homechoice==2:
        print("History page here")
    elif homechoice==3:
        print("Voucher page here")
    elif homechoice==4:
        print("Settings page here")
    else:
        print("Invalid Input")
        time.sleep(2)
        clear()
        home()
try: #Starts Execution here
    fileRead("UserAcc")
except:
    fileWrite("UserAcc",{'Mastere':'mpass'})
while True:
    loginno=input("Welcome to Bustle!\n1.Login\n2.Register\n")
    if loginno=='1':
        bool=login()
        if bool==True:
            break
        else:
            time.sleep(3)
            clear()
    elif loginno=='2':
        register()
        time.sleep(3)
        clear()
    elif loginno=='disp': #Dev Command
        accounts=fileRead('UserAcc')
        print(accounts)
    elif loginno=='fclr': #Dev Command
        with open('UserAcc','wb') as file:
            pickle.dump(accounts,file)
    elif loginno=='m':#TEMPORARY
        master()
    else:
        print("Invalid Input")
        time.sleep(3)
        clear()
home()
