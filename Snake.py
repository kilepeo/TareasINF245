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
hexadecimal = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","F"]
gametable = [["X"] * largo for i in range(ancho)] 
fila = 5
columna =  0
gametable[fila][columna] = "S"
fila_asterisco = random.randint(0, ancho - 1)
gametable[fila_asterisco][-1] = "*"

if guardias != 0:
    functions.guards(gametable, guardias, largo)

while flag:
    text.imprimir_matriz(gametable)
    text.movements()
    if largo <=20:
        direction = input().upper()
        text.short_gametable(direction,flag) #Aquí es donde te digo que queria modificarla y sin las listas no me dejaba y bno en las otras también
        while True:
            select = input()
            if all(character in binario for character in select):  #Esto por si acaso, es para ver si el texto ingresado está dentro de las listas de binario, 
                functions.binary(select)                           #Octadecimal o exadecimal que estan allí arribita definidaas antes de la gametable
                break
            else:
                print("Error: La entrada no es un número binario válido, intentelo denuevo.")
    elif largo <=100:
        direction = input().upper()
        text.medium_gametable(direction,flag)
        while True:
            select = input()
            if all(character in octadecimal for character in select):  
                functions.octadecimal(select) 
                break
            else:
                print("Error: La entrada no es un número octadecimal válido, intentelo denuevo.")
    else:
        direction = input().upper()
        text.large_gametable(direction,flag)
        while True:
            select = input()
            if all(character in hexadecimal for character in select):  
                functions.hexadecimal(select) 
                break
            else:
                print("Error: La entrada no es un número hexadecimal válido, intentelo denuevo.")
        
        
