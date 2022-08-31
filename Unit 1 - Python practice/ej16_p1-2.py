import numpy as np

def logExPlusOne(number, terms):
    if not -1 < number < 1:
        print('Error! The number must be |x| < 1 ')
        return np.NaN  
    
    logSum = 0

    for i in range(terms):
        logSum += ( ( (-1)**(i) ) / (i+1) ) * (number**(i+1))
#        print(f'Iteration {i+1}, result {logSum}')
    
    return logSum

def logExPlusOneRecursive(number, terms, start=0, currentTerm=0):

    if currentTerm == (terms):
        return start
    
    if not -1 < number < 1:
        print('Error! The number must be |x| < 1 ')
        return np.NaN  
    
    logSum = start

    term = currentTerm

    logSum += ( ( (-1)**(term) ) / (term+1) ) * (number**(term+1))        

#    print(f'Recursion {currentTerm+1}, result {logSum}')

    currentTerm += 1

    logSum = logExPlusOneRecursive(number, terms, logSum, currentTerm)

    return logSum

number = float(input('Enter a number between -1<x<1 to calculate log(x+1): '))
terms = int(input('Enter a number of terms: '))

print(f'Sumatory Method: {logExPlusOne(number,terms)}')

print(f'Recursive Method: {logExPlusOneRecursive(number,terms)}')

print(f'Numpy Method: {np.log10(1+number)}')