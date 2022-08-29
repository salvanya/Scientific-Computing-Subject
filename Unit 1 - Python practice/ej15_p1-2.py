import myfuncs as mf

print('Enter two numbers to calculate Greatest common divisor and Least common multiple')
number1 = int(input())
number2 = int(input())

def gcd(number1, number2):
    number1Factor = mf.primeFact(number1,2)
    number2Factor = mf.primeFact(number2,2)

    number1UniqueFactors = mf.uniqueElements(number1Factor)
    number2UniqueFactors = mf.uniqueElements(number2Factor)

    number1UniqueFactorsCount = mf.uniqueElementsCount(number1UniqueFactors)
    number1UniqueFactorsCount = mf.uniqueElementsCount(number2UniqueFactors)

    commonDivisors = []

    for factor, quatity in number1UniqueFactorsCount:
        if factor