from PIL import Image  #For displaying images in the terminal itself
import pyqrcode #For generating QR code's in python
from pyqrcode import QRCode #QR code module
import pickle #To write in dictionary
import os#Using to clear screen using defined clear() function
import time #Slow down execution using sleep()
import stdiomask #used to accept password without showing characters
from tabulate import tabulate#Used to display a table
from copy import deepcopy#Used to create new voucher values with different references
import re #Used to evaluate regex
import pdb
clear = lambda: os.system('cls|clear')#Lambda function to clear the screen
user = ''#Global variable to record currently logged in user
def fileWrite(filename,data):#Universal function to write to any mentioned file
    with open(filename,'wb') as file:
        pickle.dump(data,file)
def fileRead(filename):#Universal function to read any mentioned file
    with open(filename,'rb') as file:
         data=pickle.load(file)
         return data
def logout():#Function to display logout screen
    clear()
    print("Logging out");time.sleep(0.5);clear()
    print("Logging out.");time.sleep(0.5);clear()
    print("Logging out..");time.sleep(0.5);clear()
    print("Logging out...");time.sleep(0.5);clear()
    login()
def setpass(usnID,score):#Function to set the password and security question
    accounts=fileRead("bustle_files/UserAcc")
    pass1=input("Enter a password:\n")
    pass1=pass1.strip()
    while True:
        pass2=input("Confirm password:\n")
        if pass2==pass1:
            while True:
                sq=input("Enter your Security Question(Minimum of 5 characters ending with a '?'):\n")
                if len(sq) >= 6 and sq.endswith('?'):
                    sa=input("Enter the answer for your Security Question:\nWARNING: Give an answer you can remember. You will need these in case you have to reset your account password!\n")
                    accounts.update({usnID:[pass1,score,sq,sa]})
                    fileWrite('bustle_files/UserAcc',accounts)
                    return 
                else:
                    print("Enter a valid security question!(Min 5 characters ending with a '?')")
                    time.sleep(3)
                    clear()
                    continue
        else:
            print("Oops password doesn't match! Try again:")
def register(): #Function to add new user account  
    while True:
        usn=input("Enter a username(Minimum of 5 characters without special characters):\n")    
        usn=usn.strip()
        if len(usn) >= 5 and usn.isalnum():
            usn=usn+'e'
            break
        else:
            print("Enter a valid username!(Min 5 characters without special characters)")
            time.sleep(3)
            clear()
    accounts=fileRead("bustle_files/UserAcc")
    if usn in accounts:
        print("Account already exists!")
    else:
        setpass(usn,1000)
        vdata=fileRead("bustle_files/vouchers")
        vdatacopy=deepcopy(vdata["admine"])
        del vdatacopy[4]
        vdata.update({usn:vdatacopy})
        fileWrite("bustle_files/vouchers",vdata)
        print('User account successfully created! You will now be redirected to the login page')
def voucher():#Function to display and purchase vouchers
    vfile=fileRead("bustle_files/vouchers")
    accounts=fileRead("bustle_files/UserAcc")
    global user
    clear()
    print("\t\t\t\tVouchers!")
    print(f"\nUser:{user}\n")
    print(f"Score:{accounts[user+'e'][1]}\n")
    data =list(zip(vfile[user+'e'][0],vfile[user+'e'][1],vfile[user+'e'][2],vfile[user+'e'][3]))
    print(tabulate(data, headers=["V.Code","Description","Bustle Points","Purchased"], tablefmt = "fancy_grid"))
    vchoice=input("Which voucher would you like to purchase?\n")
    if vchoice in vfile[user+'e'][0]:
        vquantity=int(input("How many would you like to buy?\n"))
        i=vfile["admine"][0].index(vchoice)
        if int(accounts[user+'e'][1])>=(int(vfile[user+'e'][2][i])*vquantity):
            print(f"{vquantity} Vouchers Added!")
            vfile[user+'e'][3][i]=int(vfile[user+'e'][3][i])+vquantity
            accounts[user+'e'][1]=int(accounts[user+'e'][1])-(int(vfile[user+'e'][2][i])*vquantity)
            fileWrite("bustle_files/vouchers",vfile)
            fileWrite("bustle_files/UserAcc",accounts)
            time.sleep(2)
        elif int(accounts[user+'e'][1])<(int(vfile[user+'e'][2][i])*vquantity):
            ynchoice=input("Insufficient Bustle Points!\nWould you like to play some games to get more Bustle Points?(y/n)\n")
            if ynchoice=='y':
                clear()
                games()
            else:
                clear()
                home()
    elif vchoice=='c':
        clear()
        home()
    else:
        print("Invalid input. Reinitializing page...")
        time.sleep(2)
        clear()
        voucher()
    home()
def vouchdisc(price):
    global user
    price=int(price)
    ynchoice=input("Would you like to see the list of available vouchers?(y/n)\n")
    if ynchoice=='y' and price>100:
        vfile=fileRead("bustle_files/vouchers")
        vcodes=[]
        vdesc=[]
        vnum=[]
        for n in vfile[user+'e'][3]:
            if n>0:
                i=vfile[user+'e'][3].index(n)
                vcodes.append(vfile[user+'e'][0][i])
                vdesc.append(vfile[user+'e'][1][i])
                vnum.append(vfile[user+'e'][3][i])
        while True:
            print(f"Bill Amount:{price}")
            data =list(zip(vcodes,vdesc,vnum))
            print(tabulate(data, headers=["V.Code","Description","Available"], tablefmt = "fancy_grid"))
            vchoice=input("Which Voucher would you like to apply?\n")
            if vchoice in vcodes:
                i=vfile[user+'e'][0].index(vchoice)
                vfile[user+'e'][3][i]=int(vfile[user+'e'][3][i])-1
                discexp=vfile["admine"][4][i]
                if eval(discexp)>=100:
                    price=eval(discexp)
                    return price 
                else:
                    print("This voucher cannot be applied on the current transaction!")
                    time.sleep(2)
                    clear()
                    return 0
            elif vchoice=='c':
                return 0
            else:
                print("Invalid Input, Reinitializing page...")
                time.sleep(2)
                clear()
    elif ynchoice=='y' and price<=100:
        print("Voucher cannot be applied on the current transaction!")
        return -1
    elif ynchoice=='n':
        return -1
    else:
        print("Invalid input, reinitializing...")
        time.sleep(2)
        clear()
        return 0
