import random 
sum = random.randint(1,6) + random.randint(1,6)
print("You got: " + str(sum))
win = False
# in the code I use the "while" loop to run the multiple times until the right number is met (7,11,2,3,12), if the "win" stay false 
# then the game will continue to the second round, and will stop until the numbers are met which then my "Win" varuable will swtich into True from False 
# and the game will end, if the "Win" will stay False then the while loop will continue to run the game until it hits on of the numbers.

# loop until player wins or loses
while not win:
    # Checks if the player won or lost in the first round, if the numbers are not met then it will continue to the second round.
    if sum == 7 or sum == 11:
        print("You win")
        win = True
    elif sum == 2 or sum == 3 or sum == 12:
        print("You lose")
        win = True
    else: #Second round starts here, which checks again if the player either won or lost, and if player did not roll the right numbers the while loop will continue.
        sum2 = random.randint(1,6) + random.randint(1,6)
        if sum2 == sum:
            print("You win in second trial")
            win = True
        elif sum2 == 7:
            print("You lose in second trial")
            win = True
        else: # Here we at the end of the loop, at this point the game will reroll again and check if player won/lost in first round or second round.
            sum = sum2
            print("Rolling again...")