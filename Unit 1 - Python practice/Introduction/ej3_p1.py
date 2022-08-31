pointX = float(input("Ingrese la coordenada X del punto: "))
pointY = float(input("Ingrese la coordenada Y del punto: ")) 

if ((pointX**2)+(pointY**2))^0.5 < 0.75:
    print("El punto está dentro de la Región 1")
elif pointX > 0 and pointX < 1:
    if pointY > 0 and pointY < 1:
        print("El punto está dentro de la Región 2")
    elif pointY < 0 and pointY > -1:
        print("El punto está dentro de la Región 3")
    else:
        print("El punto no pertenece a ninguna región")
elif pointX < 0 and pointX > -1:
    print("El punto está dentro de la región 4")
else:
    print("El punto no está en ninguna región") 