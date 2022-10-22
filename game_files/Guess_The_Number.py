import random #used to generate a random number in a given range

#assigns a number of lives for each difficulty
easy_lives = 7
normal_lives = 5
hard_lives = 3

print("Welcome to Guess The Number\n")
print("Do you want to play on:\n1. Easy mode\n2. Normal mode\n3. Hard mode\n4. Nightmare mode\n")
choice = int(input("Enter your choice\n"))
if choice==1:
    while(easy_lives!=0): #Player can only play as long as they have lives
        print("Guess the number in the range 1-20\n")
        ran = random.randint(1,20) #Generates a random integer in the range 1 to 20, including both end points
        numb = int(input("Enter your guess\n"))
        if numb == ran:
            print("Congratulations, you won the game!\n")
            exit() #If the player guesses right, they win the game and the game is quit
        else:
            print("That was wrong, try again\n")
            easy_lives-=1 #Every incorrect guess subtracts a life
    print("Bad luck\nGAME OVER\n")
    exit() #As these two lines are only executed if the while loop condition fails, we know that easy_lives must be 0 and so, the game is ended and exited

elif choice==2:
    while(normal_lives!=0):
        print("Guess the number in the range 1-25\n")
        ran = random.randint(1,25)
        numb = int(input("Enter your guess\n"))
        if numb == ran:
            print("Congratulations, you won the game!\n")
            exit()
        else:
            print("That was wrong, try again\n")
            normal_lives-=1
    print("Bad luck\nGAME OVER\n")
    exit()

elif choice==3:
    while(hard_lives!=0):
        print("Guess the number in the range 1-40\n")
        ran = random.randint(1,40)
        numb = int(input("Enter your guess\n"))
        if numb == ran:
            print("Congratulations, you won the game!\n")
            exit()
        else:
            print("That was wrong, try again\n")
            hard_lives-=1
    print("Bad luck\nGAME OVER\n")
    exit()
    
if choice==4: #nightmare mode is only given one guess and so there is no need to create a variable to store it or a while loop
    print("Guess the number in the range 1-60\n")
    ran = random.randint(1,60) #to live up to the title of nightmare, the player is given an extremely large range and only one chance to get it right
    numb = int(input("Enter your guess\n"))
    if numb == ran:
        print("Congratulations, you won the game!\n")
        exit()
    else:
        print("Bad luck\nGAME OVER\n")
        exit()