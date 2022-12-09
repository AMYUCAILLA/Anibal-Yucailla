"""
Descripción:
Simula los juegos tradicionales adaptando sus condiciones y sus estados
estrictamente bajo el uso de condicionales de lógica proposicional. Los juegos seleccionados son Limbo,
El baile de las sillas y Busqueda de pareja.

Autores:
Christopher Amek Bazurto Mora
Erick Sebastian Mora Lara
Anibal Martin Yucailla Padilla

Verisión:
VER.1.1.0
"""
import numpy as np
import random as rd
import time
import os


def menuInicial(juegos):
    """
    Es un procedimiento con un bucle for que recorre los elementos del diccionario
    descrito por cada uno de los juegos Tradicionales, mediante la funcion sorted
    se logra que los ekementos se muestren en el orden propuesto:
    ------------
        Recibe un diccionario (juegos) como parametro
    
    Retorna:
    ------------
        No retorna ningun valor
    """
    print("------------------------------------------\n")
    print("                  BIENVENIDOS              \n")
    print("                TRADITIONAL GAMES         \n")
    print("------------------------------------------\n")
    for clave in sorted(juegos):
        print(f' {clave}) {juegos[clave][0]}')

def eleccion(juegos):
    """
    Es un procedimiento que valida el ingreso de datos en el menu de seleccion
    Se ha validado los numeros del 1 al 4 donde (1-3) corresponde a las opciones
    de juegos y (4) corresponde a salida del programa. Para un valor ajeno se 
    mostrara un mensaje de validacion:
    ------------
        Recibe un diccionario (juegos) como parametro
    
    Retorna:
    ------------
        Retorna una variable (a) de tipo char que indica el valor de entrada escrito por el usuario
    """
    while(a := input('Ingrese el juego: ')) not in juegos:
        print("-----------------------------------------------------------\n")
        print("\nEl juego no esta en la lista \n")
        print("Por favor ingre valores entre 1-3 para seleccionar un juego \n")
        print("-----------------------------------------------------------\n")
    return a

def elegir(juego, juegos):
    """
    Es un procedimiento que recibe una opcion del menu de juegos escrita por el usuario
    en pantalla y ejecuta la opcion elegida correspondiente al diccionario de opciones:
    ------------
        Recibe la opcion seleccionada (juego) y el diccionario (juegos) como parametros
    
    Retorna:
    ------------
        No retorna ningun valor
    """
    juegos[juego][1]()

def generarMenu(juegos, juego_elegido):
    """
    Es un procedimiento que encapsula 3 funciones definidas anteriormente y las ejecuta
    primero muetra el menu en pantalla, luego lee la opcion escrita por el usuario y la valida
    y por ultimo ejecuta la opcion relacionada a la entrada:
    ------------
        Recibe el diccionario (juegos) y la seleccion (juego_elegido) como parametros
    
    Retorna:
    ------------
        No retorna ningun valor
    """
    juego = None
    while juego != juego_elegido:
        menuInicial(juegos)
        juego = eleccion(juegos)
        elegir(juego, juegos)
        print()       

def menuPrincipal():
    """
    Es un procedimiento en el que se define el diccionario con las opciones de los diferentes juegos,
    se han definido 3 opciones y una adicional para salir del programa:
    ------------
        No tiene parametros de entrada
    
    Retorna:
    ------------
        No retorna ningun valor
    """
    juegos = {
        '1' : ("Juego 1: LIMBO", juego1),
        '2' : ("Juego 2: JUEGO DE LAS SILLAS", juego2),
        '3' : ("Juego 3: BUSQUEA DE PAREJAS", juego3),
        '4' : ("Salir", salir)
    }

    generarMenu(juegos, '4')

def salir():
    print("Saliendo")
        
##########################################################################################################
#Funcions para el juego 1 Limbo
##########################################################################################################

