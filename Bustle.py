import pickle #To write in dictionary
import os #Using to clear screen using defined clear() function
import time #Slow down execution using sleep()
import stdiomask #used to accept password without showing characters
from tabulate import tabulate#Used to display a table
clear = lambda: os.system('cls')#Lambda function to clear the screen
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
            sq=input("Enter your Security Question:\n")
            sa=input("Enter the answer for your Security Question:\nWARNING: Give an answer you can remember. You will need these in case you have to reset your account password!\n")
            accounts.update({usnID:[pass1,score,sq,sa]})
            fileWrite('bustle_files/UserAcc',accounts)
            return 
        else:
            print("Oops password doesn't match! Try again:")
def register(): #Function to add new user account  
    usn=input("Enter a username:\n")    
    usn=usn.strip()
    usn=usn+'e'
    accounts=fileRead("bustle_files/UserAcc")
    if usn in accounts:
        print("Account already exists!")
    else:
        setpass(usn,1000)
        vdata=fileRead("bustle_files/vouchers")
        vdata.update({usn:vdata["admine"]})
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
    print(data)
    print(tabulate(data, headers=["V.Code","Description","Bustle Points","Purchased"], tablefmt = "fancy_grid"))
    vchoice=input("Which voucher would you like to purchase?\n")
    if vchoice in vfile[user+'e'][0]:
        vquantity=int(input("How many would you like to buy?\n"))
        i=vfile[user+'e'][0].index(vchoice)
        if int(accounts[user+'e'][1])>=(int(vfile[user+'e'][2][i])*vquantity):
            print(f"{vquantity} Vouchers Added!")
            print(vfile)
            print(accounts)
            input()
            vfile[user+'e'][3][i]=int(vfile[user+'e'][3][i])+vquantity
            accounts[user+'e'][1]=int(accounts[user+'e'][1])-(int(vfile[user+'e'][2][i])*vquantity)
            print(vfile)
            print(accounts)
            input()
            fileWrite("bustle_files/vouchers",vfile)
            fileWrite("bustle_files/UserAcc",accounts)
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
def load():#Function to display loading screen
    print("Loading");time.sleep(0.5);clear()
    print("Loading.");time.sleep(0.5);clear()
    print("Loading..");time.sleep(0.5);clear()
    print("Loading...");time.sleep(0.5);clear()
def admin():#Function to allow admin to manage the program
    adminpass=fileRead("bustle_files/UserAcc")
    adminpass=adminpass["admine"]
    clear()
    mastchoice1=input("What would you like to do?\n1)Add provider\n2)Delete provider\n3)Manage Vouchers\n4)Manage User Accounts\n5)Logout\n")
    if mastchoice1=='1':
        mastchoice2=input("Choose a category to add to: \n1)Restaurant\n2)Hotel\n3)Bus\n4)Spa\n5)Bicycle Repair\n")#Add other services here
        if mastchoice2=='1' or mastchoice2=='2' or mastchoice2=='3':
            if mastchoice2=='1':
                tempname="restaurant"
                try:
                    service=fileRead(f"bustle_files/{tempname}")
                except:
                    fileWrite(f"bustle_files/{tempname}",{})
                    service=fileRead(f"bustle_files/{tempname}")
            elif mastchoice2=='2':
                tempname="hotel"
                try:
                    service=fileRead(f"bustle_files/{tempname}")
                except:
                    fileWrite(f"bustle_files/{tempname}",{})
                    service=fileRead(f"bustle_files/{tempname}")
            elif mastchoice2=='3':
                tempname="bus"
                try:
                    service=fileRead(f"bustle_files/{tempname}")
                except:
                    fileWrite(f"bustle_files/{tempname}",{})
                    service=fileRead(f"bustle_files/{tempname}")
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
            fileWrite(f"bustle_files/{tempname}",service)
            clear()
            print("Provider successfully added!")
            time.sleep(3)
            admin()
        elif mastchoice2=='4' or mastchoice2=='5':
            if mastchoice2=='4':
                tempname="spa"
                try:
                    service=fileRead(f"bustle_files/{tempname}")
                except:
                    fileWrite(f"bustle_files/{tempname}",{})
                    service=fileRead(f"bustle_files/{tempname}")
            elif mastchoice2=='5':
                tempname="cycle"
                try:
                    service=fileRead(f"bustle_files/{tempname}")
                except:
                    fileWrite(f"bustle_files/{tempname}",{})
                    service=fileRead(f"bustle_files/{tempname}")
            while True:
                try:
                    if mastchoice2=='5':
                        nptype='cycle'
                        npname,npexp=input("Enter Name/Experience\n").split('/')
                    else:
                        npname,nptype,npexp=input("Enter Name/Expertise/Experience\n").split('/')
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
            fileWrite(f"bustle_files/{tempname}",service)
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
                service=fileRead(f"bustle_files/{tempname}")
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
            dpname=input("Which provider would you like to delete?\n")
            if dpname in service:
                loginpass=stdiomask.getpass("Enter admin password to confirm:\n")
                if loginpass==adminpass:
                    del service[dpname]
                    fileWrite(f"bustle_files/{tempname}",service)
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
                    break
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
                    break
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
    gchoice=input("1)Snake!\n2)Sudoku(Coming Soon...)\n3)#Tic-Tac-Toe#(Coming Soon...)\n4)Back\n")
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
        exec(open("").read())
    elif gchoice =='3':
        exec(open("").read())
    elif gchoice=='4':
        home()
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
        voucher()
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
def menu():#Starting page of the program
    try: 
        fileRead("bustle_files/UserAcc")
        fileRead("bustle_files/vouchers")
    except:
        fileWrite("bustle_files/UserAcc",{'admine':'mpass'})
        fileWrite("bustle_files/vouchers",{"admine":[[],[],[],[]]})
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
    bchoice = input("Which service would you like to book?\n1.Restaurant\n2.Hotel\n3.Bus\n4.Cycle Repair\n5.Spa\n")
    if bchoice == '1':
        Restaurant()
    elif bchoice == '2':
        Hotel()
    else:
        clear()
        home()
