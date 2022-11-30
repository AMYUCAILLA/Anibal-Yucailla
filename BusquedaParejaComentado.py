"""
************************* BUSQUEDA DE PAREJA *****************************
Busqueda de pareja es un juego que permite eercitar la memoria, puesto que al jugador se le indica:
un cuadro con imagenes, objetos, en este caso números luego de unos segundos se esconde aquel cuadro,
para que el jugador proceda a recordar las ubicaciones y destaparlas, para descubrir si esta en lo correcto 
o esta equivocado.

Autor:
Aníbal Yucailla
"""

#Importamos, Numpy que nos permitira usar arreglos
import numpy as np
#importamos la libreria random para que el programa plantee los números en diferentes posiciones. 
import random as rnd
#El programa se realizó de forma estructurada por lo cual "tablero parejas" será una función que forma parte del programa
def tableroparejas(n):
    
    """
    Es un procedimiento que establece una matriz y asigna las posiciones a cada uno de los elementos(fichas-Valores)
    Parametros:
    ------------
        No tiene parametros de entrada
    
    Retorna:
    ------------
        No retorna ningun valor
    """
    #En este apartado calculamos el número de fichas(casillas), de parejas que se podrán poner en el tablero
    fichasunicas = (n*n)//2
    
    #definimos el tamaño del tablero-Matriz que sera n*n, estará formada por una matriz de ceros 
    #y las fichas a ingresar serán enteros. 
    tablero = np.zeros(shape=(n,n),dtype =int)
    
    #"i", será la ficha a ingresar, la cual tendra una posición de fila y columna
    
    i = 1
      #Establecemos el proceso para que se asignen los valores (números) en las casillas.
    #El proceso se repetira mientras i sea menor o igual a fichasúnicas. 
    while i<=fichasunicas:
        #f1 es la posición en la fila, del primer valor a asignarse aleatoriamente (menor o igual a n) por el programa. 
        f1 = int(rnd.random()*n)+0
        #c1 es la posición en la Columna, del primer valor a asignarse aleatoriamente (menor o igual a n) por el programa. 
        c1 = int(rnd.random()*n)+0
        #Para evitar que 2 números caigan en una misma casilla-posición, validamos que:
        #El tablero en las posiciones f1 y c1, no esten ocupados es decir que no sean iguales a cero.
        #indicando así que no podemos escribir hasta que se encuentre una casilla vacía. 
        while not(tablero[f1,c1]==0):
        #se repite la asignación del primer valor aleatoriamente en f1, debido a que se cumple la condición de no estar ocupado.    
            f1 = int(rnd.random()*n)+0
        #se repite la asignación del primer valor aleatoriamente en c1, debido a que se cumple la condición de no estar ocupado.    
            c1 = int(rnd.random()*n)+0
        #establecemos que el valor asignado i, se guardara en la posición fila 1 y columna 1    
        tablero[f1,c1] = i
        #f2 es la posición en la fila, del primer valor a asignarse aleatoriamente (menor o igual a n) por el programa. 
        f2 = int(rnd.random()*n)+0
        #c2 es la posición en la Columna, del primer valor a asignarse aleatoriamente (menor o igual a n) por el programa. 
        c2 = int(rnd.random()*n)+0
        #Como en el paso anterior para evitar que los siguientes números,caigan en una misma casilla-posición, validamos que:
        #El tablero en las posiciones f2 y c2, no esten ocupados es decir que no sean iguales a cero.
        #indicando así que no podemos escribir hasta que se encuentre una casilla vacía.
        while not(tablero[f2,c2]==0):
        #se repite la asignación del segundo valor aleatoriamente en f2, debido a que se cumple la condición de no estar ocupado.    
            f2 = int(rnd.random()*n)+0
        #se repite la asignación del primer valor aleatoriamente en c2, debido a que se cumple la condición de no estar ocupado.    
            c2 = int(rnd.random()*n)+0
        #establecemos que el valor asignado i, se guardara (escribira) en la posición fila 2 y columna 2    
        tablero[f2,c2] = i
    #para continuar llenando toda las casillas, luego de que i se lleo en f1, f2
    #con la siguiente casilla hasta completar todas o que i sea menor o igual al número de las casillas.
        i = i + 1
    #como resultado de todo el proceso se debe devolver la matriz(tablero), 
    # Cada casilla con sus valores respectivos.
    return(tablero)

# PROGRAMA

# INGRESO
#Definimos el tamaño del tablero que es de 4 (n=4)
n = 4
# PROCEDIMIENTO
#Para generar el tablero-Matriz llamamos a la función "tableroparejas"
tablero = tableroparejas(n)
#Iniciamos el juego con el siguiente mensaje
print('\n BIENVENIDO VEAMOS COMO ESTA TU MENTE, MEMORIZA LAS POSICIONES PARA JUGAR')
#se imprime el tablero con sus las posiciones de las fichas, para que el jugador las memorice
print(tablero)