def finDeJuego():
    """
    Es un procedimiento que nos muestra una impresión correspondiente al perder el juego
    Parametros:
    ------------
        No tiene parametros de entrada
    
    Retorna:
    ------------
        No retorna ningun valor
    """
    print("\n")
    print("*************************************\n")
    print("||         FIN DEL JUEGO       ||\n")
    print("||           PERDISTE          ||\n")
    print("||                             ||\n")
    print("||                             ||\n")
    print("||             :C              ||\n")
    print("||                             ||\n")
    print("||                             ||\n")
    print("||                             ||\n")
    print("||                             ||\n")
    print("||                             ||\n")
    print("*************************************\n")
    print("\n")


def nivelUno():
    """
    Es un procedimiento que nos muestra una impresión correspondiente al primer nivel del juego limbo
    Parametros:
    ------------
        No tiene parametros de entrada
    
    Retorna:
    ------------
        No retorna ningun valor
    """
    print("\n")
    print("*************************************\n")
    print("||=============================||\n")
    print("||                 __          ||\n")
    print("||                |  |         ||\n")
    print("||                |__|         ||\n")
    print("||               /             ||\n")
    print("||        |_____/              ||\n")
    print("||        _____/               ||\n")
    print("||       |    |                ||\n")
    print("||       |    |                ||\n")
    print("||     __|    |__              ||\n")
    print("*************************************\n")
    print("\n")

def nivelDos():
    """
    Es un procedimiento que nos muestra una impresión correspondiente al segundo nivel del juego limbo
    Parametros:
    ------------
        No tiene parametros de entrada
    
    Retorna:
    ------------
        No retorna ningun valor
    """
    print("\n")
    print("*************************************\n")
    print("||                             ||\n")
    print("||                             ||\n")
    print("||                             ||\n")
    print("||=============================||\n")
    print("||                 __ ___      ||\n")
    print("||         |______/  |___|     ||\n")
    print("||          _____/             ||\n")
    print("||         /    /              ||\n")
    print("||        /    /               ||\n")
    print("||     __|    |__              ||\n")
    print("*************************************\n")
    print("\n")

def nivelTres():
    """
    Es un procedimiento que nos muestra una impresión correspondiente al tercer nivel del juego limbo
    Parametros:
    ------------
        No tiene parametros de entrada
    
    Retorna:
    ------------
        No retorna ningun valor
    """
    print("\n")
    print("*************************************\n")
    print("||                             ||\n")
    print("||                             ||\n")
    print("||                             ||\n")
    print("||                             ||\n")
    print("||                             ||\n")
    print("||                             ||\n")
    print("||=============================||\n")
    print("||           \___________      ||\n")
    print("||        ______|   |____|     ||\n")
    print("||     __|   __|               ||\n")
    print("*************************************\n")
    print("\n")

def reglas():
    """
    Es un procedimiento que nos muestra una impresión correspondiente a las reglas del juego
    Parametros:
    ------------
        No tiene parametros de entrada
    
    Retorna:
    ------------
        No retorna ningun valor
    """
    print("_______________________________________________________________\n")
    print("Este juego contara de 3 preguntas, referenciando a 3 niveles,\n")
    print("si respones una pregunta bien podras pasar la barra del limbo\n")
    print("en caso de que falles una perderas.\n")
    print("_______________________________________________________________\n")

def validador(num):
    """
    Es un procedimiento que nos determina si un dato ingresado(numero) es un digito
    si lo es retorna un True(Verdadero) en caso de que no lo sea retorna un False(Falso)
    Parametros:
    ------------
        Tiene  un parametro de entrada (num)
    
    Retorna:
    ------------
        Retorna el valor de True si es el dato ingresado es un digito y false si no lo es
    """
    numeroValido = False
    if num.isdigit():
        numeroValido = True
        return numeroValido
    else:
        return numeroValido

        

