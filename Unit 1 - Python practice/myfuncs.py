def primeFact (i, f):
    if i < f:
        return []
    if i % f == 0:
        return [f] + primeFact (i / f, 2)
    return primeFact (i, f + 1)

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

def uniqueElements(data):
    uniqueElements = []

    for element in data:
        if not (element in uniqueElements):
            uniqueElements.append(element)
    return uniqueElements

def uniqueElementsCount(dataList, uniqueElementList):
    
    uniqueElementCountedList = {}
    
    for uniqueElement in uniqueElementList:
        count = 0
        
        for element in dataList:
            if element == uniqueElement:
                count += 1
        
        uniqueElementCountedList[uniqueElement] = count

    return uniqueElementCountedList