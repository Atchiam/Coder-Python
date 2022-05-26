import json
import pandas as pd
import numpy as np

from os.path import join

def mascotas():
    cantidad_mascotas = int (input ("cuantas mascotas tenes? "))
    intento = 0
    especie = "" #input ("que es tu mascota? ")
    nombre = "" #input ("como se llama tu mascota? ")
    historia= ""#input ("cuenta un breve historia sobre tu mascota ")
    dic_mascotas= {"especie" : especie, "nombre" : nombre, "historia" : historia}

    ruta = "C:/Users/PC/OneDrive/Desktop/rutas_python" #donde esta el archivo
    print( join(ruta,"prueva.txt") )  #mostrar, unir, ruta(carpeta del archivo) con "nombre del arcivo.txt" importante el .txt (tipo de archivo)
# file = open( join(ruta,"mascotas.txt"), "w") # write -> w, read -> r son los permisos con lo que se abre "open"
# file.write("no entiendo?")
# file.close()
    file = open( join(ruta,"mascotas.txt"), "w") 

    while (cantidad_mascotas > intento):
# file.write(dic_mascotas["especie"] + ","+  dic_mascotas["nombre"] + "," + dic_mascotas["historia"])
        especie = input ("que es tu mascota? ")
        nombre = input ("como se llama tu mascota? ")
        historia= input ("cuenta un breve historia sobre tu mascota ")
        file.write( especie + " " + nombre + " " + historia + "\n") 
        intento += 1 

    file.close()

    file_open = open (ruta + "\mascotas.txt", "r")
    lectura = file_open.read()
    print (lectura)
    file_open.close()

def abrir_txt():
    # ruta = open ("C:/Users/PC/OneDrive/Desktop/rutas_python\mascotas.txt", "r")
# lectura = ruta.read()
# print (lectura)
# ruta.close()

    ruta = "C:/Users/PC/OneDrive/Desktop/rutas_python\masotas.txt"
    mascotas_txt = open (ruta , "r" )
    lectura = mascotas_txt.read()
    print (lectura)
    mascotas_txt.close()

def json_ej():
    ruta = "C:/Users/PC/OneDrive/Desktop/rutas_python"
    datos = {}
    datos["los_wachines"]= []    #preguntar
    datos["los_wachinas"]= []

    datos["los_wachines"].append({
    "primer_nombre": "braian",
    "apellido" : "ferreyra",
    "dni" : int(39788453),
    "tel" : int(1155666771)})

    datos["los_wachines"].append({
    "primer_nombre": "matias",
    "apellido" : "cardozo",
    "dni" : int(37465832),
    "tel" : int(1159982371)})

    datos["los_wachines"].append({
    "primer_nombre": "Tobias",
    "apellido" : "bolsita de piedras",
    "dni" : int(3823763),
    "tel" : int(1174735661)})

    datos["los_wachinas"].append({
    "primer_nombre": "braian",
    "apellido" : "ferreyra",
    "dni" : int(39788453),
    "tel" : int(1155666771)})


    datos["los_wachinas"].append({
    "primer_nombre": "matias",
    "apellido" : "cardozo",
    "dni" : int(37465832),
    "tel" : int(1159982371)})

    datos["los_wachinas"].append({
    "primer_nombre": "Tobias",
    "apellido" : "bolsita de piedras",
    "dni" : int(3823763),
    "tel" : int(1174735661)}) 

    with open (ruta + "/primerjson.json", "w") as file:
        json.dump(datos, file, indent=4)

def lectura_json_ej():
    ruta = "C:/Users/PC/OneDrive/Desktop/rutas_python"
    with open (join (ruta , "primerjson.json")) as file:
        data_lectura = json.load(file)
    
    for wachines in data_lectura ["los_wachines"]:
        print ("Nombre: ", wachines ["primer_nombre"])
        print ("Apellido: ", wachines ["apellido"])
        print ("DNI: ", wachines ["dni"])
        print ("Telefono: ", wachines ["tel"])
        print ("")
   
    items = data_lectura.items ()
    print ( items )

def leer_csv():
    ruta = "C:/Users/PC/OneDrive/Desktop/rutas_python"

    variable= pd.read_csv (join(ruta, "historico_velocidad_internet.csv"))

    print (variable.head)

mascotas ()