def perteneceFibonacci(num1):
    """
    Es un procedimiento que nos permite determinar si un numero pertenece a la serie de Fibonacci
    Parametros:
    ------------
        Tiene parametros de entrada, num1 (Es numero que se quiere saber si pertenece a la serie de Fibonacci)
    
    Retorna:
    ------------
        si retorna un valor, esFibonacci (Si el numero pertenece es True, caso contrario False)
    """
    #Inicializa valores, a = 0 y b =1, para iniciar la serie de Fibonacci
    a, b = 0,1
    #Inicializa la variable n = 100, representando el limite de la serie
    n=100
    #Inicializa la variable  esFibonacci=False
    esFibonacci=False
    #Inicio del bucle, serie de Fibonacci
    while a < n:
        #Asigna valores de a = b y b=a+b
        a, b = b, a+b
        #Si a es igual al numero ingresado (num1) entoces
        if a == num1:
            #Se asigana a esFibonacci=True, el numero ingresa si pertenece a la serie
            esFibonacci=True
            #Retorna el valor de esFibonacci
            return esFibonacci
    #Retorna el valor de esFibonacci
    return esFibonacci

##########################################################################################################
#Funcions para el juego 2 Juego de las Sillas
##########################################################################################################
def ingresarNombres(participantes):
    """
    Funcion para guardar los nombres de los participantes en una lista/vector
    de acuerdo al numero de jugadores dado, cada nombre se va adicionando 
    con iteracion de un ciclo for y en la posicion final disponible del vector.

    Parametros:
    ------------
        Recibe como parametro el numero ingresado de participantes del juego (participantes)
    
    Retorna:
    ------------
        Retorna un vector/lista que contiene los nombres de los participantes (listaParticipantes)
    """
    listaJugadores = []
    #Se inicializa una lista Vacia, para posteriormente almacenar los nombres de los jugadores
    #Ciclo repetitivo For para solicitar el ingreso de Nombres de Jugadores 
    for x in range(participantes):
        #El ciclo esta controlado por el numero de jugadores (participantes) Ingresado anteriormente
        print("Ingrese Nombre del Jugador ",x+1, " :")
        nombre = str(input('')) #En cada iteracion se solicita un nombre de Jugador
        #Cada Nombre se va almacenando en la Lista vacia inicializada 
        listaJugadores.append(nombre) #Va almacenando los nombres en la ultima posicion libre 
        
    print("Empieza la Ronda con los siguientes jugadores: \n")
    print(listaJugadores)
    #Se muestra en pantalla la Lista con los participantes de la ronda
    return listaJugadores #retornamos la lista para usarla en la funcion que desarolla el juego

def juegoSillas(participantes,sillas):
    """
   Funcion donde se desarrollara toda la interaccion del juego de las sillas
   se operara con la lista de participantes y se lor ira eliminando hasta que 
   quede un unico participante en la lista, que sera el ganador

   Parametros:
    ------------
        Recibe dos parametros: El numero de participantes (participantes) y el numero de sillas que se usaran(sillas)
    
    Retorna:
    ------------
        No retorna ningun valor
    """
    
    turnos=0 #inicializamos una variable turnos para cada iteracion del juego
    listaJugadores = ingresarNombres(participantes) 
    #llamamos a la funcion ingresarNombres() para que realice su proceso y nos retorne la lista de participantes
    #Inicializamos un ciclo if para cuando el numero de sillas sea mayor que 0
    if (sillas>0):
        for x in range(participantes-1): #Restamos en 1 la longuitud del vector porque la condicion del juego es que debe quedar un ganador
            #por tanto tambien debe quedar un elemento en el vector
            turnos+=1 #en cada iteracion avanzara un turno
            #Mensajes de interaccion por turnos
            input("Presiona cualquier tecla para continuar..")
            print("Empieza el Turno ",turnos)
            print("Suena La Musica...")
            time.sleep(3)
            print("Se detiene la Musica...")
            #Utilizando la funcion choice de la biblioteca random se selecciona un elemento al azar de la lista de jugadores
            azar = rd.choice(listaJugadores)
            time.sleep(2)
            #dicho elemento elegido o jugador elegido sera el descalificado en ese turno
            print(azar, " Se ha quedado sin silla, es descalificado") #mensaje de Descalificado
            listaJugadores.remove(azar) #se remueve el elemento del vector utilizando su valor en string
            print("Se quita una silla...")
            sillas-=1 #Se resta una silla por cada turno 
            time.sleep(2)
            print("Participantes restantes: ",len(listaJugadores), ' ', listaJugadores) 
            print("Sillas restantes: ",sillas) 
            #Se imprime por pantalla el numero de jugadores y sillas restantes
            #Tambien se imprimira el status de la Lista para observar como varia en cada turno

    #Ciclo if que se cumple cuando el valor de las sillas alcanza su valor de 0
    if (sillas == 0):
        print("____________________")
        print("Juego Terminado") #Cuando las sillas llegan a 0 significa que se termino el juego
        #Por tanto se muestra al ganador de la ronda
        print("EL GANADOR ES: ", listaJugadores) #El participante que quede en la lista gana