def load():#Function to display loading screen
    print("Loading");time.sleep(0.5);clear()
    print("Loading.");time.sleep(0.5);clear()
    print("Loading..");time.sleep(0.5);clear()
    print("Loading...");time.sleep(0.5);clear()
def CardVerify(cnumber,ctype,ccomp):#Funcion to verfiy Card Number
    if ctype=='1':
        if ccomp=='1':
            pattern="^5[1-5][0-9]{14}|^(222[1-9]|22[3-9]\\d|2[3-6]\\d{2}|27[0-1]\\d|2720)[0-9]{12}$"
        elif ccomp=='2':
            pattern="^4[0-9]{12}(?:[0-9]{3})?$"
    elif ctype=='2':
        if ccomp=='1':
            pattern="^5[1-5][0-9]{14}|^(222[1-9]|22[3-9]\\d|2[3-6]\\d{2}|27[0-1]\\d|2720)[0-9]{12}$"
        elif ccomp=='2':
            pattern="^4[0-9]{12}(?:[0-9]{3})?$"
    elif ctype == 'c':
        clear()
        load()
        Booking()
    p=re.compile(pattern)
    if(re.search(p,cnumber)):
        return True
    else:
        return False
def settings():#Funtion for settings page
    clear()
    global user
    accounts=fileRead("bustle_files/UserAcc")
    book= fileRead("bustle_files/bookings")
    vouch=fileRead("bustle_files/vouchers")
    setchoice=input("Settings:\n1)Clear Booking History\n2)Change Username\n3)Change Password\n4)Delete Profile\n5)About us\n6)Back\n")
    if setchoice=='1':
        while True:
            ynchoice=input("Do you want to clear your Booking History?(y/n)\n")
            if ynchoice=='y':
                clear()
                print("Booking History Cleared!")
                del book[user]
                book.update({user:([],[],[],[])})
                fileWrite("bustle_files/bookings",book)
                time.sleep(2)
                settings()
            elif ynchoice=='n':
                print("Operation cancelled. Redirecting...")
                time.sleep(2)
                settings()
            else:
                print("Invalid Input, Reinitializing page...")
                time.sleep(2)
                clear()
    elif setchoice=='2':
        ynchoice=input("Do you want to change your Username?(y/n)\n")
        if ynchoice=='y':
            clear()
            newUSN=input("Enter the new username\n")
            accounts[newUSN+'e']=accounts[user+'e']
            book[newUSN]=book[user]
            vouch[newUSN+'e']=vouch[user+"e"]
            del accounts[user+'e']
            del vouch[user+'e']
            del book[user]
            fileWrite("bustle_files/UserAcc",accounts)
            fileWrite("bustle_files/vouchers",vouch)
            fileWrite("bustle_files/bookings",book)
            print("Username changed! You will now be taken back to the settings page...")
            user=newUSN
            time.sleep(2)
            settings()
        elif ynchoice=='n':
            print("Operation cancelled. Redirecting...")
            time.sleep(2)
            settings()
        else:
            print("Invalid Input, Reinitializing page...")
            time.sleep(2)
            clear()
    elif setchoice=='3':
        ynchoice=input("Do you want to change your Password?(y/n)\n")
        if ynchoice=='y':
            clear()
            while True:
                newPass=input("Confirm Current Password\n")
                if newPass==accounts[user+'e'][0]:
                    newPass=input("Enter the new password:\n")
                    if newPass==input("Confirm the password:\n"):
                        accounts[user+'e'][0]=newPass
                        fileWrite("bustle_files/UserAcc",accounts)
                        print("Password changed successfully! You will be redirected to the settings page\n")
                        time.sleep(2)
                        clear()
                        settings()
                    else:
                        print("The passwords do not match! Try setting the password again.")
                        time.sleep(2)
                        clear()
                elif newPass=='c':
                    clear()
                    settings()
                else:
                    print("Incorrect Password! Try Again")
                    time.sleep(3)
                    clear()
        elif ynchoice=='n':
            print("Operation cancelled. Redirecting...")
            time.sleep(2)
            settings()
        else:
            print("Invalid Input. Reinitializing page...")
            time.sleep(2)
            settings()
    elif setchoice=='4':
        ynchoice=input("Are you sure you want to delete your profile?(y/n)\n")
        if ynchoice=='y':
            del accounts[user+'e']
            del book[user]
            del vouch[user+'e']
            fileWrite("bustle_files/UserAcc",accounts)
            fileWrite("bustle_files/bookings",book)
            fileWrite("bustle_files/vouchers",vouch)
            print("User Deleted! Hope to see you again!\n")
            time.sleep(2)
            clear()
            menu()
    elif setchoice=='5':
        clear()
        print("Team bustle is a group of persistant, hard working and perfectionist coders.")
        print("Project Bustle, our very first project, is an intuitive slot booking and management software that ensures your time and efforts saved")
        print("Members: Harsh Somvanshi, Harini Anand and Bhaskarla Sri Saahith")
        time.sleep(4)
        settings()
    elif setchoice=='6':
        clear()
        home()
    else:
        print("Invalid Input. Reinitializing page...")
        time.sleep(2)
        settings()
