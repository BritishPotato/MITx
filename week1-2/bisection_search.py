low = 0
high = 100

print("Please think of a number between 0 and 100!")
while 1:
    check = int((high + low) / 2)
    ans = input("Is your secret number " + str(check) +"? \n" + \
                "Enter 'h' to indicate the guess is too high. " + \
                "Enter 'l' to indicate the guess is too low. " + \
                "Enter 'c' to indicate I guessed correctly. ")
    if ans == "h":
        high = check
    elif ans == "l":
        low = check
    elif ans == "c":
        break
    else:
        print("Sorry, I did not understand your input.")
        
print("Game over. Your secret number was: " + str(check))