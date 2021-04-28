winning_number = 45
user_input=int(input("guess a number from 1 to 100 :"))
if(user_input==winning_number):
    print("You Win!!")
else:
    if user_input<winning_number:
        print("Too low!!")
    else:
        print("Too high!!")



        ##Number Guessing Game