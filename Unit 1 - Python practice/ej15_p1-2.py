import myfuncs as mf

def gcd(number1, number2):
    number1Factor = mf.primeFact(number1,2)
    number2Factor = mf.primeFact(number2,2)

    number1UniqueFactors = mf.uniqueElements(number1Factor)
    number2UniqueFactors = mf.uniqueElements(number2Factor)

    number1UniqueFactorsCount = mf.uniqueElementsCount(number1Factor, number1UniqueFactors)
    number2UniqueFactorsCount = mf.uniqueElementsCount(number2Factor, number2UniqueFactors)

    commonDivisors = {}

    for factor in number1UniqueFactorsCount.keys():
        if factor in number2UniqueFactorsCount.keys():
            if number1UniqueFactorsCount[factor] < number2UniqueFactorsCount[factor]:
                commonDivisors[factor] = number1UniqueFactorsCount[factor]
            else:
                commonDivisors[factor] = number2UniqueFactorsCount[factor]
    
    numericGCD = 1

    for factor in commonDivisors.keys():
        numericGCD *= factor**commonDivisors[factor]

    return numericGCD, commonDivisors


def lcm(number1, number2):
    number1Factor = mf.primeFact(number1,2)
    number2Factor = mf.primeFact(number2,2)

    number1UniqueFactors = mf.uniqueElements(number1Factor)
    number2UniqueFactors = mf.uniqueElements(number2Factor)

    number1UniqueFactorsCount = mf.uniqueElementsCount(number1Factor, number1UniqueFactors)
    number2UniqueFactorsCount = mf.uniqueElementsCount(number2Factor, number2UniqueFactors)
    
    commonMultiples = {}

    for factor in number1UniqueFactorsCount.keys():
        if factor in number2UniqueFactorsCount.keys():
            if number1UniqueFactorsCount[factor] > number2UniqueFactorsCount[factor]:
                commonMultiples[factor] = number1UniqueFactorsCount[factor]
            else:
                commonMultiples[factor] = number2UniqueFactorsCount[factor]
        else:
            commonMultiples[factor] = number1UniqueFactorsCount[factor]

    for factor in number2UniqueFactorsCount.keys():
        if factor not in number1UniqueFactorsCount:
            commonMultiples[factor] = number2UniqueFactorsCount[factor]
    
    numericLCM = 1

    for factor in commonMultiples.keys():
        numericLCM *= factor**commonMultiples[factor]

    return numericLCM, commonMultiples

print('Enter two numbers to calculate Greatest common divisor and Least common multiple')
number1 = int(input())
number2 = int(input())

# print(f'Number 1 factor: {mf.primeFact(number1,2)}')
# print(f'Number 2 factor: {mf.primeFact(number2,2)}')


# print(f'Number 1 factor unique: {mf.uniqueElements(mf.primeFact(number1,2))}')
# print(f'Number 2 factor unique: {mf.uniqueElements(mf.primeFact(number2,2))}')

# print(f'Number 1 factor unique counted: {mf.uniqueElementsCount(mf.primeFact(number1,2), mf.uniqueElements(mf.primeFact(number1,2)))}')
# print(f'Number 2 factor unique counted: {mf.uniqueElementsCount(mf.primeFact(number2,2), mf.uniqueElements(mf.primeFact(number2,2)))}')



numericGCD, factorsGCD = gcd(number1, number2)
numericLCM, factorsLCM = lcm(number1, number2)

print(f"The Greatest common divisor between {number1} and {number2} is: {numericGCD}\n \
    It's factors are: {factorsGCD} ")
print(f"The Least common mutiple between {number1} and {number2} is: {numericLCM}\n \
    It's factors are: {factorsLCM} ")
