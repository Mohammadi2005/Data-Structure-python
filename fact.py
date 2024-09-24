def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number-1)

number = int(input("Enter a number for give factorial : "))
result = factorial(number)
print(result)






