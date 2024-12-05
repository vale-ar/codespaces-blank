# Instructions  
# Write a program that takes two input numbers, then adds them together and prints the result.

# **Remember** This project will be automatically graded, and computers are very literal!

## Extra time

# If you complete this task then please try adding the following features:
# * Take two numbers and subtract the second from the first number.
# * Take two numbers and multiply the two.
# * Take two numbers and divide the first number by the second number.
# * Take two numbers and perform a modulus operation.
# * Allow users to choose which operation they want to perform on two numbers.
# * Take 3 numbers and add them together.
# * Allow users to mix operations with 3 numbers or more
# e.g. 2 + 4 - 3, 4 *5 + 1 / 3

# **Note:** These features must be presented to the user *after* the initial task, or else the automatic grading will mark this as failed! Scoring for additional features will be done manually.

num1 = int(input("Introduce un numero: "))
num2 = int(input("Introduce un numero: "))
suma = num1 + num2
resta = num2 - num1
multi = num1 * num2
div = num1 / num2
mod = num1 % num2
eleccion = input("")


print(f"Este es tu resultado: {suma}")