##########################################################################################################
#Funciones para el juego 3 BUSQUEDA DE PAREJA
##########################################################################################################

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
        f1 = int(rd.random()*n)+0
        #c1 es la posición en la Columna, del primer valor a asignarse aleatoriamente (menor o igual a n) por el programa. 
        c1 = int(rd.random()*n)+0
        #Para evitar que 2 números caigan en una misma casilla-posición, validamos que:
        #El tablero en las posiciones f1 y c1, no esten ocupados es decir que no sean iguales a cero.
        #indicando así que no podemos escribir hasta que se encuentre una casilla vacía. 
        while not(tablero[f1,c1]==0):
        #se repite la asignación del primer valor aleatoriamente en f1, debido a que se cumple la condición de no estar ocupado.    
            f1 = int(rd.random()*n)+0
        #se repite la asignación del primer valor aleatoriamente en c1, debido a que se cumple la condición de no estar ocupado.    
            c1 = int(rd.random()*n)+0
        #establecemos que el valor asignado i, se guardara en la posición fila 1 y columna 1    
        tablero[f1,c1] = i
        #f2 es la posición en la fila, del primer valor a asignarse aleatoriamente (menor o igual a n) por el programa. 
        f2 = int(rd.random()*n)+0
        #c2 es la posición en la Columna, del primer valor a asignarse aleatoriamente (menor o igual a n) por el programa. 
        c2 = int(rd.random()*n)+0
        #Como en el paso anterior para evitar que los siguientes números,caigan en una misma casilla-posición, validamos que:
        #El tablero en las posiciones f2 y c2, no esten ocupados es decir que no sean iguales a cero.
        #indicando así que no podemos escribir hasta que se encuentre una casilla vacía.
        while not(tablero[f2,c2]==0):
        #se repite la asignación del segundo valor aleatoriamente en f2, debido a que se cumple la condición de no estar ocupado.    
            f2 = int(rd.random()*n)+0
        #se repite la asignación del primer valor aleatoriamente en c2, debido a que se cumple la condición de no estar ocupado.    
            c2 = int(rd.random()*n)+0
        #establecemos que el valor asignado i, se guardara (escribira) en la posición fila 2 y columna 2    
        tablero[f2,c2] = i
    #para continuar llenando toda las casillas, luego de que i se lleo en f1, f2
    #con la siguiente casilla hasta completar todas o que i sea menor o igual al número de las casillas.
        i = i + 1
    #como resultado de todo el proceso se debe devolver la matriz(tablero), 
    # Cada casilla con sus valores respectivos.
    return(tablero)


def rangoNumero(num):
    """
    Es un procedimiento que nos determina si un dato ingresado(numero) esta en rango [0-3]
    si lo esta retorna un True(Verdadero) en caso de que no lo sea retorna un False(Falso)
    Parametros:
    ------------
        Tiene  un parametro de entrada (num)
    
    Retorna:
    ------------
        Retorna el valor de True si es el dato ingresado esta dentro del rango [0-3],
        o un False si no lo esta
    """
    #inicializa validadorRangoNumero en falso
    validadorRangoNumero = False
    #Si el numero ingresado esta entre [0-3] entonces
    if (num < 4) and (num >= 0) :
        #asigna validadorRangoNumero en True
        validadorRangoNumero = True
        #retorna validadorRangoNumero
        return  validadorRangoNumero
    else:
        # si no cumple retorna validadorRangoNumero
        return validadorRangoNumero


