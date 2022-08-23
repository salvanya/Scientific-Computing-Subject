Namess = ["Lionel", "Lautaro", "Ángel", "Rodrigo", "Leandro", "Giovanni" ]
gradess = [10, 9, 10, 5, 7, 4]

def printGrades(Names, grades):
    if len(Names) == len(grades):
        for Name in Names:
            if grades[Names.index(Name)] >= 6:
                print(Name, " tu nota es un", grades[Names.index(Name)], ". Felicitaciones aprobaste!")
            else:
                print(Name, " tu nota es un", grades[Names.index(Name)], ". Vamos que en el recuperatorio sale!")
    else:    
        print("Error, las longitudes de las listas no coinciden")

printGrades(Namess, gradess)

