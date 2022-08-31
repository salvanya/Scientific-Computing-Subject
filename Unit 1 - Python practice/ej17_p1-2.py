def Factorial(number):
    
    factorial = 1

    for i in range(number):
        factorial *= i+1

    return factorial

def FactorialRec(number, currentValue=1, currentRec=1):
    if currentRec == number+1:
        return currentValue

    currentValue *= currentRec

    currentRec += 1

    return FactorialRec(number, currentValue, currentRec)

number = int(input("Number to compute the factorial: "))

print(f'Factorial with iterative method: {Factorial(number)}')

print(f'Factorial with recursive method: {FactorialRec(number)}')