#JUEGOS
def juego1():
    """
    Es un procedimiento que ejecuta el juego 1: Limbo
    Parametros:
    ------------
        No tiene parametros de entrada
    
    Retorna:
    ------------
        No retorna ningun valor
    """
    print("------------------------\n")
    print("Juego 1: Limbo. Escogido")
    print("------------------------\n")
    #Imprime inicio del juego
    print("------------------------------------------\n")
    print("                  BIENVENIDO              \n")
    print("                JUEGO DEL LIMBO           \n")
    print("------------------------------------------\n")
    #Imprime las reglas del juego
    reglas()
    #Imprime mensaje de ingreso de nombre del jugador y asigna el nombre a nombreJugador
    nombreJugador = input("Por favor ingrese su Nickname: ")
    #Imprime mensaje del primer nivel del limbo
    print("---------------------------------------------\n")
    print("\nNivel 1: Ingrese 2 numeros pares diferentes\n")
    print("---------------------------------------------\n")
    pasoPrimernivel = False
    pasoSegundonivel = False
    pasoTercernivel = False
    while True:
        #Imprime mensaje de ingreso del primer numero y asigna el numero a primerNumero
        primerNumero = input("Por favor ingrese el primer numero: ")
        #Valida que el primer numero sea un numero entero postivo
        if validador(primerNumero) == True:
            #Combierte el dato entrado a Integer(Entero) y lo asigna a primerNumero
         primerNumero=int(primerNumero)
         break
        else:
            #Imprime mensaje de error en ingreso de datos
            print("--------------------------------------------------------------\n")
            print("                              ERROR                           \n")
            print("El dato ingresado no es un numero entero positivo, intente de nuevo.\n")
            print("--------------------------------------------------------------\n")
    while True:
        #Imprime mensaje de ingreso del segundo numero y asigna el numero a segundoNumero
        segundoNumero = input("Por favor ingrese el segundo numero: ")
        #Valida que el segundo numero sea un numero entero postivo
        if validador(segundoNumero) == True:
            #Combierte el dato entrado a Integer(Entero) y lo asigna a segundoNumero
            segundoNumero=int(segundoNumero)
            break
        else:
            #Imprime mensaje de error en ingreso de datos
            print("--------------------------------------------------------------\n")
            print("                              ERROR                           \n")
            print("El dato ingresado no es un numero entero positivo, intente de nuevo.\n")
            print("--------------------------------------------------------------\n")
    #Si los dos numeros ingresados son pares y no se repiten entonces
    if (primerNumero % 2 == 0) and (segundoNumero % 2 == 0) and (primerNumero != segundoNumero):
        #Imprime que se paso el nivel uno
        nivelUno()
        #Asigna pase de nivel 1 a verdero
        pasoPrimernivel = True
    else:
        #Imprime el fin del juego
        finDeJuego()
    #Si paso el primer nivel entonces
    if(pasoPrimernivel == True):
        #Imprime mensaje del segundo nivel del limbo
        print("--------------------------------------------------------------\n")
        print("Nivel 2: Ingrese 2 numeros de la serie de fibonacci diferentes\n")
        print("--------------------------------------------------------------\n")
        while True:
            #Imprime mensaje de ingreso del primer numero y asigna el numero a primerNumero
            primerNumero = input("Por favor ingrese el primer numero: ")
            #Valida que el primer numero sea un numero entero postivo
            if validador(primerNumero) == True:
                #Combierte el dato entrado a Integer(Entero) y lo asigna a primerNumero
                primerNumero=int(primerNumero)
                break
            else:
                #Imprime mensaje de error en ingreso de datos
                print("--------------------------------------------------------------\n")
                print("                              ERROR                           \n")
                print("El dato ingresado no es un numero entero positivo, intente de nuevo.\n")
                print("--------------------------------------------------------------\n")
        while True:
            #Imprime mensaje de ingreso del segundo numero y asigna el numero a segundoNumero
            segundoNumero = input("Por favor ingrese el segundo numero: ")
            #Valida que el segundo numero sea un numero entero postivo
            if validador(segundoNumero) == True:
                #Combierte el dato entrado a Integer(Entero) y lo asigna a segundoNumero
                segundoNumero=int(segundoNumero)
                break
            else:
                #Imprime mensaje de error en ingreso de datos
                print("--------------------------------------------------------------\n")
                print("                              ERROR                           \n")
                print("El dato ingresado no es un numero entero positivo, intente de nuevo.\n")
                print("--------------------------------------------------------------\n")
    #si los dos nuemeros son diferentes y pertencen a la serie entonces
    if (pasoPrimernivel == True) and (perteneceFibonacci(primerNumero)==True)and (perteneceFibonacci(segundoNumero)==True) and (primerNumero != segundoNumero):
        #Imprime que se paso el nivel dos
        nivelDos()
        #Asigna pase de nivel 2 a verdero
        pasoSegundonivel = True
    elif (pasoPrimernivel == True) and (pasoPrimernivel == False):
        #Imprime el fin del juego
        finDeJuego()

    #si paso el segundo nivel entonces
    if(pasoSegundonivel == True):
        #Imprime mensaje del tercer nivel del limbo
        print("-------------------------------------------------------------------------------\n")
        print("Nivel 3: Ingrese 2 numeros de la serie de fibonacci que sean pares y diferentes\n")
        print("-------------------------------------------------------------------------------\n")
        while True:
            #Imprime mensaje de ingreso del primer numero y asigna el numero a primerNumero
            primerNumero = input("Por favor ingrese el primer numero: ")
            #Valida que el primer numero sea un numero entero postivo
            if validador(primerNumero) == True:
                #Combierte el dato entrado a Integer(Entero) y lo asigna a primerNumero
                primerNumero=int(primerNumero)
                break
            else:
                #Imprime mensaje de error en ingreso de datos
                print("--------------------------------------------------------------\n")
                print("                              ERROR                           \n")
                print("El dato ingresado no es un numero entero positivo, intente de nuevo.\n")
                print("--------------------------------------------------------------\n")
        while True:
            #Imprime mensaje de ingreso del segundo numero y asigna el numero a segundoNumero
            segundoNumero = input("Por favor ingrese el segundo numero: ")
            #Valida que el segundo numero sea un numero entero postivo
            if validador(segundoNumero) == True:
                #Combierte el dato entrado a Integer(Entero) y lo asigna a segundoNumero
                segundoNumero=int(segundoNumero)
                break
            else:
                #Imprime mensaje de error en ingreso de datos
                print("--------------------------------------------------------------\n")
                print("                              ERROR                           \n")
                print("El dato ingresado no es un numero entero positivo, intente de nuevo.\n")
                print("--------------------------------------------------------------\n")
            #si los dos numeros ingresados son diferentes y pares y pertencen a la serie de fibonacci entonces
        if(pasoSegundonivel == True) and (perteneceFibonacci(primerNumero)==True) and (perteneceFibonacci(segundoNumero)==True) and (primerNumero % 2 == 0) and (segundoNumero % 2 == 0) and (primerNumero != segundoNumero):
            #Imprime que se paso el nivel tres
            nivelTres()
            #Asigna pase de nivel 3 a verdero
            pasoTercernivel = True
            #Imprime mensaje de ganar el juego
            print("------------------------------------------\n")
            print("                  FELICIDADES             \n")
            print("          GANASTE " + nombreJugador +" \n")
            print("             EL JUEGO DEL LIMBO           \n")
            print("------------------------------------------\n")
        else:
            #Imprime el fin del juego
            finDeJuego()
        
    #desarollar Juego 2    