def admin():#Function to allow admin to manage the program
    adminpass=fileRead("bustle_files/UserAcc")
    adminpass=adminpass["admine"]
    clear()
    mastchoice1=input("What would you like to do?\n1)Add provider\n2)Delete provider\n3)Manage Vouchers\n4)Manage User Accounts\n5)Logout\n")
    if mastchoice1=='1':
        mastchoice2=input("Choose a category to add to: \n1)Restaurant\n2)Hotel\n3)Spa\n4)Bicycle Repair\n5)Back\n")#Add other services here
        if mastchoice2=='1' or mastchoice2=='2':
            if mastchoice2=='1':
                tempname="restaurant"
                try:
                    service=fileRead(f"bustle_files/restaurants/{tempname}")
                except:
                    fileWrite(f"bustle_files/restaurants/{tempname}",{})
                    service=fileRead(f"bustle_files/restaurants/{tempname}")
            elif mastchoice2=='2':
                tempname="hotel"
                try:
                    service=fileRead(f"bustle_files/hotels/{tempname}")
                except:
                    fileWrite(f"bustle_files/hotels/{tempname}",{})
                    service=fileRead(f"bustle_files/hotels/{tempname}")
            '''elif mastchoice2=='3':
                tempname="bus"
                try:
                    service=fileRead(f"bustle_files/buss/{tempname}")
                except:
                    fileWrite(f"bustle_files/buss/{tempname}",{})
                    service=fileRead(f"bustle_files/buss/{tempname}")'''
            while True:
                try:
                    npname,npseat,npprice=input("Enter Name/Available Slots/Price\n").split('/')
                except:
                    print("Incorrect number of inputs received")
                    time.sleep(3)
                    clear()
                    admin()
                if npname in service:
                    print("Entry already exists!")
                    time.sleep(3)
                else:
                    service.update({npname:[npseat,npprice]})
                    break
            fileWrite(f"bustle_files/{tempname+'s'}/{tempname}",service)   
            clear()
            print("Provider successfully added!")
            time.sleep(3)
            admin()
        elif mastchoice2=='3' or mastchoice2=='4':
            if mastchoice2=='3':
                tempname="spa"
                try:
                    service=fileRead(f"bustle_files/spas/{tempname}")
                except:
                    fileWrite(f"bustle_files/spas/{tempname}",{})
                    service=fileRead(f"bustle_files/spas/{tempname}")
            elif mastchoice2=='4':
                tempname="cycle"
                try:
                    service=fileRead(f"bustle_files/cycles/{tempname}")
                except:
                    fileWrite(f"bustle_files/cycles/{tempname}",{})
                    service=fileRead(f"bustle_files/cycles/{tempname}")
            while True:
                try:
                    if mastchoice2=='4':
                        nptype='cycle'
                        npname,npexp,npprice=input("Enter Name/Experience/Price\n").split('/')
                    else:
                        npname,nptype,npexp,npprice=input("Enter Name/Expertise/Experience/Price\n").split('/')
                except:
                    print("Incorrect number of inputs received")
                    time.sleep(3)
                    clear()
                    admin()
                if npname in service:
                    ynchoice=input("Entry already exists! Do you want to add another provider?(y/n)\n")
                    if ynchoice=='n':
                        admin()
                else:
                    service.update({npname:[npexp,nptype,npprice]})
                    break
            fileWrite(f"bustle_files/{tempname+'s'}/{tempname}",service)
            clear()
            print("Provider successfully added!")
            time.sleep(3)
            admin()
        elif mastchoice2=='5':
            clear()
            admin()
        else:
            print("Invalid input! Reinitializing page...")
            time.sleep(3)
            clear()
            admin()
    elif mastchoice1=='2':
        while True:
            mastchoice2=input("Choose a category to delete from:\n1)Restaurant\n2)Hotel\n3)Spa\n4)Bicycle Repair\n5)Back\n")#Add other services here
            if mastchoice2=='1':
                tempname="restaurant"
            elif mastchoice2=='2':
                tempname="hotel"
            #elif mastchoice2=='3':
                #tempname="bus"
            elif mastchoice2=='3':
                tempname="spa"
            elif mastchoice2=='4':
                tempname="cycle"
            elif mastchoice2=='5':
                admin()
            else:
                print("Invalid input! Reinitializing page..")
                time.sleep(2)
                clear()
                continue
            try:
                service=fileRead(f"bustle_files/{tempname+'s'}/{tempname}")
                if service:
                    for key in service:
                     print(key)
                else:
                    ynchoice=input("No providers available for this category yet. Would you like to add a provider instead?(y/n)\n")
                    if ynchoice=='y':
                        clear()
                        admin()
                    elif ynchoice=='n':
                        continue
            except:
                ynchoice=input("No entries in this category available! Do you want to browse another category instead?(y/n)\n")
                if ynchoice=='n':
                    admin()
                elif ynchoice=='y':#check if really necessary
                    continue
            dpname=input("Which provider would you like to delete?\n")
            if dpname in service:
                loginpass=stdiomask.getpass("Enter admin password to confirm:\n")
                if loginpass==adminpass:
                    del service[dpname]
                    fileWrite(f"bustle_files/{tempname+'s'}/{tempname}",service)
                    print("Provider Deleted!\n")
                else:
                    print("Incorrect password. Provider deleletion failed")
                time.sleep(3)
                clear()
            else:
                print("Provider doesn't exist! Provider deleletion failed")
                time.sleep(3)
                clear()
    elif mastchoice1=='3':
        vfile=fileRead("bustle_files/vouchers")
        vchoice=input("What would you like to do?\n1)Add Voucher\n2)Delete voucher\n")
        if vchoice=='1':
            while True:
                try:
                    vcode,vdesc,vscore=input("Enter Voucher Code/Voucher Description/Cost\n").split('/')
                    vcalc=input("Enter the mathematical expression on \"price\"\n")
                    break
                except:
                    print("Invalid Input! Reinitializing page")
                    time.sleep(3)
                    clear()
            for user in fileRead("bustle_files/UserAcc"):
                if user in vfile:
                    vfile[user][0].append(vcode)#list of all voucher codes
                    vfile[user][1].append(vdesc)#list of all voucher descriptions
                    vfile[user][2].append(vscore)#list of all costs
                    vfile[user][3].append(0)#quantity of vouchers present
                    vfile.update({user:vfile[user]})
            vfile["admine"][4].append(vcalc)#list of all the mathematical operations for vouchers
            fileWrite("bustle_files/vouchers",vfile)
            clear()
            print("Voucher Added!")
            time.sleep(3)
            admin()
        elif vchoice=='2':
            vfile=fileRead("bustle_files/vouchers")
            while True:
                if len(vfile["admine"][0])!=0:
                    print("Which voucher would you like to delete?")
                    print(vfile["admine"][0])
                    vcode=input()
                    if vcode in vfile["admine"][0]:
                        i=vfile["admine"][0].index(vcode)
                        for user in vfile:
                            del vfile[user][0][i]
                            del vfile[user][1][i]
                            del vfile[user][2][i]
                            del vfile[user][3][i]
                            vfile.update({user:vfile[user]})
                            fileWrite("bustle_files/vouchers",vfile)
                        clear()
                        print("Voucher Deleted!")
                        time.sleep(3)
                        admin()
                    else:
                        print("Invalid input! Reinitializing page...")
                        time.sleep(2)
                        clear()
                        continue
                else:
                    print("No vouchers found!")
                    time.sleep(3)
                    clear()
                    admin()
        elif vchoice=='c':
            clear()
            admin()
        else:
            print("Invalid Input!")
            time.sleep(3)
            clear()
            admin()
    elif mastchoice1=='4':
        mchoice=input("What would you like to do?\n1)Enable/Disable user\n2)Delete a user\n")
        accounts = fileRead("bustle_files/UserAcc")
        if mchoice=='1':
            print("Which account do you wish to manage?")
            for key in accounts:
                if key != "admine":
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
                admin()
            fileWrite("bustle_files/UserAcc",accounts)
        elif mchoice=='2':
            for key in accounts:
                if key != "admine":
                    print(key)  
            usnchoice=input("Which user would you like to delete\n")
            while True:
                if usnchoice in accounts:
                    del accounts[usnchoice]
                    vfile=fileRead("bustle_files/vouchers")
                    del vfile[usnchoice]
                    fileWrite("bustle_files/UserAcc",accounts)
                    fileWrite("bustle_files/vouchers",vfile)
                    print("User deleted!")
                    time.sleep(2)
                    clear()
                    admin()
                elif usnchoice=='c':
                    clear()
                    break
                else:
                    print("Invalid Input! Reinitializing...")
                    clear()
        elif mchoice=='c':
            clear()
            admin()
        else:
            print("Invalid Input! Reinitializing...")
            clear()
            admin()
    elif mastchoice1=='5':
        logout()
    else:
        print("Invalid Input! Reinitializing page...")
        time.sleep(3)
        admin()
