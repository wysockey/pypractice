#todo, change to random number
import random

answer = random.randint(0,5)

guess =int(raw_input("Enter a number, 0-5:"))





print(answer, guess)

if(guess > answer):
	print("Your number is too high")
	guess = int(raw_input("Enter a number, 0-5"))
	if(guess > answer):
		print("your number is still too high.")
	elif(guess < answer):
		print("your number is too low.")
	elif(guess == answer):
		print("Good job you got my number!")


elif(guess < answer):
	print("Your number is too low. Please try again.")
	guess = int(raw_input("Enter a number, 0-5"))
	if( guess > answer):
		print("your number is still too high.")
	elif(guess< answer):
		print("your number is too low")
	elif (guess == answer):
		print("good job,  you guessed correctly.")
elif(guess == answer):
	print("Yes, you guessed my number")


