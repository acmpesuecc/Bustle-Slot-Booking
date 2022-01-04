import pickle #To write in dictionary
import os #Using to clear screen using defined clear() function
import time #Slow down execution using sleep()
accounts={'Master':'mpass'}
clear = lambda: os.system('cls')
def home():#Home page
    print("This is the Home Page")
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
def login(): #Checks and logs in user
    n=5
    for key in accounts:
        print(key)
    usnchoice=input("Select an account\n")
    if usnchoice in accounts:
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