def Restaurant(): #Choosing Restaurants
    from datetime import datetime
    try:
        fileRead("bustle_files/restaurant")
    except:
        clear()
        print("Error 404: Page not found")
        time.sleep(3)
        Booking()
    name = "Restaurant"
    clear()
    slots = fileRead("bustle_files/restaurant")
    print("Which restaurant would you like to book a table in?")
    for key in slots:
        print(key)
    print("(Press 'c' to go back)")
    rchoice = input()
    if rchoice in slots:
        try:
            fileRead(f"bustle_files/{rchoice}")
        except:
            fileWrite(f"bustle_files/{rchoice}", {"10:00-12:00":[slots[rchoice][0],slots[rchoice][1]],"12:00-2:00":[slots[rchoice][0],slots[rchoice][1]],"2:00-4:00":[slots[rchoice][0],slots[rchoice][1]],"4:00-6:00":[slots[rchoice][0],slots[rchoice][1]],"6:00-8:00":[slots[rchoice][0],slots[rchoice][1]],"8:00-10:00":[slots[rchoice][0],slots[rchoice][1]]})
        booking = fileRead(f"bustle_files/{rchoice}")
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
                                    fileWrite(f"bustle_files/{rchoice}",booking)
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
        fileRead("bustle_files/hotel")
    except:
        clear()
        print("Error 404: Page not found")
        time.sleep(3)
        Booking()
    name = 'Hotel'
    clear()
    slots = fileRead("bustle_files/hotel")
    print("Which hotel would you like to book a room in?")
    for key in slots:
        print(key)
    print("(Press 'c' to go back)")
    hchoice = input()
    if hchoice in slots:
        clear()
        try:
            fileRead(f"bustle_files/{hchoice}")
        except:
            fileWrite(f"bustle_files/{hchoice}",[slots[hchoice][0],slots[hchoice][1]])
        booking = fileRead(f"bustle_files/{hchoice}")
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
                                print("Hotel name:",hchoice)
                                print("No.of rooms to be booked:",nchoice)
                                print("Total price:",price)
                                pchoice = input("\nDo you wish to continue?(y/n)\n")
                                if pchoice == 'y':
                                    if checkout():
                                        print("Payment successful")
                                        avail = avail - int(nchoice)
                                        booking[0] = str(avail)
                                        fileWrite(f"bustle_files/{hchoice}",booking)
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
def checkout(): #Checkout page
    clear()
    load()
    while True:
        pchoice = int(input("How would you like to make your payment?:\n1.Debit card\n2.Credit card\n"))
        if pchoice == 1:
            while True:
                dcn = input("Enter Debit Card number:")
                if len(dcn) == 16:
                    dcna = input("Enter Name of card holder:")
                    exp = input("Enter card expiry date:")
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
                    ccna = input("Enter Name of card holder:")
                    exp = input("Enter card expiry date:")
                    cvv = input("Enter cvv:")
                    return True
                else:
                    print("Invalid Credit Card number!")
                    time.sleep(3)
                    clear()
        else:
            print("Invalid Input!")
            time.sleep(3)
            clear()
def BookingHist(name, service, price, time):#Funtion to display the Bookings History page
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
    if name != None and service != None and price != None and time != None:
        x.append(name)
        y.append(service)
        p.append(price)
        z.append(time)
        hist.update({user:(y,x,p,z)})
    fileWrite("bustle_files/bookings",hist)
    print("\t\t\tBooking history")
    print(f"\nUser:{user}\n")
    order = list(zip(x,y,z,p))
    l = ["Service","Name","Amount paid","Time of booking"]
    order.insert(0,l)
    print(tabulate(order, headers = "firstrow", tablefmt = "fancy_grid", showindex = range(1,len(order))))
    bchoice = input("\n(Press 'c' to go back)\n")
    if bchoice == 'c':
        home()
menu()#Starts Execution here