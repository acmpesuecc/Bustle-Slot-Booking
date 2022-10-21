import random

easy_lives = 7
normal_lives = 5
hard_lives = 3

print("Welcome to Guess The Number\n")
print("Do you want to play on:\n1. Easy mode\n2. Normal mode\n3. Hard mode\n4. Nightmare mode\n")
choice = int(input("Enter your choice\n"))
if choice==1:
    while(easy_lives!=0):
        print("Guess the number in the range 1-20\n")
        ran = random.randint(1,20)
        numb = int(input("Enter your guess\n"))
        if numb == ran:
            print("Congratulations, you won the game!\n")
            exit()
        else:
            print("That was wrong, try again\n")
            easy_lives-=1
    print("Bad luck\nGAME OVER\n")
    exit()

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
    
if choice==4:
    print("Guess the number in the range 1-60\n")
    ran = random.randint(1,60)
    numb = int(input("Enter your guess\n"))
    if numb == ran:
        print("Congratulations, you won the game!\n")
        exit()
    else:
        print("Bad luck\nGAME OVER\n")
        exit()