"""
Una pizzeria se instala en DUOC. Es su trabajo crear un programa para realizar pedidos

Para esto, el programa debe mostrar la lista de pizzas (dada a usted) y el precio de cada una de estas.
Luego, debe preguntar al usuario que tipo de usuario es.

Una vez que el usuario elije todas las pizas que desee comprar, se le aplicarán
descuentos segun lo siguiente:

Si el usuario es tipo "estudiante": 20% de descuento al total de la compra
Si el usuario es tipo "profesor": 10% de descuento al total de la compra

Si lleva 3 pizzas "Napolitanas", solo paga 2
Si lleva 2 pizzas de "Pepperoni", 10% de descuento al total de la compra

Los descuentos se acumulan.

Una vez que un usuario compra sus pizzas, se puede pasar a otro usuario o finalizar el programa.
El programa debe mostrar el total de las ganancias (las ventas totales de todos los usuarios)

Puede asumir que el usuario ingresa bien los datos
NO puede usar ninguna libreria
"""
#Pizas y precios de cada una
# Tradicional 12000
# Pepperoni 14000
# Margarita 12500
# Napolitana 11000
# Carnes 17000
usuario = 0
while True:
    matriz_pizzas=[["Tradicional",12000],["Pepperoni",14000],["Margarita",12500],["Napolitana",11000],["Carnes",17000]]
    print("Bienvenido a la pizzeria DUOC\nEstos son nuestros tipos de pizzas y sus precios")
    for i in range(len(matriz_pizzas)): 
        print(i+1,".",matriz_pizzas[i][0],matriz_pizzas[i][1])  #llamo a la matriz y le digo que me imprima el numero de la pizza y su nombre y precio
    total = 0
    print("¿Que pizza desea comprar?")
    while True:
        pizza = int(input("Ingrese el numero de la pizza que desea comprar: "))
        cantidad = int(input("Ingrese la cantidad de pizzas que desea comprar: "))
        if pizza < 1 or pizza > 5:
            print("Ingrese un numero valido")
        else:
            total = total + (matriz_pizzas[pizza-1][1] * cantidad)
            if pizza == 4 and cantidad == 3:
                total = total - matriz_pizzas[pizza-1][1]
                print(f"hay un beneficio de llevar 3 pizzas Napolitanas al precio de 2")
                print(f"Entonces el  total de la compra es de {total}")
            elif pizza == 2 and cantidad == 2:
                total = total - (total * 0.1)
                print(f"hay un descuento al llevar 2 pizzas Pepperoni del 10%")
                print(f"Entonces el  total de la compra es de {total}")
            else:
                print(f"Entonces el  total de la compra es de {total}")
        opcion = int(input("¿Desea comprar otra pizza?\nIngrese un digito\n1. Si\n2. No\n"))
        if opcion == 2:
            break
    print(f"El total de las ventas es de {total}")
    matriz_tipo_user = [["Estudiante",1],["Profesor",2],["Otro",3]]
    print("¿Que tipo de usuario es?\n1. Estudiante\n2. Profesor\n3. Otro (administrativos, limpieza, etc)")
    tipo = int(input("Ingrese el numero del tipo de usuario: "))
    if tipo < 1 or tipo > 3:
        print("Ingrese un numero valido")
    else :
        print(f"El tipo de usuario es: '{matriz_tipo_user[tipo-1][0]}'")
    if tipo == 1:
        print("Usted es estudiante por lo que se le aplicara un 20% de descuento")
        total = total - (total * 0.2)
    elif tipo == 2:
        print("Usted es profesor por lo que se le aplicara un 10% de descuento")
        total = total - (total * 0.1)
    else:
        print("Usted es otro tipo de usuario por lo que no se le aplicara ningun descuento")
    print(f"El total de la compra con descuento es de {total}")

    print("Gracias por preferirnos")

    print("Vuelva pronto")
    usuario = usuario + 1
    cliente = int(input("¿hay otro usuario?\n1. Si\n2. No"))
    if cliente == 2:
        break

total_usuarios = 0 
total_ganancias = 0
total_usuarios = total_usuarios + usuario
total_ganancias = total_ganancias + total
print(f"El total de las ganancias es de {total_ganancias} y el total de los usuarios es de {total_usuarios}")