# We are going to write a program that generates a random number and asks the user to guess it.
# If the player's guess is higher than the actual number, the program displays "Lower number please".Similarly if user's guess is lower than the actual number, the program displays "Higher number please".When the user guesses the correct number, the program displays the number of guesses the player used to arrive at the number.
# Hint:Use the random module
import random
randNo=random.randint(1, 100)
userGuess=int(input("Enter your guess:"))
nguesses=1
while(userGuess!=randNo):
    if(userGuess>randNo):
        userGuess=int(input("Enter lower number please:"))
    elif(userGuess<randNo):
        userGuess=int(input("Enter higher number please:"))
    nguesses=nguesses+1
print(f"You guessed the number in {nguesses} attempts")