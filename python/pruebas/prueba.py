""""
nombre_user1 = input ("nombre: ")
nota1_user1 = int (input ("primera nota: "))
nota2_user1 = int (input ("segunda nota: "))
print("El estudiante", nombre_user1,"obtuvo una nota de", nota1_user1, "en su primera evaluacion y", nota2_user1, "en la segunda estancia, dando como resultado una nota de", nota1_user1*0.4 + nota2_user1*0.6, "en su nota final")
"""

# nota = "acitametaM ,5.8 ,otipeP ordeP"
# print(nota [::-1])

#"def NOMBRE ():" es una "funcion" " para que funcioone la funcion debe tener una tabulacion"
#dentro de () de un def se puede espesificar datos ej:culo estos datos dentro del () se remplasaran automaticamente en el codigo "def"
#para llamar una "def" se pone el "nombre de la def" y () ej: caca() 

#"int()": es una especificacion donde solo pueden ser numeros "long()" se encargara de numeros mas grandes "float()" de numeros con decimal
# para realizar una espesificacion de numeros se vede de especificar y poner entre () lo que se quiere avarcar EJ:caca

#"imput()": se le pregunta al usuario lo que quiere, se rrellena la "caja" con lo escrito.



def caca(): #1er ejercicio de CoderHouse. nota de profe
    nota = "acitametaM ,5.8 ,otipeP ordeP"
    print(nota [::-1])
    nombre_user1 = input ("nombre: ")
    nota1_user1 = int (input ("primera nota: "))#int (numeros enteros) se encierra todo entre() 
    nota2_user1 = int (input ("segunda nota: "))
    print("El estudiante", nombre_user1,"obtuvo una nota de", nota1_user1, "en su primera evaluacion y", nota2_user1, "en la segunda estancia, dando como resultado una nota de", nota1_user1*0.4 + nota2_user1*0.6, "en su nota final")

def culo(adj): #ejemplo de (adj)
    #adj (puede ser cualquier cosa) es remplasado por la palabra, cuando lo llamas
    papel = "que lindos",adj, "son los culos",adj
    print(papel)

def mate(a,b,c): #ampliacion de "culo" mesclada con operaciones matematicas
    suma= a + b 
    print(suma==c) #(==)operador buliano verdadero o falso, comparar.

def mate1 (): #ejemplos de input con condicionales "==" , "if():" , "else:"
 
    A = int ( input ("A "))
    B = int ( input ("B "))
    C = int ( input ("C "))

    if(A+B==C): # "if():" si se cumple se ejecuta, si no la linea 43 y 44 se salta "==" se usara cuando queramos verificar si lo que esta a su izquierda es igual a lo de su derecha
        print("ejecutar culo")
        mate("pedo","pis","pedopis")
    
    else:       #si no se cumple el "if():" se ejecuta, si se cumple el "if():" no
        print("false")

def caja (): #if elif else
    caja1 = int (input("caja1:"))
    caja2 = int (input("caja2:"))
    if(caja1<caja2):
        print("menor")
    elif(caja1==caja2):
        print("igual")
    else:
        print("mayor")

def funcion ():
    funcion= input("cual funcion queres papa ")
    if (funcion=="caca"):
        print("abriendo ")
        caca()
    elif (funcion=="mate1"):
        print("abriendo ")
        mate1()
    elif (funcion=="caja"):
        print("abriendo ")
        caja()
    elif (funcion=="culo"):
        adjculo = input("tirame un adjetivo ")
        culo (adjculo)
    elif (funcion=="mate"):
        Num1 = int(input("Numero A"))
        Num2 = int(input("Numero B"))
        Num3 = int(input("Numero C"))
        mate(Num1,Num2,Num3)        
    else:
        print("te funeo")

def slising1 (): #cadena echa por el profe [slicing]  [.split(",")] 
    cadena = "acitametaM ,5.8 ,otipeP ordeP"
    cadena_volteada = cadena[::-1]
    nombre, nota, materia = cadena_volteada.split(",") # corta la cadena por un caracter que definamos en este caso "," pero puede ser una letra o lo que definamos.
    print(nota,nombre,materia)

def slicing2 (): #cadena echa por mi. [slicing]  [.split(",")]
    nombre, apellido, edad= "Braian, ferreyra, 25".split(",")
    print(len(nombre))  #len para saver cuantas letras tiene. definimos dentro de un string cuantos caracteres tiene
    print(nombre[::-1]) #[0:6:1] el 1° (0) es de donde comensara 2° (6) donde terminara y el 3° (1) de a cuantos saltara
    print(nombre)
    print(nombre[0:3:1]+"y"+nombre[4:6:1])

def Ac_slicing1 ():
    cadena = "acitametaM ,5.8 ,otipeP ordeP"
    nombre, nota, materia = cadena[::-1].split(",")
    print(nombre, "ha sacado un", nota, "en", materia)
