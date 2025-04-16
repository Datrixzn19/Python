dia = int(input("Introduces el numreo del dia de la semana: "))

match dia:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miercoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sabado")
    case 7:
        print("Domingo")



#Otra manera 
match dia:
    case 1 | 2 | 3:
        print("Primera mitad de la semana")
    case 4 | 5:
        print("Segunda mitad")



#los case tambien puede ser usado con texto
opcion = input("Elige una fruta (manzana, banana, naranja): ").lower()

match opcion:
    case "manzana":
        print("Fruta roja")
    case "banana":
        print("Fruta amarilla")
    case "naranja":
        print("Fruta naranja")
    case _:
        print("Fruta desconocida")