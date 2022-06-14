class Mamifero:
    def __init__(self, cantMamas, esperanzaDeVida) -> None:
        self.cantMamas = cantMamas
        self.esperanzaDeVida = esperanzaDeVida
    
    def mamar(self):
        print ("todos los mamiferos toman leche")
    
    def nacer(self):
        pass

class Animal_marino:
    def __init__(self, tieneBranqueas, especie) -> None:
        self.tieneBranqueas = tieneBranqueas
        self.especie = especie
    
    def nadar(self):
        print ("nada sumamente rapido")

class Cetaceo (Mamifero, Animal_marino):
    def __init__(self, cantMamas, esperanzaDeVida, tieneBranqueas, especie, notas, viveEn, peso) -> None:
        Mamifero.__init__(self,cantMamas, esperanzaDeVida) #agarra la class mamifero
        Animal_marino.__init__(self, tieneBranqueas, especie) #agarra la class Animal_marino
        self.notas = notas
        self.viveEn = viveEn
        self.peso = peso
    
    def nacer (self):
        print ("hola é nacido")
    
    def nadar(self):
        print ("no nada muy rapido pero puede nadar grandes distancias y a gran profundidad")

BallenaAzul = Cetaceo(2, 100, False, "cetaceo", "es un animal gordo y gil", "en el mar", 110000)

print (BallenaAzul.esperanzaDeVida)

BallenaAzul.nacer()
BallenaAzul.nadar()
BallenaAzul.mamar()