def games():#Function to display and launch games
    global user
    accounts=fileRead("bustle_files/UserAcc")
    print("Which game would you like to play?\n")
    gchoice=input("1)Snake!\n2)Bustle Tetris\n3)Impossible Tic-Tac-Toe!\n4)Sudoku\n5)Trivia!\n6)Points Distribution\n7)Back\n")
    if gchoice =='1':
        exec(open("game_files/snake.py").read())
        with open("tempscore","r") as file:
            score=int(file.read())
        os.remove("tempscore")
        if score>10:
            accounts[user+'e'][1]+=int((score-10)/2)
        fileWrite("bustle_files/UserAcc",accounts)
        time.sleep(2)
    elif gchoice =='2':
        exec(open("game_files/TETRIS_FINAL.py").read())
        clear()
        with open("tempscore","r") as file:
            score=int(file.read())
        os.remove("tempscore")
        score=score/10
        accounts[user+'e'][1]+=int(score)
        fileWrite("bustle_files/UserAcc",accounts)
        print(f"Your Final Score was: {score}")
        time.sleep(2)
    elif gchoice =='3':
        exec(open("game_files/tictactoe/TictacToe.py").read())
    elif gchoice=='4':
        exec(open("game_files/sudoku/GUI.py").read())
        with open("tempscore","r") as file:
            if not file.read() == "None":
                score=int(file.read())
            else:
                score=0
        os.remove("tempscore")
        accounts[user+'e'][1]+=int(score)
        fileWrite("bustle_files/UserAcc",accounts)
        print(f"Your Final Score was: {score}")
        time.sleep(2)
    elif gchoice=='5':
        exec(open("game_files/trivia/BUSTLEQUIZ.py").read())
        clear()
        with open("tempscore","r") as file:
            score=int(file.read())
        os.remove("tempscore")
        accounts[user+'e'][1]+=int(score)
        fileWrite("bustle_files/UserAcc",accounts)
        print(f"Your Final Score was: {score}")
        time.sleep(2)
    elif gchoice=='6':
        clear()
        data =list(zip(["Snake!","Bustle Tetris","Impossible Tic-Tac-Toe!","Sudoku","Trivia!"],["0.5 Bustle Points for every Game point after 10","1 Bustle point for every row cleared","100 Bustle points for winning against computer","10 Bustle points for clearing boaard","1 Bustle point for every correct answer"]))
        print(tabulate(data, headers=["Game","Points Awarded"], tablefmt = "fancy_grid"))
        input("\nPress any key to go back")
    elif gchoice=='7':
        home()
    else:
        print("Invalid Input. Reinitializing page...")
        time.sleep(2)
        clear()
        games()
    home()
