import pickle #To write in dictionary
import os #Using to clear screen using defined clear() function
import time #Slow down execution using sleep()
accounts={'Mastere':'mpass'}
restlist=[]
clear = lambda: os.system('cls')
def fileWrite(filename,data):#Universal function to write to any mentioned file
    with open(filename,'wb') as file:
        pickle.dump(data,file)
def fileRead(filename):
    with open(filename,'rb') as file:
         accounts=pickle.load(file)
         return accounts
def register(): #Adds new user account
    usn=input("Enter a username:\n")
    usn=usn.strip()
    usn=usn+'e'
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
    mastchoice1=input("What would you like to do?\n1)Add provider\n2)Delete provider\n3)Manage User Accounts\n")
    #mastchoice2=input("Which service would you like to edit?\n1)Restaurant")
    if mastchoice1=='1':
        mastchoice2=input("Which service would you like to edit?\n1)Restaurant")#Add other services here
        print("LOLZ finish this part man")
        #START HERE
        #fileWrite(mastchoice2)
    #elif mastchoice1=='2':
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

while True:
    loginno=input("Welcome to Bustle!\n1.Login\n2.Register\n") #Starts Execution here
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
    else:
        print("Invalid Input")
        time.sleep(3)
        clear()
home()
