
def ej1_nombre ():
    """ operadores lógicos en una sola línea:
    NOMBRE sea diferente de cuatro asteriscos “****”
    EDAD sea mayor que 10 y a su vez menor que 18
    Que la longitud de NOMBRE sea mayor o igual a 3 pero a la vez menor que 10
    EDAD multiplicada por 4 sea mayor que 40
    """
    nombre  = input("cual es tu nombre? ")
    edad = int(input("cual es tu edad"))
    (nombre != "****") and (edad > (10) and edad < (18)) and (len (nombre) > 3 and len (nombre) < 10) and (edad * 4 > 40)

def ej2_edades ():
    #edades
    #EDAD MAYOR de 18; menor que 18, erroneas
    edad = int(input ("cual es tu edad?: "))
    if (edad < 18):
        print ("sos un pujui")
    elif (edad >= 18):
        print ("felicidades champ")
    else:
        print ("fecha erronea")

"""
Un curso se ha dividido en dos grupos: A y B de acuerdo al nombre y a una preferencia (Marvel o Capcom). 
El grupo A está formado por fans de Marvel con un nombre anterior a la M y los fans de Capcom con un nombre posterior a la N y el grupo B por el resto. 
Escribir un programa que pregunte al usuario su nombre y preferencia, y muestre por pantalla el grupo que le corresponde.
"""
def tres_grupos ():
    nombre = input("cual es tu nombre?: ")
    team = input ("sos team Marvel o Capcom?: ")

    if ( ( team.title() =="Marvel" and nombre[0].title() < "M" ) or ( team.title() =="Capcom" and nombre[0].title() > "N" ) ):
        print ("sos del grupo A")
    else:
        print ("sos del grupo B")

def lista_tupla ():
    numero = tuple (range (11))
    print (numero)
    print ("Braian sos un puto genio")

"""
Escribir un programa que le pregunte al usuario números hasta que ingrese el 0, 
cuando lo haga mostrar por pantalla la suma de todos los números ingresados.
Nota: Para preguntarle al usuario, recuerda usar input

numero = int ( input ( "escrivi numeros hasta que sea 0" ) )
while numero != 0:
"""
def ejn_1 ():
    numero_1 = int(input("elija el primer numero: "))
    numero_2 = int(input("elija el segundo numero: "))
    operacion = input ("elija la operacion entre +, - , * o salir:")

    if (operacion == "+" or operacion == "suma"):
        print (f"la suma de los numeros es {numero_1 + numero_2}")
    elif (operacion == "-" or operacion == "resta"):
        print (f"la resta de los numeros es {numero_1 - numero_2}")
    elif (operacion == "*" or operacion == "multiplicacion"):
        print (f"la multiplicacion de los numeros es {numero_1 * numero_2}")
    elif (operacion == "salir"):
        close
    else:
        print ("no es ninguna de las operaciones mencionadas")

def ejn_2 ():
    numero = int( input ("escribi un numero: ") )
    numero_2= numero % 2
    while (numero_2 == 0):
        numero = int( input ("escribi otro numero: ") )
        numero_2 = numero % 2
    if (numero_2 == 1):
        print (f"el numero {numero} es inpar")

def ejn_3 ():
    numeros100 = sum (list ( range(0, 101) [1::2] ))

    print (numeros100)

def ejn_4 ():
    numeros_list = []
    cant_de_numeros = int(input("Cuantos numeros queres ingresar?: "))
    intento = 0
    while (intento < cant_de_numeros):
        numeros_list.append (int ( input ( "escrivi tus numeros: " )))
        intento += 1 

    print (f"la media de tus numeros es {(sum (numeros_list))/cant_de_numeros}")
    
def ejn_5 ():
    numeros = [1, 3, 6, 9]

    numeros_int = int(input("introdusca numeros del 0 al 9: "))
    while (numeros_int < 0 or numeros_int >= 10):
        numeros_int = int(input("introdusca numeros del 0 al 9: "))

    print ("correcto")
    if numeros_int in numeros:
        print ("esta en la lista")

def ejn_6 ():
    lista_1 = list (range (1 , 10) )
    lista_2 = list (range (-10,1 ) )
    lista_3 = list (range ( 0 , 21, 2))
    lista_4 = list (range ( -19, 0, 2))
    lista_5 = list (range ( 0, 51, 5))
    print (lista_5)

def ejn_7 ():
    lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
    lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
    lista_3 = []
    for element in (lista_1):
        if (element in lista_2 and not (element in lista_3)):
            lista_3.append (element)
        
    print (lista_3)


