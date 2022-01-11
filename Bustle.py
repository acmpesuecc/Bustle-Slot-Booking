import pickle #To write in dictionary
import os #Using to clear screen using defined clear() function
import time #Slow down execution using sleep()
import stdiomask #used to accept password without showing characters
clear = lambda: os.system('cls')
user = ''
def fileWrite(filename,data):#Universal function to write to any mentioned file
    with open(filename,'wb') as file:
        pickle.dump(data,file)
def fileRead(filename):
    with open(filename,'rb') as file:
         data=pickle.load(file)
         return data
def logout():
    clear()
    print("Logging out");time.sleep(0.5);clear()
    print("Logging out.");time.sleep(0.5);clear()
    print("Logging out..");time.sleep(0.5);clear()
    print("Logging out...");time.sleep(0.5);clear()
    login()
def setpass(usnID,score):
    accounts=fileRead("UserAcc")
    pass1=input("Enter a password:\n")
    pass1=pass1.strip()
    while True:
        pass2=input("Confirm password:\n")
        if pass2==pass1:
            sq=input("Enter your Security Question:\n")
            sa=input("Enter the answer for your Security Question:\nWARNING: Give and answer you can remember. You will need these in case you have to reset your account password!\n")
            accounts.update({usnID:[pass1,score,sq,sa]})
            fileWrite('UserAcc',accounts)
            return 
        else:
            print("Oops password doesn't match! Try again:")
def register(): #Adds new user account  
    usn=input("Enter a username:\n")    
    usn=usn.strip()
    usn=usn+'e'
    accounts=fileRead("UserAcc")
    if usn in accounts:
        print("Account already exists!")
    else:
        setpass(usn,0)
        input()
        print('User account successfully created! You will now be redirected to the login page')
def admin():
    adminpass=fileRead("UserAcc")
    adminpass=adminpass["admine"]
    clear()
    mastchoice1=input("What would you like to do?\n1)Add provider\n2)Delete provider\n3)Manage User Accounts\n4)Logout\n")
    if mastchoice1=='1':
        mastchoice2=input("Choose a category to add to: \n1)Restaurant\n2)Hotel\n3)Bus\n4)Spa\n5)Bicycle Repair\n")#Add other services here
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
                    npname,npseat,npprice=input("Enter Name\Available Slots\Price per table\n").split('\\')
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
            fileWrite(tempname,service)
            clear()
            print("Provider successfully added!")
            time.sleep(3)
            admin()
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
                    admin()
                if npname in service:
                    ynchoice=input("Entry already exists! Do you want to add another provider?(y/n)\n")
                    if ynchoice=='n':
                        admin()
                else:
                    service.update({npname:[npexp,nptype]})
                    break
            fileWrite(tempname,service)
            clear()
            print("Provider successfully added!")
            time.sleep(3)
            admin()
        elif mastchoice2=='6':
            clear()
            admin()
        else:
            print("Invalid input! Reinitializing page...")
            time.sleep(3)
            clear()
            admin()
    elif mastchoice1=='2':
        while True:
            mastchoice2=input("Choose a category to delete from:\n1)Restaurant\n2)Hotel\n3)Bus\n4)Spa\n5)Bicycle Repair\n6)Back\n")#Add other services here
            if mastchoice2=='1':
                tempname="restaurant"
            elif mastchoice2=='2':
                tempname="hotel"
            elif mastchoice2=='3':
                tempname="bus"
            elif mastchoice2=='4':
                tempname="spa"
            elif mastchoice2=='5':
                tempname="cycle"
            elif mastchoice2=='6':
                admin()
            else:
                print("Invalid input! Reinitializing page..")
                time.sleep(2)
                clear()
                continue
            try:
                service=fileRead(tempname)
                if service:
                    for key in service:
                     print(key)
                else:
                    ynchoice=input("No providers available for this category yet. Would you like to add a provder instead?(y/n)\n")
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
            '''if service:  
                for key in service:
                    print(key)
            else:
                ynchoice=("No providers available for this category yet. Would you like to add a provder instead?(y/n)\n")
                if ynchoice=='y':
                    clear()
                    admin() 
                elif ynchoice=='n':
                    continue'''
            dpname=input("Which provider would you like to delete?\n")
            if dpname in service:
                loginpass=stdiomask.getpass("Enter admin password to confirm:\n")
                if loginpass==adminpass:
                    del service[dpname]
                    fileWrite(tempname,service)
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
        accounts = fileRead("UserAcc")
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
        fileWrite("UserAcc",accounts)
    elif mastchoice1=='4':
        logout()
    else:
        print("Invalid Input! Reinitializing page...")
        time.sleep(3)
        admin()
def games():
    print("Which game would you like to play?\n")
    gchoice=input("1)Snake!\n2)Sudoku(Coming Soon...)\n3)#Tic-Tac-Toe#(Coming Soon...)\n4)Back\n")
    if gchoice =='1':
        exec(open("snake.py").read())
    elif gchoice =='2':
        exec(open("").read())
    elif gchoice =='3':
        exec(open("").read())
    elif gchoice=='4':
        home()
    home()
