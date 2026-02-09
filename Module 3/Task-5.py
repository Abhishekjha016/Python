#Calculating factorial using a loop

def factorial(number):
    fact = 1
    while number > 1:
        fact *= number
        number -= 1
    return fact
print(factorial(int(input("Enter the number: "))))