def isItPrime(number):

    if number <= 1:
        return False

    if number == 2 or number == 3:
        return True
    

    naturalNumber = 2
    
    while naturalNumber < number:
        if number % naturalNumber == 0:
            return False        
        naturalNumber += 1

    return True

def generatePrimeList(limit):
    primeList = []

    for number in range(limit): 
        if isItPrime(number):
            primeList.append(number)

    return primeList

limit = int(input("Enter a natural number: "))

print( generatePrimeList(limit) )
