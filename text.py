#Esta funcion te imprime la matriz, puedes acceder a la matriz con cordenadas X e Y como está al principio del codigo para poscicionar la S
def imprimir_matriz(gametable):
    for fila in gametable:
        print("".join(fila))  
#Esta funcion es para cuando la tabla es pequeña y tiene que hacer la conversión a binario, pero es puro texto más o menos, entra la flag para que cuando ponga -1 salga del loop
def short_gametable(direction,flag):
    while True:
        if direction == "W":
            print("Escribe la cantidad de pasos que vas a moverte hacia arriba en binario: ")
            break
        elif direction == "A":
            print("Escribe la cantidad de pasos que vas a moverte hacia la izquierda en binario: ")
            break
        elif direction == "S":
            print("Escribe la cantidad de pasos que vas a moverte hacia abajo en binario: ")
            break
        elif direction == "D":
            print("Escribe la cantidad de pasos que vas a moverte hacia la derecha en binario: ")
            break
        elif direction == "-1":
            print("Saliendo...")
            flag[0]= False
            break
        else:
            print(" ")
            print("Dirección no reconocida, intentalo denuevo.")
            print("Ingresa a la dirección que deseas moverte.")
            print("W: Moverte hacia arriba.")
            print("A: Moverte hacia la izquierda.")
            print("S: Moverte hacia abajo.")
            print("D: Moverte hacia la derecha.")
            print("-1: Salir del juego.")
            direction = input().upper()

#Esta funcion es lo mismo solo que en vez de que diga binario dice octadecimal
def medium_gametable(direction, flag):
    while True:
        if direction == "W":
            print("Escribe la cantidad de pasos que vas a moverte hacia arriba en octadecimal: ")
            break
        elif direction == "A":
            print("Escribe la cantidad de pasos que vas a moverte hacia la izquierda en octadecimal: ")
            break
        elif direction == "S":
            print("Escribe la cantidad de pasos que vas a moverte hacia abajo en octadecimal: ")
            break
        elif direction == "D":
            print("Escribe la cantidad de pasos que vas a moverte hacia la derecha en octadecimal: ")
            break
        elif direction == "-1":
            print("Saliendo...")
            flag[0] = False
            break
        else:
            print(" ")
            print("Dirección no reconocida, intentalo denuevo.")
            print("Ingresa a la dirección que deseas moverte.")
            print("W: Moverte hacia arriba.")
            print("A: Moverte hacia la izquierda.")
            print("S: Moverte hacia abajo.")
            print("D: Moverte hacia la derecha.")
            print("-1: Salir del juego.")
            direction = input().upper()

#Esto lo mismo con la flag y con el texto
def large_gametable(direction, flag):
    while True:
        if direction == "w":
            print("Escribe la cantidad de pasos que vas a moverte hacia arriba en hexadecimal: ")
            break
        elif direction == "A":
            print("Escribe la cantidad de pasos que vas a moverte hacia la izquierda en hexadecimal: ")
            break
        elif direction == "S":
            print("Escribe la cantidad de pasos que vas a moverte hacia abajo en hexadecimal: ")
            break
        elif direction == "D":
            print("Escribe la cantidad de pasos que vas a moverte hacia la derecha en hexadecimal: ")
            break
        elif direction == "-1":
            print("Saliendo...")
            flag[0] = False
            break
        else:
            print(" ")
            print("Dirección no reconocida, intentalo denuevo.")
            print("Ingresa a la dirección que deseas moverte.")
            print("W: Moverte hacia arriba.")
            print("A: Moverte hacia la izquierda.")
            print("S: Moverte hacia abajo.")
            print("D: Moverte hacia la derecha.")
            print("-1: Salir del juego.")
            direction = input().upper()

#Esto es para que se imprima cada vez que quiera moverse, si quieres cambiar algo de estas funciones igual hazlo y lo pones en los comentarios :p
def movements():
    print("Ingresa a la dirección que deseas moverte.")
    print("W: Moverte hacia arriba.")
    print("A: Moverte hacia la izquierda.")
    print("S: Moverte hacia abajo.")
    print("D: Moverte hacia la derecha.")
    print("-1: Salir del juego.")
