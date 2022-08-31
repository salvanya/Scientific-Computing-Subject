import matplotlib.pyplot as plt
import numpy as np

file = open("data/ej11.dat")

elemQuant = file.readline()

data = []

for element in file:
    data.append(int(element))

file.close()

def uniqueElements(data):
    uniqueElements = []

    for element in data:
        if not (element in uniqueElements):
            uniqueElements.append(element)
    return uniqueElements

print('All data: ', data)    
print('Unique elements: ', uniqueElements(data))    

def uniqueElementsCount(dataList, uniqueElementList):
    
    uniqueElementCountedList = {}
    
    for uniqueElement in uniqueElementList:
        count = 0
        
        for element in dataList:
            if element == uniqueElement:
                count += 1
        
        uniqueElementCountedList[uniqueElement] = count

    return uniqueElementCountedList

print('The unique element count is: ', uniqueElementsCount(data, uniqueElements(data)) )

def elementCountToPlot(uniqueElementCountedList):
    x = []
    y = []
    for element in uniqueElementCountedList:
        x.append(str(element))
        y.append(uniqueElementCountedList[element])

    return np.array(x), np.array(y)

x, y = elementCountToPlot( uniqueElementsCount(data, uniqueElements(data)) )

#print(f'x:{x}\n x length={len(x)} ')
#print(f'y:{y}\n y length={len(y)} ')

plt.bar(x, y)

plt.show()




