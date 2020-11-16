#  This script is used for reference
#  to the Lesson 1 - Python basics

import random
options = ['rock','paper','scissors']


def translate(choice):
    option_index = choice - 1
    return options[option_index]


def shoot():
    print('''

1) Rock
2) Paper
3) Scissors

q) Quit''')

    x = input("Choice: ")
    return(x)

def get_user_input():
    while True:
        user_string = shoot()
        if (user_string == 'q'):
            user_int = user_string
            break
        else:
            try:
                user_int = int(user_string)
                if (user_int < 0) or (user_int > 3):
                    print ("Error! Not a valid choice")
                else:
                    break
            except ValueError:
                print("Error! Must choose a number")
    return user_int

def option_compare(choice1,choice2):
    #  Results
    #  0 - tie
    #  1 - choice1
    #  2 - choice2

    if choice1 == 'rock':
        if choice2 == 'rock':
            return 0
        elif choice2 == 'paper':
            return 2
        else:
            return 1
    elif choice1 == 'paper':
        if choice2 == 'rock':
            return 1
        elif choice2 == 'paper':
            return 0
        else:
            return 2
    elif choice1 == 'scissors':
        if choice2 == 'rock':
            return 2
        elif choice2 == 'paper':
            return 1
        else:
            return 0

if __name__ == "__main__":
    user_score = 0
    comp_score = 0
    while True:
        user_guess = get_user_input()
        if (user_guess == 'q'):
            break
        comp_guess = random.choice(options)
        user_guess = translate(user_guess)
        result = option_compare(user_guess,comp_guess)
        print("You      chose {}".format(user_guess))
        print("Computer chose {}".format(comp_guess))
        if result == 0:
            print("TIE!")
            print("CURRENT SCORE:")
            print("{:10}:{:3}".format("User Score",user_score))
            print("{:10}:{:3}".format("Computer Score",comp_score))
            print("\n"*3)
        elif result == 1:
            print("YOU WON!")
            user_score+=1
            print("CURRENT SCORE:")
            print("{:10}:{:3}".format("User Score",user_score))
            print("{:10}:{:3}".format("Computer Score",comp_score))
            print("\n"*3)
        else:
            print("COMPUTER WON!")
            comp_score+=1
            print("CURRENT SCORE:")
            print("{:10}:{:3}".format("User Score",user_score))
            print("{:10}:{:3}".format("Computer Score",comp_score))
            print("\n"*3)
    print("Thanks for playing!")
    print("{:10}:{:3}".format("User Score",user_score))
    print("{:10}:{:3}".format("Computer Score",comp_score))
    if user_score > comp_score:
        print("YOU WON!")
    elif comp_score > user_score:
        print("YOU LOST :(")
    else:
        print("YOU TIED")
