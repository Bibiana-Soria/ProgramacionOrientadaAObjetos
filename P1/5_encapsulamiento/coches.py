import os
os.system("cls")

class Coches:

    #Atributos o propiedades (variables)
    #Caracteristicas del coche
    #valores iniciales es posible declarar al principio de una clase
    #Metodo constructor para inicializar los valores de los atributos a la hora de crear o instanciar un objeto de la clase
    
    def __init__(self,marca, color, modelo, velocidad, caballaje, plazas): 
      self.__marca=marca
      self.__color=color
      self.__modelo=modelo
      self.__velocidad=velocidad
      self.__caballaje=caballaje
      self.__plazas=plazas


   
    #Crear los métodos setters y getters.- estos metodos son importantes y necesarios en todas las clases para que el programador interactue con los valores de los atributos a traves de estos metodos... digamos que es la manera mas adecuada y recomendada para solicitar un valor (get) y/o para ingresar o cambiar un valor (set) a un atributo en particular de la clase a traves de un objeto.
    # en teoria se deberia de crear un metodo getters y setters por cada atributo que contenga la clase.
    #Los metodos get siempre regresan valor, es decir el valor de la propiedad a traves del return
    #Por otro lado el metodo set siempre recibe parametros para cambiar o modofocar el valor del atributo o propiedad en cuestion
   
   #Primer forma
    def getMarca(self):
      return self.__marca
    
    def setMarca(self,marca):
       self.__marca=marca
  
    #Segunda forma
    @property
    def marca2(self):
       return self.__marca
    @marca2.setter
    def marca2(self, marca):
       self.__marca=marca
    
    def getColor(self):
      return self.__color
    
    def setColor(self,color):
       self.__color=color

    def getModelo(self):
      return self.__modelo
    
    def setModelo(self,modelo):
       self.__modelo=modelo

    def getVelocidad(self):
      return self.__velocidad
    
    def setVelocidad(self,velocidad):
       self.__velocidad=velocidad

    def getCaballaje(self):
      return self.__caballaje
    
    def setCaballaje(self,caballaje):
       self.__caballaje=caballaje

    def getPlazas(self):
      return self.__plazas
    
    def setPlazas(self,plazas):
       self.__plazas=plazas

    #Metodos o acciones o funciones que hace el objeto 
    
    def acelerar(self):
      return "Estas acelerando"

    def frenar(self):
      return "Estas frenando"

#Fin definir clase

#Crear un objetos o instanciar la clase

#coche2=Coches("Nissan", "Azul", "2020", 180, 150, 6)
#coche3=Coches("Honda","","",0,0,0)
#coche1.num_serie="B014567890"
#coche4=Coches("","","",0,0,0)
#coche4.marca2="Volvo"
#print(coche4.marca2)

#print(f"Datos del Vehiculo: \n Marca:{coche1.getMarca()} \n color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje: {coche1.getCaballaje()} \n plazas: {coche1.getPlazas()}\n Número de serie: {coche1.num_serie} ")

#print(f"Datos del Vehiculo: \n Marca:{coche2.getMarca()} \n color: {coche2.getColor()} \n Modelo: {coche2.getModelo()} \n velocidad: {coche2.getVelocidad()} \n caballaje: {coche2.getCaballaje()} \n plazas: {coche2.getPlazas()} ")

#print(coche3.marca2)

