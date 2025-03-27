import random

#Esta funcion genera guardias dependiendo de la cantidad de guardias y la tabla, se le pasa la tabla para que pueda modificar la matriz y el largo para que pueda 
#acceder del 0 hasta la ultima columna, porque filas siempre serán 11
def guards(gametable, guardias, largo):
    i = 0
    while i != guardias:
        fila_guardias = random.randint(0, 10)
        columna_guardias = random.randint(0, largo - 1)
        if gametable[fila_guardias][columna_guardias] == "X":
            gametable[fila_guardias][columna_guardias] = "!"
            i+=1

#De binario a decimal. se le saca el tamaño del string - 1 y se parte por la izquierda a derecha, el numero * 2 elevado al tamaño, se va reduciendo el tamaño y el total
#Acomula todo lo que es el binario
def binary(select):
    size = len(select)-1
    total = 0
    for number in select:
       total += int(number) * (2**size)
       size -=1
    return total

#De octadecimal a decimal, la misma wea pero trabajas con base 8
def octadecimal(select):
    size = len(select)-1
    total = 0
    for number in select:
        total += int(number) * (8**size)
        size -=1
    return total

#Aquí no me juzgues, no se me ocurrio otra forma que poner millones de elifs, si sabes otra forma PORFAVOR OPTIMIZA ESTA ASQUEROSIDAD, se ve horrendo
#Pero basicamente cuando es las letras, las convierte altiro a decimal con un auxiliar y las multiplica por 16 y el tamaño que lo sacamos como antes
#Tambien se podia trabajar como binario pero según yo esto es más facil.    
def hexadecimal(select):
    size = len(select)-1
    total = 0
    for number in select:
        if number not in ["A", "B", "C", "D", "E", "F"]:
            total += int(number) * (16**size)
        elif number == "A":
            aux = 10
            total += aux * (16**size)
        elif number == "B":
            aux = 11
            total += aux * (16**size)            
        elif number == "C":
            aux = 12
            total += aux * (16**size)
        elif number == "D":
            aux = 13
            total += aux * (16**size)
        elif number == "E":
            aux = 14
            total += aux * (16**size)
        elif number == "F":
            aux = 15
            total += aux * (16**size)
        size -= 1
    return total


#decimal_to_binary(hack_num)
#decimal_to_octadecimal(hack_num)
#decimal_to_hexadecimal(hack_num)