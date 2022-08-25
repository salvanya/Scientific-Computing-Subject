import random

InvalidInput = True

while InvalidInput:
    numberOfMatches = input("Enter the number of matches: ") 
    try:
        numberOfMatches = int(numberOfMatches)
    except:
        print("The number must be an integer")
    else:
        numberOfMatches = int(numberOfMatches)
        InvalidInput = False

def createMatchesList(numberOfMatches): 
    matches = []

    for i in range(numberOfMatches):
        matches.append(random.randrange(-1 ,2))
    
    return matches

matches = createMatchesList(numberOfMatches)



print("\nThe start condition is:\n", matches, "\n")

def propagate(Matches):
    
    previousState = Matches
    newState = []
    firstIteration = True
    iterationCounter = 1
    while previousState != newState:      
        
        print("Iteration ", iterationCounter, ":\n")

        if not firstIteration:
            previousState = newState
            newState = []
        
        firstIteration = False

        print("Previous state: ", previousState, "\n")

        for index, match in enumerate(previousState):
            if match == 0:
                if index == 0:
                    if previousState[1] == 1:
                        newState.append(1)
                elif index == (len(previousState)-1):
                    if previousState[index-1] == 1:
                        newState.append(1)
                else:
                    if previousState[index-1] == 1 or previousState[index+1] == 1:
                        newState.append(1)
                    else:
                        newState.append(0)
            elif match == 1:
                newState.append(-1)
            elif match == -1:
                newState.append(-1)
                
        print("New state: ", newState, "\n")
        iterationCounter += 1
    
    return newState        
    


matches = propagate(matches)

print("The final state is:\n", matches)