def juego2():
    """
    Es un procedimiento que ejecuta el juego 2: Juego de las Sillas
    Parametros:
    ------------
        No tiene parametros de entrada
    
    Retorna:
    ------------
        No retorna ningun valor
    """
    print("------------------------\n")
    print("Juego 2: Juego de Las Sillas. Escogido")
    print("------------------------\n")
    #desarollar Juego 2
    #Declaramos dos variables globales indispensables para desarollar el juego
    #Numero de participantes y numero de sillas
    #Mensaje de Bienvenida y primera indicacion
    print("***BIENVENIDO AL JUEGO DE LAS SILLAS***")
    print("--Para poder jugar se necesitan 2 o mas participantes--")
    """A continuacion se propone un control de ingreso de datos, definido
    por un bucle (While True) y un manejo de excepciones, el ciclo solo se 
    terminara cuando se cumpla la condicion de que el numero
    de participantes ingresados sea un entero y sea mayor que 1
    """
    while True:
        try:
            participantes = int(input("Ingrese el numero de participantes: "))
        except ValueError:
            print("Solo Enteros")
            continue
        if participantes<=1:
            print("Debe haber mas de un jugador")
            continue
        else:
            break       
    #Por regla del juego el numero de sillas corresponde al numero de participantes -1
    sillas = participantes-1
    print("El juego empieza con ",participantes," participantes")
    print("Sillas en juego: " ,sillas)
    #Mensaje de numero de participantes y Sillas
    #ingresarNombres(participantes)
    juegoSillas(participantes, sillas)
 

  
 #Llamado a la funcion que desarolla el juego
 #desarollar Juego 3
 