#Para evitar que el usuario repita el ingreso de las mimas posiciones durante el juego
#Establecemos un tablero donde se reflejará las fichas descubiertas de tamaño n*n
descubiertas = np.zeros(shape=(n,n),dtype=int)
#Inicializamos la variable equivocado,que contará las veces que se equivoca.
equivocado = 0
#Inicializamos la variable encontrado,que contará las cantidad de aciertos.
encontrado = 0
#Para realizar varios intentos de encontrar varias parejas usamos While
#Como el jugador durante todo el juego solo podrá equivocarse 3 veces, establecemos que:
#Se repite los intentos mientras equivocado sea menor a 3 y encontrado sea menor a n*n es decir igual a 16(número de casillas)
while (equivocado<3 and encontrado<(n*n)):
    #Para saber la antidad de descubiertas, imprimimos el siguiente mensaje 
    print('estado del juego:')
    #este tablero dará a conocer las fichas con aciertos descubiertas.
    print(descubiertas)
    # Solicitamos que se ingrese la posición en la fila(0 a 3) de la ficha 1.
    f1 = int(input('ingresa la fila de la  ficha1:'))
   # Solicitamos que se ingrese la posición en la columna(0 a 3) de la ficha 1.
    c1 = int(input('ingresa la columna de la ficha1:'))
    
   #Para evitar que el jugador ingrese posiciones de fichas descubiertas establecemos que:
   #Podremos ingresar posiciones, mientras esas posiciones no sean aún descubiertas.
   #Si el jugador ingresa las mismas posiciones , el programa seguirá pidinedo coordenadas de la misma ficha.
    while not(descubiertas[f1,c1]==0):
        #si se ingresa posiciones ya descubiertas se imprime el siguiente mensaje
        print('Esta ficha ya fue descubierta INGRESA OTRAS COORDENADAS')
        #Dado que se cumple la condición, solicitamos que se ingrese la fila de la ficha 1.
        f1 = int(input('fila ficha1:'))
        #Dado que se cumple la condición, solicitamos que se ingrese la columna de la ficha 1.
        c1 = int(input('columna ficha1:'))
        
   # Solicitamos que se ingrese la posición en la fila(0 a 3) de la ficha 2.
    f2 = int(input('ingresa la fila de la ficha2:'))
    # Solicitamos que se ingrese la posición en la columna(0 a 3) de la ficha 2.
    c2 = int(input('ingresa la columna de la0 ficha2:'))
   #Para evitar que el jugador ingrese posiciones de fichas descubiertas establecemos que:
   #Podremos ingresar posiciones, mientras esas posiciones no sean aún descubiertas.
   #Si el jugador ingresa las mismas posiciones , el programa seguirá pidinedo coordenadas de la misma ficha.
    while not(descubiertas[f2,c2]==0):
       #si se ingresa posiciones ya descubiertas se imprime el siguiente mensaje
        print('Esta ficha ya fue descubierta INGRESA OTRAS COORDENADAS')
        #Dado que se cumple la condición, solicitamos que se ingrese la fila de la ficha 2.
        f2 = int(input('fila ficha2:'))
        #Dado que se cumple la condición, solicitamos que se ingrese la columna de la ficha 2.
        c2 = int(input('columna ficha2:'))
        
    #Se registra que se elige la ficha a descubir de la ficha 1
    ficha1 = tablero[f1,c1]
    #Se registra que se elige la ficha a descubir de la ficha 2 que seria pareja de la ficha 1
    ficha2 = tablero[f2,c2]
    
    #establecemos que si la ficha 1 y ficha 2 descubiertas son iguales. 
    if ficha1==ficha2:
        #Utilizamos el tablero descubiertas, para registrar las fichas acertadas por el jugador con la ficha 1.
        descubiertas[f1,c1] = ficha1
        #Utilizamos el tablero descubiertas, para registrar las fichas acertadas por el jugador con la ficha 2.
        descubiertas[f2,c2] = ficha2
        #Contamos la cantidad de aciertos, todo los aciertos que teniamos mas 2, dado que:
        #Cada acierto conlleva encontrar 2 fichas.
        encontrado = encontrado + 2
        #Se imprime que se encontro una pareja, junto a las fichas descubiertas.
        print('ENCONTRASTE una pareja..!',ficha1,ficha2)
        #Usamos else, dado el caso contrario de que las fichas no sean iguales
        #
    else:  
        #Contamos las veces que se equivoco, donde equivocado anteriormente se establecio que inicia en cero y
        equivocado = equivocado + 1
    #se imprime que las fichas son diferentes,junto a las fichas descubiertas.
        print('Las fichas son diferentes: ',ficha1,ficha2)

# AL FINALIZAR EL JUEGO: 
#Se imprime la solución del juego
print('\n EL JUEGO HA FINALIZADO')
print('Solucion del tablero:')
#Se imprime el tablero jugado
print(tablero)
#Para dar a conocer las fichas descubiertas, se imprime el mensaje:
print('Fichas descubiertas:')
#Se imprime el tablero con las fichas descubiertas
print(descubiertas)
#PAra dar a conocer si se encontro toda las fichas o no establecemos que:
# si encontrado es igual a todo los aciertos
if encontrado==(n*n):
    #se imprime lo sigueinte felicitando.
    print(' Muy bien..!! todas las fichas encontradas')
    #Caso contrario a lo establecido anteeriormente
else:
    #Se imprime lo siguiente:
    print('Perdiste...  agotaste tus oportunidades...')
    # Se imprime tambien las fichas encontradas.
    print('fichas descubiertas:', encontrado)