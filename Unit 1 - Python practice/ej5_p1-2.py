# import random

# InvalidInput = True

# while InvalidInput:
#     numberOfMatches = input("Enter the number of matches: ") 
#     try:
#         numberOfMatches = int(numberOfMatches)
#     except:
#         print("The number must be an integer")
#     else:
#         numberOfMatches = int(numberOfMatches)
#         InvalidInput = False

# def createMatchesList(numberOfMatches): 
#     matches = []

#     for i in range(numberOfMatches):
#         matches.append(random.randrange(-1 ,2))
    
#     return matches

# matches = createMatchesList(numberOfMatches)

matches = [1,0,0,-1,0,0,1]

print("\nThe start condition is:\n", matches, "\n")

def propagate(Matches):
   
    currentState = Matches
    previousState = []
   
    while previousState != currentState:
        previousState = currentState
        for index, match in enumerate(previousState):
            if match == 0:
                if index == 0: 
                    if previousState[1] == 1:
                        currentState[0] = 1
                elif index == (len(previousState)-1):
                    if previousState[index-1] == 1:
                        currentState[index] = 1
                else:
                    if previousState[index-1] == 1 or previousState[index+1] == 1:
                        currentState[index] = 1
            elif match == 1:
                currentState[index] = -1

        print("Previous state: ", previousState)
        print("Current state: ", currentState, "\n")
    
    return currentState        

matches = propagate(matches)

print("The final state is:\n", matches)




