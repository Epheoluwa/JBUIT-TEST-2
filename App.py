import random

initial_score = 10
tk_game = ()

rand_num = random.randint(1 , 10)
print("Welcome to my guessing game Friends")
name = str(input("Please enter your name: "))
print(f'Welcome: {name}, You have three attempts to guess a number from 1 to 10')
print("GOODLUCK!!")
print("Hint: You will be directed either guessed number is higher or lower than random number, Enjoy!!!")

trail = 1
while trail < 4:
    initial_score -= 1
    number = int(input("Enter number: "))
    if number == rand_num :
        print("Congratulations!!, You have guessed the right number")
        print("your score is", initial_score + 1)
        break
    elif number < rand_num:
        print(f'HINT: Number is greater than {number} , please try again')
        print('Your score now is ', initial_score)
    elif number > rand_num:
        print(f'HINT: Number is lesser than {number}, please try again')
        print('Your score now is ', initial_score)
    else:
        break

    trail += 1
