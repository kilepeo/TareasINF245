import random
import text, functions

ancho = 11 
largo = int(input("Ingrese el largo del pasillo: ")) 
guardias = int(input("Ingrese la cantidad de guardias: "))
flag = [True] #Aquí la flag cuando queria modificarla no me dejaba, era o hacerla con esta cosa de listas, o trabajarla con una flag global, revisemos esto despuess

#Explicación de gpto
#Uso de una lista para flag: Al pasar flag como una lista (flag = [True]), puedes modificar el
# valor dentro de la función short_gametable porque las listas son mutables en Python. Así puedes cambiar el valor de flag[0] 
# desde dentro de la función y que se vea reflejado fuera de ella.
#Modificación de flag[0]: En lugar de flag = False, ahora usas flag[0] = False para cambiar el valor dentro de la lista

#También intenté tirar varias variables a la wea de funciones ponte tu la wea del asterisco, pero no caché como hacerlo pq siempre estoy ocupando 
#las variables, si quieres puedes ordenarlo más pero encuentro que está ordenadito igual.

binario = ["0","1"]
octadecimal = ["0","1","2","3","4","5","6","7"]
hexadecimal = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
gametable = [["X"] * largo for i in range(ancho)] 
fila = 5
columna =  0
gametable[fila][columna] = "S"
fila_asterisco = random.randint(0, ancho - 1)
if fila_asterisco != gametable[fila][columna]:
    fila_asterisco = random.randint(0, ancho - 1)
    gametable[fila_asterisco][-1] = "*"
else :
    fila_asterisco = random.randint(0, ancho - 1)

if guardias != 0:
    functions.guards(gametable, guardias, largo)

while flag[0]:  # <-- Asegúrate de usar flag[0] para evaluar la condición
    if largo <=20:
        text.imprimir_matriz(gametable)
        text.movements()
        direction = input().upper()
        text.short_gametable(direction, flag) 
        select = input()
        while True:
            if all(character in binario for character in select):  
                pasos = functions.binary(select)  
                for X in range(pasos):
                    gametable[fila][columna] = "X"
                    if direction == "W": 
                        if fila > 0:
                            fila -= 1
                    elif direction == "S":  
                        if fila < ancho - 1:
                            fila += 1
                    elif direction == "A":  
                        if columna > 0:
                            columna -= 1
                    elif direction == "D":  
                        if columna < largo - 1:
                            columna += 1

                    if gametable[fila][columna] == "!":
                        print("¡Has chocado con un guardia! Juego terminado.")
                        flag[0] = False
                        break 
                    elif gametable[fila][columna] == "*":
                        print("¡Has llegado al objetivo! Iniciando hackeo... ")
                        hack_num = random.randint(0,20)
                        #Aquí hay que meter la conversion de cambio de base de decimal a binario
                        print("Para poder finalizar el juego, debes escribir el siguiente número en decimal: ") # + Y aqui iria el valor que retorna la funcion
                        #Esto por ahora.
                        flag[0] = False
                        break 
                    
                if not flag[0]:  
                    break 
                print("Te has movido: " + str(pasos) + " pasos!")
                gametable[fila][columna] = "S"
                break
            else:
                print("Error: La entrada no es un número binario válido, intentelo denuevo.")
    elif 100 >= largo > 20:
        text.imprimir_matriz(gametable)
        text.movements()
        direction = input().upper()
        text.medium_gametable(direction,flag)
        select = input()
        while True:
            if all(character in octadecimal for character in select):  
                pasos = functions.octadecimal(select)
                for X in range(pasos):
                    gametable[fila][columna] = "X"
                    if direction == "W": 
                        if fila > 0:
                            fila -= 1
                    elif direction == "S":  
                        if fila < ancho - 1:
                            fila += 1
                    elif direction == "A":  
                        if columna > 0:
                            columna -= 1
                    elif direction == "D":  
                        if columna < largo - 1:
                            columna += 1
                    if gametable[fila][columna] == "!":
                        print("¡Has chocado con un guardia! Juego terminado.")
                        flag[0] = False
                        break 
                    elif gametable[fila][columna] == "*":
                        print("¡Has llegado al objetivo! Iniciando hackeo... ")
                        hack_num = random.randint(0,100)
                        #Aquí hay que meter la conversion de cambio de base de decimal a octadecimal
                        print("Para poder finalizar el juego, debes escribir el siguiente número en decimal: ") # + Y aqui iria el valor que retorna la funcion
                        #Esto por ahora.
                        flag[0] = False
                        break 

                if not flag[0]:  
                    break 
                print("Te has movido: " + str(pasos) + " pasos!")
                gametable[fila][columna] = "S"
                break
            else:
                print("Error: La entrada no es un número octadecimal válido, intentelo denuevo.")
    else:
        text.imprimir_matriz(gametable)
        text.movements()
        direction = input().upper()
        text.large_gametable(direction,flag)
        select = input()
        while True:
            if all(character in hexadecimal for character in select):  
                pasos = functions.hexadecimal(select)
                for X in range(pasos):
                    gametable[fila][columna] = "X"
                    if direction == "W": 
                        if fila > 0:
                            fila -= 1
                    elif direction == "S": 
                        if fila < ancho - 1:
                            fila += 1
                    elif direction == "A":  
                        if columna > 0:
                            columna -= 1
                    elif direction == "D":  
                        if columna < largo - 1:
                            columna += 1
                    if gametable[fila][columna] == "!":
                        print("¡Has chocado con un guardia! Juego terminado.")
                        flag[0] = False
                        break   
                    elif gametable[fila][columna] == "*":
                        print("¡Has llegado al objetivo! Iniciando hackeo... ")
                        hack_num = random.randint(0,500)
                        #Aquí hay que meter la conversion de cambio de base de decimal a hexadecimal
                        print("Para poder finalizar el juego, debes escribir el siguiente número en decimal: ") # + Y aqui iria el valor que retorna la funcion
                        #Esto por ahora.
                        flag[0] = False
                        break 

                if not flag[0]:  
                    break 
                print("Te has movido: " + str(pasos) + " pasos!")
                gametable[fila][columna] = "S"
                break
            else:
                print("Error: La entrada no es un número hexadecimal válido, intentelo denuevo.")
        
        
