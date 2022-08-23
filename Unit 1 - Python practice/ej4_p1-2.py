import random

Namess = ["Lionel", "Lautaro", "Ángel", "Rodrigo", "Leandro", "Giovanni" ]

def printGrades(Names):
        for Name in Names:
            grade = random.randrange(1,11)
            if grade >= 6:
                print(Name, " tu nota es un", grade, ". Felicitaciones aprobaste!")
            else:
                print(Name, " tu nota es un", grade, ". Vamos que en el recuperatorio sale!")

printGrades(Namess)
