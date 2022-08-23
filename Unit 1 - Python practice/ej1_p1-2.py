import numpy as np 
text='El cambio de movimiento es directamente proporcional a la fuerza motriz\
 impresa y ocurre según la línea recta a lo largo de la cual aquella fuerza\
 se imprime.'

print(text)

print("\na) ------------------------\n")

textEvenWords = ""
evenWord = True
for character in text:
    if evenWord:
        textEvenWords += character
    
    if character == " ":
        if evenWord == True:
            evenWord = False
        elif evenWord == False:
            evenWord = True
print (textEvenWords)

print("\nb) ------------------------ \n")

splitedText = text.split()

for word in splitedText:
    if "e" in word:
        print(word)

 
 

