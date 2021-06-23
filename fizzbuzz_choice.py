num = 0

fizz = int(input("choose your Fizz number:  "))
buzz = int(input("choose your Buzz number:  "))
for num in range(100):
    num += 1
    if num % fizz == 0 and num % buzz != 0:
        print("Fizz")
        num +=1

    elif num % buzz == 0 and num % fizz != 0:
        print("Buzz")
        num += 1

    elif num % (fizz*buzz) == 0:
        print("FizzBuzz")
        num += 1

    else:
        print(num)
        num += 1