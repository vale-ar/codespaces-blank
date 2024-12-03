for numerito in range(1, 101):
    if numerito % 3 == 0 and numerito % 5 == 0:
        print("FizzBuzz")
    elif numerito % 3 == 0:
        print("Fizz")
    elif numerito % 5 == 0:
        print("Buzz")
    else:
        print(numerito)