def login(): #Checks and logs in user
    clear()
    n=5
    accounts=fileRead("UserAcc")
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
                fileWrite('UserAcc',accounts)
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
                    fileWrite('UserAcc',accounts)
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
        print("Loading");time.sleep(0.5);clear()
        print("Loading.");time.sleep(0.5);clear()
        print("Loading..");time.sleep(0.5);clear()
        print("Loading...");time.sleep(0.5);clear()
        Booking()
    elif homechoice=='2':
        print("History page here")
    elif homechoice=='3':
        print("Voucher page here")
    elif homechoice=='4':
        games()
    elif homechoice=='5':
        print("Settings page here")
    elif homechoice=='6':
        logout()
    else:
        print("Invalid Input")
        time.sleep(2)
        home()
def menu():
    try: 
        fileRead("UserAcc")
    except:
        fileWrite("UserAcc",{'admine':'mpass'})
    while True:
        loginno=input("Welcome to Bustle!\n1.Login\n2.Register\n")
        if loginno=='1':
            login()
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
            admin()
        else:
            print("Invalid Input")
            time.sleep(3)
            clear()
def Booking(): #Bookings page
    bchoice = input("Which service would you like to book?\n1.Restaurant\n2.Hotel\n3.Bus\n4.Cycle Repair\n5.Spa\n")
    if bchoice == '1':
        Restaurant()
    else:
        clear()
        menu()
def Restaurant(): #Choosing Restaurants
    clear()
    slots = fileRead("restaurant")
    print("Which restaurant would you like to book a table in?")
    for key in slots:
        print(key)
    print("(Press 'c' to go back)")
    rchoice = input()
    if rchoice in slots:
        try:
            fileRead(rchoice)
        except:
            fileWrite(rchoice, {"10:00-12:00":[slots[rchoice][0],slots[rchoice][1]],"12:00-2:00":[slots[rchoice][0],slots[rchoice][1]],"2:00-4:00":[slots[rchoice][0],slots[rchoice][1]],"4:00-6:00":[slots[rchoice][0],slots[rchoice][1]],"6:00-8:00":[slots[rchoice][0],slots[rchoice][1]],"8:00-10:00":[slots[rchoice][0],slots[rchoice][1]]})
        booking = fileRead(rchoice)
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
                print(f"No. of seats available in time slot {tname}: {avail}")
                nchoice = input("\nHow many persons would you like to book for?\n")
                if nchoice.isdigit():   
                    if (avail - int(nchoice)) > 0:
                        if int(nchoice) > 4 and int(nchoice)%4 != 0:
                            no = 1 + (int(nchoice)//4)
                        elif int(nchoice)%4 == 0:
                            no = int(nchoice)//4
                        else:
                            no = 1
                        price = int(booking[tname][1])*no
                        print("No. of tables:",no)
                        print("Total price:",price)
                        ychoice = input("Would you like to proceed to checkout(y/n)?\n")
                        if ychoice == 'y':
                            clear()
                            print("Loading");time.sleep(0.5);clear()
                            print("Loading.");time.sleep(0.5);clear()
                            print("Loading..");time.sleep(0.5);clear()
                            print("Loading...");time.sleep(0.5);clear()
                            print("Restaurant name:",rchoice)
                            print("Time slot:",tname)
                            print("No of persons:",nchoice)
                            print("Total price:",price)
                            pchoice = input("\nDo you wish to continue?(y/n)\n")
                            if pchoice == 'y':
                                if checkout():
                                    print("Payment successful")
                                    avail = avail - no
                                    booking.update({tname:[avail,booking[tname][1]]})
                                    fileWrite(rchoice,booking)
                                    time.sleep(3)
                                    clear()
                                    Bill(rchoice,price)
                                    BookingHist(rchoice)
                                    time.sleep(5)
                                    home()
                                else:
                                    print("Payment Failed!")
                                    Restaurant()
                            elif pchoice == 'n':
                                clear()
                            break
                        elif ychoice == 'n':
                            clear()
                    else:
                        print(f"\nSorry! {nchoice} number of seats unavailable in time slot {tname}")
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
def checkout(): #Checkout page
    clear()
    print("Loading");time.sleep(0.5);clear()
    print("Loading.");time.sleep(0.5);clear()
    print("Loading..");time.sleep(0.5);clear()
    print("Loading...");time.sleep(0.5);clear()
    pchoice = int(input("How would you like to make your payment?:\n1.Debit card\n2.Credit card\n"))
    if pchoice == 1:
        while True:
            dcn = input("Enter Debit Card number:")
            if len(dcn) == 16:
                cvv = input("Enter cvv:")
                return True
            else:
                print("Invalid Debit Card number!")
                time.sleep(3)
                clear()
    elif pchoice == 2:
        while True:
            ccn = input("Enter Credit Card number:")
            if len(ccn) == 16:
                cvv = input("Enter cvv:")
                return True
            else:
                print("Invalid Credit Card number!")
                time.sleep(3)
                clear()
def Bill(name,price): #Rudimentary Bill page
    clear()
    print("\tBill")
    print(name)
    print(f"Total amount: Rs.{price}")
def BookingHist(a):
    global user
    try:
        fileRead("bookings")
    except:
        fileWrite("bookings","")
    hist = dict()
    hist[user] = a
    fileWrite("bookings",hist)
menu()#Starts Execution here