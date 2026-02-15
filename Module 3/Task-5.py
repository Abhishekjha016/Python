#Calculating factorial using a loop

num1 = int(input("Enter the number: "))
def fact_rec(num1):
    if num1 == 1:
        return 1
    elif num1 > 1:
        factorial = num1 * fact_rec(num1 - 1)
        return factorial
    else:
        print(f" The Factorial of {num1} is not existing.")

print(f"Factorial of {num1} is {fact_rec(num1)}")
