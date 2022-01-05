import pickle #To write in dictionary
import os #Using to clear screen using defined clear() function
import time #Slow down execution using sleep()
accounts={'Master':'mpass'}
restlist=[]
clear = lambda: os.system('cls')
def fileWrite(filename,data):#Universal function to write to any mentioned file
    with open(filename,'wb') as file:
        pickle.dump(data,file)
def register(): #Adds new user account
    usn=input("Enter a username:\n")
    usn=usn.strip()
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
    mastchoice1=input("What would you like to do?\n1)Add provider\n2)Delete provider")
    mastchoice2=input("Which service would you like to edit?\n1)Restaurant")
    if mastchoice1==1:
        #START HERE
        fileWrite(mastchoice2,)
    #elif mastchoice1==2:
        
def login(): #Checks and logs in user
    n=5
    with open('UserAcc','rb') as file:
            accounts=pickle.load(file)
    for key in accounts:
        print(key)
    usnchoice=input("Select an account\n")
    if usnchoice=="Master":
        loginpass=input("Enter your password\n")
        if loginpass==accounts[usnchoice]:
            master()
    elif usnchoice in accounts:
        while n>=0:
            loginpass=input("Enter your password\n")
            if loginpass==accounts[usnchoice]:
                clear()
                print("Welcome ",usnchoice,"!\nLoading");time.sleep(0.5);clear()
                print("Welcome ",usnchoice,"!\nLoading.");time.sleep(0.5);clear()
                print("Welcome ",usnchoice,"!\nLoading..");time.sleep(0.5);clear()
                print("Welcome ",usnchoice,"!\nLoading...");time.sleep(0.5);clear()
                return True
            else:
                n=n-1
                if n!=0:
                    print("Incorrect Password. Try again!\nYou have ",n," tries remaining:")
                else:
                    print("Too many failed attempts. You will now be redirected to the login page")
                    return  False
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
        with open('UserAcc','rb') as file:
            print(pickle.load(file))
    elif loginno=='forceclear': #Dev Command
        accounts={'Master':'mpass'}
        with open('UserAcc','wb') as file:
         pickle.dump(accounts,file)
    else:
        print("Invalid Input")
        time.sleep(3)
        clear()
home()