"""
# numero_1 = 9
# numero_2 = 3
# numero_3 = 6
# media = (numero_1 + numero_2 + numero_3) / 3
# print("La nota media es", media)
# La nota media es 14.0

# nota_1 = 10
# nota_2 = 7
# nota_3 = 4


# o bien tambien puede ser algo asi, para que sea el profesor quien ponga las notas deceadas
# nota_1 = int(input ("nota 1 "))
# nota_2 = int(input ("nota 2 "))
# nota_3 = int(input ("nota 3 "))


# nota_media = (nota_1*0.15 + nota_2*0.35 + nota_3*0.5) /3
# print("la nota media del estudiante es", nota_media)


# matriz = [
# [1, 5, 1],
# [2, 1, 2],
# [3, 0, 1],
# [1, 4, 4]
# ]

# matriz[0].append(sum(matriz[0]))
# matriz[1].append(sum(matriz[1]))
# matriz[2].append(sum(matriz[2]))
# matriz[3].append(sum(matriz[3]))
# print(matriz)

# Añade los usuarios: Ana, Ramón, Marta, Eric, David
# Elimina los usuarios: Mario, Miguel, Esteban
"""
def ejercicio_clase_6_sets():
    grupo = {"Miguel", "Blanca", "Mario", "Andrés"}
    grupo_2 = {"Ana", "Ramón", "Marta", "Eric", "David"}
    grupo_eliminar = {"Mario", "Miguel", "Esteban"}

    grupo.update(grupo_2)

    for nombre in grupo_eliminar:
        grupo.discard(nombre)

    print (grupo)

def ejercici_clase_6_dic():
    """
    Añade al diccionario las claves perro, tigre y mono con sus respectivos valores “Bobby”,  “Peepe” y “homero”
    Modificá las claves elefante y delfin con los valores “Trompis”y “Manolo” respectivamente
    """
    animales = {"elefante": ""}

    animales.update({"perro":"Bobby", "tigre":"Peepe", "mono":"homero"})

    print (animales)

    animales["elefante"] = "Trompis"
    animales["delfin"] = "Manolo"

    print (animales)


def ejercico_de_numeroros():
    # Borrar los elementos duplicados
# Ordenar la lista de mayor a menor
# Eliminar todos los números impares 
# Realizar una suma de todos los números que quedan
# Añadir como primer elemento de la lista la suma realizada
# Devolver la lista modificada
# Finalmente, después de ejecutar la función, comprueba que la suma de todos los números a partir del segundo, concuerda con el primer número de la lista
    lista = [29, -5, -12, 17, 5, 7 ,9 , 24, 5, 12, 23, 16, 12, 5, -12, 17]
    lista2 = list(set(lista))
    lista2.sort()
    print (lista)

    for numeros in lista2:
        print (numeros ,numeros%2 ,numeros%2 == 1)
        if numeros%2 == 1 :
            lista2.pop(numeros)
    print (lista2)
    suma = sum (lista2)
    lista2.insert(0,suma)
    print (lista2)

    lista = [29, -5, -12, 17, 5, 7 ,9 , 24, 5, 12, 23, 16, 12, 5, -12, 17]
    lista = list(set(lista))
    lista.sort()
    lista2 = []

    for numeros in lista:
        if (numeros%2 == 0) :
            lista2.append(numeros)
    print (lista2)


def check(num): #EXEPCIONES ".isdigit()" ---> es dijito?
    # excepciones
    if num.isdigit():
        num = int(num) #---> si es un dijito la variable num= pasara de str a int.
        return True, num
    else:
        #print("El tipo de dato es incorrecto.")
        return False



def año_bisiestoV1 (año):
    if check(año):
        if año % 4 == 0:
            if año % 400 == 0 or not año % 100 == 0:
                print (f"Bien! {año} es bisiesto!")
            else:
                print ("no es bisiesto")
        else:
            print ("no es bisiesto")
    else:
        print ("no es un numero ")
        año_bisiestoV1()


def año_bisiestoV2 (año):
    if año.isdigit():
        año = int(año)
        if año % 4 == 0 and (año % 400 == 0 or not año % 100 == 0):
            print (f"Bien! {año} es bisiesto!")
        else:
            print ("no es bisiesto papa")
    
    else:
        print ("no es un numero ")

#def Año_bisiesto_full(check, año_bisiestoV2):
def check(num):
    if num.isdigit():
        num = int(num)
        return num
    else:
        return False

def año_bisiestoV2 (año):
    if check(año):
        año= check(año)
        if año % 4 == 0 and (año % 400 == 0 or not año % 100 == 0):
            print (f"Bien! {año} es bisiesto!")
        else:
            print (f"Este {año} no es bisiesto.")
    else:
        print ("no es un numero ")
        año_bisiestoV2 (input("escrivi un año: "))

im_año_user = input("escrivi un año: ")
año_bisiestoV2(im_año_user)

im_año_user = input("escrivi un año: ")
año_bisiestoV2(im_año_user)


# im_año_user = input("escrivi un año: ")
# año_bisiestoV2(im_año_user)
#input_año = int(input("escriva un año: "))
#año_bisiesto(1995)