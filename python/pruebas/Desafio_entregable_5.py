from math import pi as PI
"""
def area_rectangulo(base, altura):
    area = base * altura
    return area

base= int(input ("base del cuadrado: "))
altura = int(input ("altura del cuadrado: "))

print (f"El area del cuadrado es {area_rectangulo(base, altura)}")
"""
"""
def area_circulo(radio):
    area = PI * (radio**2)
    return area

radio = int(input("cual es el radio de tu circulo? "))

print(f"el area del circulo es {area_circulo(radio)}")
"""
"""
def relacion(a, b):
    if a > b:
        return 1

    elif a < b:
        return -1

    else:
        return 0

num1 = int(input("escrivi 1° num: "))
num2 = int(input("escrivi 2° num: "))
print (relacion(num1 , num2))
"""
"""
def intermedio(a, b):
    inter = (a+b)/2
    return inter

num1 = int(input("escrivi 1° num: "))
num2 = int(input("escrivi 2° num: "))
print (intermedio(num1 , num2))
"""
"""
def recortar(a, b, c):
    if a < b:
        return b
    elif a > c:
        return c
    else:
        return a

num1 = int(input("escrivi el numero que corte: "))
num2 = int(input("escrivi limite inferior: "))
num3 = int(input("escrivi limite superior: "))

print (recortar(num1 , num2 , num3))
"""
def separar(num):
    num_pares= []
    num_impares= []
    for numero in num:
        if numero % 2 == 0:
            num_pares.append(numero)
        elif numero % 2 == 1:
            num_impares.append(numero)
    num_pares.sort()
    num_impares.sort()
    return num_pares, num_impares

numeros = [6,5,2,1,7]
pares = separar(numeros)[0]
impares = separar(numeros)[1]
print (separar(numeros))
print(pares)
print (impares)