def login(): #Checks and logs in user
    clear()
    n=5
    accounts=fileRead("bustle_files/UserAcc")
    bool=True
    for key in accounts:
        if key[-1]=='e':
            print(key[0:-1])
        elif key[-1]=='d':
            print(key[0:-1],"(disabled)")
    usnchoice=input("Select an account (Enter 'c' to go back)\n")
    for key in accounts:
        if key.startswith(usnchoice) and key[-1]=='e':
            usnchoice = usnchoice + key[-1]
            bool=True
        elif key.startswith(usnchoice) and key[-1]=='d':
            usnchoice = usnchoice + key[-1]
            bool=False
    if usnchoice=="admine":
        loginpass=stdiomask.getpass("Enter your password\n")
        if loginpass==accounts[usnchoice]:
            admin()
        else:
            if n!=0:
                print("Incorrect Password.\nTry again!\nYou have ",n," tries remaining:\n")
            else:
                print("Too many failed attempts. You will now be redirected to the login page")
                accounts[usnchoice[0:-1]+'d']=accounts[usnchoice]
                del accounts[usnchoice]
                fileWrite('bustle_files/UserAcc',accounts)
                return  False    
    elif usnchoice in accounts and bool==True:
        while n>=0:
            loginpass=stdiomask.getpass("Enter your password\n")
            if loginpass==accounts[usnchoice][0]:
                clear()
                global user 
                print("Welcome ",usnchoice[0:-1],"!\nLoading");time.sleep(0.5);clear()
                print("Welcome ",usnchoice[0:-1],"!\nLoading.");time.sleep(0.5);clear()
                print("Welcome ",usnchoice[0:-1],"!\nLoading..");time.sleep(0.5);clear()
                print("Welcome ",usnchoice[0:-1],"!\nLoading...");time.sleep(0.5);clear()
                user = usnchoice[0:-1]
                home()
            elif loginpass=='F':
                fpans=input(accounts[usnchoice][2])
                if fpans== accounts[usnchoice][3]:
                    print("Enter New Password(Make sure to remember this one!)\nNote:You will be required to enter new Security credentials\n")
                    score=accounts[usnchoice][1]
                    setpass(usnchoice,score)
                    login()
            else:
                n=n-1   
                if n!=0:
                    print("Incorrect Password.\nForgot Password? Press F (to pay respects)\nTry again!\nYou have ",n," tries remaining:")
                else:
                    print("Too many failed attempts. You will now be redirected to the login page")
                    accounts[usnchoice[0:-1]+'d']=accounts[usnchoice]
                    del accounts[usnchoice]
                    fileWrite('bustle_files/UserAcc',accounts)
                    return  False   
    elif usnchoice in accounts and bool==False:
        print("This account is disabled. Kindly contact the admin to re-enable your account")
        return False
    elif usnchoice=='c':
        clear()
        menu()
    else:
        clear()
        print("This user doesn't exist!")
        time.sleep(3)
        login()
def home():#Home page
    clear()
    homechoice=input("What would you like to do today?\n1)Make a Booking\n2)Booking History\n3)Vouchers\n4)Games\n5)Settings\n6)Logout\n")
    if homechoice=='1':
        clear()
        load()
        Booking()
    elif homechoice=='2':
        clear()
        load()
        BookingHist(None,None,None,None)
    elif homechoice=='3':
        clear()
        voucher()
    elif homechoice=='4':
        clear()
        games()
    elif homechoice=='5':
        clear()
        settings()
    elif homechoice=='6':
        logout()
    else:
        print("Invalid Input")
        time.sleep(2)
        home()
def menu():#Starting page of the program
    try: 
        fileRead("bustle_files/UserAcc")
        fileRead("bustle_files/vouchers")
    except:
        fileWrite("bustle_files/UserAcc",{'admine':'mpass'})
        fileWrite("bustle_files/vouchers",{"admine":[[],[],[],[],[]]})
    while True:
        loginno=input("Welcome to Bustle!\n1.Login\n2.Register\n")
        if loginno=='1':
            login()
        elif loginno=='2':
            register()
            time.sleep(3)
            clear()
        elif loginno=='disp': #Dev Command
            accounts=fileRead('bustle_files/UserAcc')
            print(accounts)
        elif loginno=='fclr': #Dev Command
            os.remove("bustle_files/UserAcc")
            fileWrite("bustle_files/UserAcc",{'admine':'mpass'})
        elif loginno=='m':#TEMPORARY
            admin()
        elif loginno=='vdisp':
            print(fileRead("bustle_files/vouchers"))
        else:
            print("Invalid Input")
            time.sleep(3)
            clear()
def Booking(): #Bookings page
    bchoice = input("Which service would you like to book?\n1)Restaurant\n2)Hotel\n3)Cycle Repair\n4)Spa\n5)Back\n")
    if bchoice == '1':
        Restaurant()
    elif bchoice == '2':
        Hotel()
    elif bchoice == '3':
        Cycle_Repair()
    elif bchoice == '4':
        SPA()
    elif bchoice == '5':
        clear()
        home()
    else:
        print("Invalid Input!")
        time.sleep(3)
        clear()
        Booking()
