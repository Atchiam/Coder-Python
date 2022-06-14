def dividir(a, b):
    if (a==0 or b==0):
        print ("no seas boludo no se puede dividir por 0")
    else:
        return a/b

def dividir_2(a, b): #try: except:
    try:
        Res= a/b
    
    except ZeroDivisionError:
        print("no se puede dividir por cero")
    
    except TypeError:
        print("tiene que ser un numero")
    
    except Exception as e:
        print ("que rompiste boludo", type (e).__name__) # .__name__ solo retorna el nombre del error 
    
    else:
        print ("aca tenes tu numero")
        return Res
    
    finally:
        print ("fin del programa sea lo que sea")
    

a= 4
b= "??"
print (dividir_2(a, b))