def juego3():
  
  
    """
    Es un procedimiento que ejecuta el juego 3: Juego de Busqueda de pareja
    Parametros:
    ------------
        No tiene parametros de entrada
    
    Retorna:
    ------------
        No retorna ningun valor
    """
    print("Juego 3: Busqueda de Pareja. Escogido")    
    
    #Definimos el tamaño del tablero que es de 4 (n=4)
    n = 4
    # PROCEDIMIENTO
    #Para generar el tablero-Matriz llamamos a la función "tableroparejas"
    tablero = tableroparejas(n)
    #Iniciamos el juego con el siguiente mensaje
    print("\n BIENVENIDO VEAMOS COMO ESTA TU MENTE, MEMORIZA LAS POSICIONES PARA JUGAR")
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
        #Generamos un while para validar datos de entrada de l ficha 1 
        while True:
            #Establecemos que el programa intente leer el dato f1, en caso de que no lo consiga
            #ejecutará, lo que hay en el except
            try:
                # Solicitamos que se ingrese la posición en la fila(0 a 3) de la ficha 1.
                f1 = int(input('ingresa la fila de la  ficha 1:'))
                #en caso de que con try al intentar leer f1, no fue exitoso, se verifica cuál es el error.
            except (ValueError,NameError):
                #dado el caso de que se ingreso caracteres y no números se pide que ingrese un número
                print("Ingrese un número")
                #en caso de que si sea un número se continua al siguiente apartado.
                continue
        #establecemos un condicional e invocamos a la función "rangoNumero", para 
        #establecer que si "f1" es verdadero es decir un número menor a 4, como se planteao en la función.
            if rangoNumero(f1)== True:

                break
        #caso contrario  
            else:
        #si el númeroñ es mayor a 4, se imprime que "la fila debe ser entre 0 y 3"  
                print("La fila debe ser entre 0 y 3")
                
        # resuelto la validación de datos, continuamos con la ejecución del programa.  

        #Generamos un while para validar datos de entrada de la ficha 2
        while True:
            #Establecemos que el programa intente leer el dato f1, en caso de que no lo consiga
            #ejecutará, lo que hay en el except
            try:
                # Solicitamos que se ingrese la posición en la fila(0 a 3) de la ficha 2.
                c1 = int(input('ingresa la columna de la ficha 1 :'))
                #en caso de que con try al intentar leer f1, no fue exitoso, se verifica cuál es el error.
            except (ValueError, NameError):
                #dado el caso de que se ingreso caracteres y no números se pide que ingrese un número
                print("Ingrese un número")
                #en caso de que si sea un número se continua al siguiente apartado.
                continue
            #establecemos un condicional e invocamos a la función "rangoNumero", para 
            #establecer que si "f1" es verdadero es decir un número menor a 4, como se planteao en la función.
            if rangoNumero(c1)==True:    
                break 
                #caso contrario  
            else:
                #si el número es mayor a 4, se imprime que "la fila debe ser entre 0 y 3"  
                print("La columna debe ser entre 0 y 3")
                # resuelto la validación de datos, continuamos con la ejecución del programa.    
                continue
        #hacemos un salto al proximo paso del programa.

    
        #Para evitar que el jugador ingrese posiciones de fichas descubiertas establecemos que:
        #Podremos ingresar posiciones, mientras esas posiciones no sean aún descubiertas.
        #Si el jugador ingresa las mismas posiciones , el programa seguirá pidinedo coordenadas de la misma ficha.
        while not(descubiertas[f1,c1]==0):
            #si se ingresa posiciones ya descubiertas se imprime el siguiente mensaje
            print('Esta ficha ya fue descubierta INGRESA OTRAS COORDENADAS')
            #Dado que se cumple la condición, solicitamos que se ingrese la fila de la ficha 1.
            f1 = int(input('fila ficha 1:'))
            #Dado que se cumple la condición, solicitamos que se ingrese la columna de la ficha 1.
            c1 = int(input('columna ficha 1:'))
            
        #Generamos un while para validar datos de entrada de la fila 2 de la ficha 2 
        while True:
            #Establecemos que el programa intente leer el dato f2, en caso de que no lo consiga
            #ejecutará, lo que hay en el except
            try:
                # Solicitamos que se ingrese la posición en la fila(0 a 3) de la ficha 2.
                f2 = int(input('ingresa la fila de la  ficha 2:'))
                #en caso de que con try al intentar leer f2, no fue exitoso, se verifica cuál es el error. 
            except (ValueError,NameError):
                #dado el caso de que se ingreso caracteres y no números se pide que ingrese un número    
                print("Ingrese un número")
                #en caso de que si sea un número se continua al siguiente apartado.  
                continue
            #establecemos un condicional e invocamos a la función "rangoNumero", para 
            #establecer que si "f2" es verdadero es decir un número menor a 4, como se planteao en la función.
            if rangoNumero(f2)== True:
                break
            #caso contrario      
            else:
                #si el número es mayor a 4, se imprime que "la fila debe ser entre 0 y 3" 
                print("La fila debe ser entre 0 y 3")
                # resuelto la validación de datos, continuamos con la ejecución del programa.   
        #Generamos un while para validar datos de entrada de la columna de la ficha 2    
        while True:
            #Establecemos que el programa intente leer el dato c2, en caso de que no lo consiga
            #ejecutará, lo que hay en el except
            try:
                # Solicitamos que se ingrese la posición en la columna(0 a 3) de la ficha 1.
                c2 = int(input('ingresa la columna de la ficha 2 :'))
                #en caso de que con try al intentar leer f1, no fue exitoso, se verifica cuál es el error.  
            except (ValueError, NameError):
                #dado el caso de que se ingreso caracteres y no números se pide que ingrese un número     
                print("Ingrese un número")
            #en caso de que si sea un número se continua al siguiente apartado.  
                continue
            #establecemos un condicional e invocamos a la función "rangoNumero", para 
            #establecer que si "c1" es verdadero es decir un número menor a 4, como se planteao en la función.
            if rangoNumero(c2)==True:
                break 
                #caso contrario   
            else:
                #si el número es mayor a 4, se imprime que "la columna debe ser entre 0 y 3" 
                print("La columna debe ser entre 0 y 3")
                # resuelto la validación de datos, continuamos con la ejecución del programa.
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
        #  Se registra que se elige la ficha a descubir de la ficha 2 que seria pareja de la ficha 1
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
if __name__ == '__main__':
    #Variables para juego Limbo
    #Inicializa variables paso de nivel correspondiente al nivel, todas en False
    pasoPrimernivel = False
    pasoSegundonivel = False
    pasoTercernivel = False
    nombreJugador = ""
    primerNumero = 0
    segundoNumero = 0
    #Variables para juego de la silla
    participantes = 0 
    sillas = 0
    #Variables para juego Busqueda de pareja
    n=4
    tablero = tableroparejas(n)
    equivocado = 0
    encontrado = 0
    menuPrincipal()