def Restaurant(): #Choosing Restaurants
    from datetime import datetime
    try:
        fileRead("bustle_files/restaurants/restaurant")
    except:
        clear()
        print("Error 404: Page not found")
        time.sleep(3)
        Booking()
    name = "Restaurant"
    clear()
    slots = fileRead("bustle_files/restaurants/restaurant")
    print("Which restaurant would you like to book a table in?")
    for key in slots:
        print(key)
    print("(Press 'c' to go back)")
    rchoice = input()
    if rchoice in slots:
        try:
            fileRead(f"bustle_files/restaurants/{rchoice}")
        except:
            fileWrite(f"bustle_files/restaurants/{rchoice}", {"10:00-12:00":[slots[rchoice][0],slots[rchoice][1]],"12:00-2:00":[slots[rchoice][0],slots[rchoice][1]],"2:00-4:00":[slots[rchoice][0],slots[rchoice][1]],"4:00-6:00":[slots[rchoice][0],slots[rchoice][1]],"6:00-8:00":[slots[rchoice][0],slots[rchoice][1]],"8:00-10:00":[slots[rchoice][0],slots[rchoice][1]]})
        booking = fileRead(f"bustle_files/restaurants/{rchoice}")
        print("\nNo. of seats per table: 4")
        print(f"Price per table: {slots[rchoice][1]}")
        while True:
            print("\nWhich Time slot would you like to book?")
            i = 1
            for key in booking:
                print(f"{i}) {key}")
                i += 1
            print("(Press 'c' to go back)")
            tchoice = input()
            if tchoice == '1':
                tname = "10:00-12:00"
            elif tchoice == '2':
                tname = "12:00-2:00"
            elif tchoice == '3':
                tname = "2:00-4:00"
            elif tchoice == '4':
                tname = "4:00-6:00"
            elif tchoice == '5':
                tname = "6:00-8:00"
            elif tchoice == '6':
                tname = "8:00-10:00"
            elif tchoice == 'c':
                clear()
                Restaurant()
            else:
                print("Invalid Input!")
                tname = ""
            if tname in booking:
                avail = int(booking[tname][0])
                clear()
                print(f"No. of tables available in time slot {tname}: {avail}")
                nchoice = input("\nHow many persons would you like to book for?\n")
                if nchoice.isdigit():   
                    if int(nchoice) > 4 and int(nchoice)%4 != 0:
                        no = 1 + (int(nchoice)//4)
                    elif int(nchoice)%4 == 0:
                         no = int(nchoice)//4
                    else:
                            no = 1
                    if (avail - no) >= 0:
                        price = int(booking[tname][1])*no
                        print("No. of tables:",no)
                        print("Total price:",price)
                        ychoice = input("Would you like to proceed to checkout(y/n)?\n")
                        if ychoice == 'y':
                            clear()
                            load()
                            n=0
                            while True:
                                print("Restaurant name:",rchoice)
                                print("Time slot:",tname)
                                print("No of persons:",nchoice)
                                print("Total price:",price)
                                print(f"{n} vouchers applied!")
                                check=vouchdisc(price)
                                if check==-1:
                                    break
                                elif check==0:
                                    continue
                                else:
                                    price=check
                                    n+=1
                            pchoice = input("\nDo you wish to continue?(y/n)\n")
                            if pchoice == 'y':
                                if checkout():
                                    print("Payment successful")
                                    avail = avail - no
                                    booking.update({tname:[avail,booking[tname][1]]})
                                    fileWrite(f"bustle_files/restaurants/{rchoice}",booking)
                                    now = datetime.now()
                                    time.sleep(3)
                                    clear()
                                    BookingHist(rchoice,name,price,now)
                                else:
                                    print("Payment Failed!")
                                    Restaurant()
                            elif pchoice == 'n':
                                clear()
                            break
                        elif ychoice == 'n':
                            clear()
                    else:
                        print(f"\nSorry! {no} table(s) unavailable in time slot {tname}")
                        time.sleep(3)
                        clear()
                elif nchoice == 'c':
                    clear()
                else:
                    print("invalid input!")
                    time.sleep(3)
                    clear()
            else:
                print("Invalid time slot!")
                time.sleep(3)
                clear()
    elif rchoice == 'c':
        clear()
        Booking()
    else:
        print("Please give a valid restaurant name")
        time.sleep(3)
        clear()
        Restaurant()
def Hotel():#Funtion to book hotels
    from datetime import datetime
    try:
        fileRead("bustle_files/hotels/hotel")
    except:
        clear()
        print("Error 404: Page not found")
        time.sleep(3)
        Booking()
    name = 'Hotel'
    clear()
    slots = fileRead("bustle_files/hotels/hotel")
    print("Which hotel would you like to book a room in?")
    for key in slots:
        print(key)
    print("(Press 'c' to go back)")
    hchoice = input()
    if hchoice in slots:
        clear()
        try:
            fileRead(f"bustle_files/hotels/{hchoice}")
        except:
            fileWrite(f"bustle_files/hotels/{hchoice}",[slots[hchoice][0],slots[hchoice][1]])
        booking = fileRead(f"bustle_files/hotels/{hchoice}")
        while True:
            print("(Note: Check-in time: 10:00 am and Check-out time: 12:00 pm for all bookings)")
            print(f"Number of rooms available: {booking[0]}")
            print(f"Price per room: {booking[1]}")
            bchoice = input(f"Would you like to book in {hchoice}?(y/n): ")
            avail = int(booking[0])
            if bchoice == 'y':
                while True:
                    nchoice = input("How many rooms would you like to book?\n(Press 'c' to go back)\n")
                    if nchoice.isdigit():
                        if (avail-int(nchoice)) >= 0:
                            price = int(booking[1])*int(nchoice)
                            clear()
                            print(f"No. of rooms to be booked: {nchoice}")
                            print(f"Total price: {price}")
                            cchoice = input("\nDo you wish to proceed to checkout?(y/n)\n")
                            if cchoice == 'y':
                                clear()
                                load()
                                n=0
                                while True:
                                    print("Hotel name:",hchoice)
                                    print("No.of rooms to be booked:",nchoice)
                                    print("Total price:",price)
                                    print(f"{n} vouchers applied!")
                                    check=vouchdisc(price)
                                    if check==-1:
                                        break
                                    elif check==0:
                                        continue
                                    else:
                                        price=check
                                        n+=1
                                pchoice = input("\nDo you wish to continue?(y/n)\n")
                                if pchoice == 'y':
                                    if checkout():
                                        print("Payment successful")
                                        avail = avail - int(nchoice)
                                        booking[0] = str(avail)
                                        fileWrite(f"bustle_files/hotels/{hchoice}",booking)
                                        time.sleep(3)
                                        now = datetime.now()
                                        clear()
                                        BookingHist(hchoice,name,price,now)
                                    else:
                                        print("Payment Failed!")
                                        Hotel()
                                elif pchoice == 'n':
                                    clear()
                                    Hotel()
                            elif cchoice == 'n':
                                clear()
                                Hotel()
                        else:
                            print(f"\nSorry! {nchoice} room(s) unavailable")
                            time.sleep(3)
                            clear()
                    elif nchoice == 'c':
                        clear()
                        Hotel()
                    else:
                        print("Invalid input!")
                        time.sleep(3)
                        clear()
            elif bchoice == 'n':
                clear()
                Hotel()
            else:
                print("Invalid input!")
                time.sleep(3)
                clear()
    elif hchoice == 'c':
        clear()
        Booking()
    else:
        print("\nPlease give a valid hotel name!")
        time.sleep(3)
        Hotel()
def SPA(): #Function for SPA bookings
    from datetime import datetime
    try:
        fileRead("bustle_files/spas/spa")
    except:
        clear()
        print("Error 404: Page not found")
        time.sleep(3)
        Booking()
    name = 'SPA'
    hist = ''
    clear()
    services = []
    slots = fileRead("bustle_files/spas/spa")
    for key in slots:
        if slots[key][1] not in services:
            services.append(slots[key][1])
    while True:
        print("Which SPA service would you like to book")
        for service in services:
            print(service)
        print("(Press 'c' to go back)")
        schoice = input()
        if schoice in services:
            while True:
                flag = 0
                print("\nList of providers:")
                for key in slots:
                    if slots[key][1] == schoice and key.endswith('a'):
                        print(f"Name: {key[:-1]}, Experience: {slots[key][0]}, Availability = Available")
                    elif slots[key][1] == schoice and key.endswith('b'):
                        print(f"Name: {key[:-1]}, Experience: {slots[key][0]}, Availability = Booked")
                pchoice = input("\nWhich provider would you like to book (Press 'c' to go back)?\n").strip()
                if pchoice == 'c':
                    clear()
                    SPA()
                else:
                    for key in slots:
                        if key[:-1] == pchoice:
                            if key.endswith('a'):
                                avail = True
                                flag = 0
                            elif key.endswith('b'):
                                avail = False
                                flag = 0
                            break
                        else:
                            flag += 1 
                    if flag == 0 and avail == True:
                        while True:
                            try:
                                th,tm = input("Enter time at which you wish for the provider to arrive(hh/mm):\n").split(":")
                            except:
                                print("Invalid time entry!(hh:mm)")
                                time.sleep(3)
                                clear()
                                continue
                            if th.isdigit() and tm.isdigit() and int(th) <= 23 and int(tm) <=59 and int(th) >= 0 and int(tm) >= 0:
                                price = slots[pchoice+'a'][2]
                                clear()
                                print(f"Type of service: {schoice}")
                                print(f"Name of provider: {pchoice}")
                                print(f"Timing: {th}:{tm}")
                                print(f"Price: {price}")
                                ychoice = input("\nDo you wish to proceed to checkout?(y/n):\n")
                                if ychoice == 'y':
                                    clear()
                                    load()
                                    n=0
                                    while True:
                                        print("Type of service:",schoice)
                                        print("Provider name:",pchoice)
                                        print("Total price:",price)
                                        print(f"{n} vouchers applied!")
                                        check=vouchdisc(price)
                                        if check==-1:
                                            break
                                        elif check==0:
                                            continue
                                        else:
                                            price=check
                                            n+=1
                                    cchoice = input("\nDo you wish to continue?(y/n)\n")
                                    if cchoice == 'y':
                                        if checkout():
                                            print("Payment successful")
                                            hist = schoice + "-" + pchoice
                                            slots[pchoice +'b'] = slots[pchoice +'a']
                                            del slots[pchoice + 'a']
                                            fileWrite("bustle_files/spas/spa",slots)
                                            time.sleep(3)
                                            now = datetime.now()
                                            clear()
                                            BookingHist(name,hist,price,now)
                                        else:
                                            print("Payment Failed!")
                                            SPA()
                                    elif cchoice == 'n':
                                        clear()
                                        SPA()
                                if ychoice == 'n':
                                    clear()
                                    SPA()
                            else:
                                print("Invalid time entry!(hh:mm)")
                                time.sleep(3)
                                clear()
                                continue
                    elif flag == 0 and avail == False:
                        print("Provider Unavailable!")
                        time.sleep(3)
                        clear()
                        SPA()
                    else:
                        print("Provider input invalid!")
                        time.sleep(3)
                        clear()
                        continue
        elif schoice == 'c':
            clear()
            Booking()
        else:
            print("Invalid input!")
            time.sleep(3)
            clear()
def Cycle_Repair():
    from datetime import datetime
    try:
        fileRead("bustle_files/cycles/cycle")
    except:
        clear()
        print("Error 404: Page not found")
        time.sleep(3)
        Booking()
    name = 'Cycle Repair'
    clear()
    slots = fileRead("bustle_files/cycles/cycle")
    while True:
        print("List of providers:")
        for key in slots:
            if key.endswith('a'):
                print(f"Name:{key[:-1]}, Experience:{slots[key][0]}, Availability: Available")
            else:
                print(f"Name:{key[:-1]}, Experience:{slots[key][0]}, Availability: Booked")
        pchoice = input("\nWhich provider would you like to book (Press 'c' to go back)?\n").strip()
        flag = 0
        if pchoice == 'c':
            clear()
            Booking()
        else:
            for key in slots:
                if key[:-1] == pchoice:
                    if key.endswith('a'):
                        avail = True
                        flag = 0
                    elif key.endswith('b'):
                        avail = False
                        flag = 0
                    break
                else:
                    flag += 1 
            if flag == 0 and avail == True:
                while True:
                    try:
                        th,tm = input("Enter time at which you wish for the provider to arrive(hh/mm):\n").split(":")
                    except:
                        print("Invalid time entry!(hh:mm)")
                        time.sleep(3)
                        clear()
                        continue
                    if th.isdigit() and tm.isdigit() and int(th) <= 23 and int(tm) <= 59 and int(th) >= 0 and int(tm) >= 0:
                        price = slots[pchoice+'a'][2]
                        clear()
                        print(f"Type of service: Bicycle Repair")
                        print(f"Name of provider: {pchoice}")
                        print(f"Timing: {th}:{tm}")
                        print(f"Price: {price}")
                        ychoice = input("\nDo you wish to proceed to checkout?(y/n):\n")
                        if ychoice == 'y':
                            clear()
                            load()
                            n=0
                            while True:
                                print("Type of service: Bicycle Repair")
                                print("Provider name:",pchoice)
                                print("Total price:",price)
                                print(f"{n} vouchers applied!")
                                check=vouchdisc(price)
                                if check==-1:
                                    break
                                elif check==0:
                                    continue
                                else:
                                    price=check
                                    n+=1
                            cchoice = input("\nDo you wish to continue?(y/n)\n")
                            if cchoice == 'y':
                                if checkout():
                                    print("Payment successful")
                                    slots[pchoice +'b'] = slots[pchoice +'a']
                                    del slots[pchoice + 'a']
                                    fileWrite("bustle_files/cycles/cycle",slots)
                                    time.sleep(3)
                                    now = datetime.now()
                                    clear()
                                    BookingHist(name,pchoice,price,now)
                                else:
                                    print("Payment Failed!")
                                    Cycle_Repair()
                            elif cchoice == 'n':
                                clear()
                                Cycle_Repair()
                        if ychoice == 'n':
                            clear()
                            Cycle_Repair()
                    else:
                        print("Invalid time entry!(hh:mm)")
                        time.sleep(3)
                        clear()
                        continue
            elif flag == 0 and avail == False:
                print("Provider Unavailable!")
                time.sleep(3)
                clear()
                Cycle_Repair()
            else:
                print("Provider input invalid!")
                time.sleep(3)
                clear()
                continue


def checkout(): #Checkout page
    clear()
    load()
    while True:
        #pdb.set_trace()
        pchoice = input("How would you like to make your payment?:\n1.Debit card\n2.Credit card\n3.UPI\n4.Back")
        if pchoice == '1':
            while True:
                cardchoice=input("Which card would you like to use?\n1)Mastercard\n2)Visa\n3)Back\n")
                if cardchoice != '3':
                    clear()
                    dcn = input("Enter Debit Card number:")
                    if CardVerify(dcn,pchoice,cardchoice):
                        dcna = input("Enter Name of card holder:").strip()
                        if dcna.replace(' ','').isalpha(): 
                            try: 
                                expm,expy = input("Enter card expiry date(MM/YY):").split("/")
                            except:
                                print("Enter Expiry date in the form MM/YY")
                                time.sleep(3)
                                clear()
                                continue 
                            if expm.isdigit() and expy.isdigit():
                                cvv = input("Enter cvv:").strip()
                                if cvv.isdigit() and len(cvv) == 3:
                                    return True
                                else:
                                    print("Enter a valid cvv!")
                                    time.sleep(3)
                                    clear() 
                            else:
                                print("Enter valid exp date!")
                                time.sleep(3)
                                clear()
                        else:
                            print("Enter valid Debit card holder name!")
                            time.sleep(3)
                            clear()
                    else:
                        print("Invalid Debit Card number!")
                        time.sleep(3)
                        clear()
                else:
                    clear()
                    checkout()
        elif pchoice == '2':
            while True:
                cardchoice=input("Which card would you like to use?\n1)Mastercard\n2)Visa\n3)Back\n")
                if cardchoice != '3':
                    clear()
                    ccn = input("Enter Credit Card number:")
                    if CardVerify(ccn,pchoice,cardchoice):
                        ccna = input("Enter Name of card holder:")
                        if ccna.replace(' ','').isalpha():
                            try:
                                expm,expy = input("Enter card expiry date:").split("/")
                            except:
                                print("Enter Expiry date in the form MM/YY!")
                                time.sleep(3)
                                clear()
                                continue
                            if expm.isdigit() and expy.isdigit():
                                cvv = input("Enter cvv:")
                                if cvv.isdigit() and len(cvv) == 3:
                                    return True
                                else:
                                    print("Enter a valid cvv!")
                                    time.sleep(3)
                                    clear()
                            else:
                                print("Enter valid exp date!")
                                time.sleep(3)
                                clear()
                        else:
                            print("Enter valid Debit card holder name!")
                            time.sleep(3)
                            clear()
                    else:
                        print("Invalid Credit Card number!")
                        time.sleep(3)
                        clear()
                else:
                    clear()
                    checkout()
        elif pchoice == '3':
            clear()
            print("You have chosen to pay through UPI option")
            print("Below is the QR code which you should scan using the UPI app of your choice")
            s = "The link to the UPI payment"
            url = pyqrcode.create(s)
            url.png("payment.png", scale = 3)
            img = Image.open('payment.png')
            img.show()
            print("You have 50 seconds to scan this QR code for security purpouses")
            time.sleep(5)
            checkout()
        elif pchoice == '4':
            clear()
            load()
            Booking()
        else:
            print("Invalid Input!")
            time.sleep(3)
            clear()
def BookingHist(name, service, price, time1):#Funtion to display the Bookings History page
    global user
    a = {}
    try:
        fileRead("bustle_files/bookings")
    except:
        fileWrite("bustle_files/bookings", a)
    hist = fileRead("bustle_files/bookings") 
    if user not in hist.keys():
        hist[user] = ([],[],[],[])
    x = hist[user][1]
    y = hist[user][0]
    p = hist[user][2]
    z = hist[user][3]
    if name != None and service != None and price != None and time1 != None:
        x.append(name)
        y.append(service)
        p.append(price)
        z.append(time1)
        hist.update({user:(y,x,p,z)})
    fileWrite("bustle_files/bookings",hist)
    print("\t\t\tBooking history")
    print(f"\nUser:{user}\n")
    order = list(zip(x,y,p,z))
    l = ["Service","Name","Amount paid","Time of booking"]
    order.insert(0,l)
    print(tabulate(order, headers = "firstrow", tablefmt = "fancy_grid", showindex = range(1,len(order))))
    bchoice = input("\n(Press 'c' to go back)\n")
    if bchoice == 'c':
        home()
    else:
        print("Invalid input!")
        time.sleep(3)
        clear()
        BookingHist(None,None,None,None)
menu()#Starts Execution here