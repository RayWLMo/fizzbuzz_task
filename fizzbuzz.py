num = 0

for num in range(100):
    num += 1
    if num % 3 == 0 and num % 5 != 0:
        print("Fizz")
        num +=1

    elif num % 5 == 0 and num % 3 != 0:
        print("Buzz")
        num += 1

    elif num % 15 == 0:
        print("FizzBuzz")
        num += 1

    else:
        print(num)
        num += 1
