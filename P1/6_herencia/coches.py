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
      return "Estas acelerando el coche"

    def frenar(self):
      return "Estas frenando el coche"

#Fin definir clase

class Camiones(Coches):
   def __init__(self, marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadCarga):
      super().__init__(marca, color, modelo, velocidad, caballaje,plazas)
      self.__eje=eje
      self.__capacidadCarga=capacidadCarga
      
   def cargar(self, tipo_carga): 
      self.tipo_carga=tipo_carga
      return tipo_carga
   
   def acelerar(self):
      return "Estas acelerando el camion"
   
   def frenar(self):
      return "Estas frenando el camion"
   
   @property
   def eje(self):
      return self.__eje
   
   @eje.setter
   def eje(self, eje):
      self.__eje=eje

   @property
   def capacidadCarga(self):
      return self.__capacidadCarga
   
   @capacidadCarga.setter
   def eje(self, capacidadCarga):
      self.__capacidadCarga=capacidadCarga


class Camionetas(Coches):
   def __init__(self, marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada):
      super().__init__(marca, color, modelo, velocidad, caballaje,plazas)
      self.__traccion=traccion
      self.__cerrada=cerrada
      
   def transportar(self, num_pasajeros): 
      self.num_pasajeros=num_pasajeros
      return num_pasajeros
   
   def acelerar(self):
      return "Estas acelerando la camioneta"
   
   def frenar(self):
      return "Estas frenando la camioneta"
   
   @property
   def traccion(self):
      return self.__traccion
   
   @traccion.setter
   def eje(self, traccion):
      self.__traccion=traccion

   @property
   def cerrada(self):
      return self.__cerrada
   
   @cerrada.setter
   def eje(self, cerrada):
      self.__cerrada=cerrada

