#Task #1 
def factorial(n):
    if n < 0:
        return "Factorial is not defined for -ve numbers"
    elif n== 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2,n+1):
            result *= i
        return result   

# Example usage
output = factorial(5)
print("Factorial of 5 is:", output)