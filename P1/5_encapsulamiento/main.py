<<<<<<< HEAD
from coches import *

# Solicitar los datos que posteriormente serán los atributos del objeto

num_coches=int(input("¿Cuantos coches tienes?: "))

for i in range(0, num_coches):
    print(f"\n\t ...Datos del automovil # {i+1}...")
    marca=input("Ingresar la marca: ").upper()
    color=input("Ingresar el color: ").upper()
    modelo=input("Ingresar modelo: ").upper()
    velocidad=int(input("Ingresar Velocidad: "))
    potencia=int(input("Ingresar la potencia: "))
    plazas=int(input("Ingresar el # de plazas: "))

    coche1=Coches(marca, color, modelo, velocidad, potencia, plazas)

    print(f"\n\tDatos del Vehiculo: \n Marca:{coche1.getMarca()} \n color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje: {coche1.getCaballaje()} \n plazas: {coche1.getPlazas()}")




#coche2=Coches("Nissan", "Azul", "2020", 180, 150, 6)
#coche3=Coches("Honda","","",0,0,0)
#coche1.num_serie="B014567890"
#coche4=Coches("","","",0,0,0)
#coche4.marca2="Volvo"
#print(coche4.marca2)

#print(f"Datos del Vehiculo: \n Marca:{coche1.getMarca()} \n color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje: {coche1.getCaballaje()} \n plazas: {coche1.getPlazas()}\n Número de serie: {coche1.num_serie} ")

#print(f"Datos del Vehiculo: \n Marca:{coche2.getMarca()} \n color: {coche2.getColor()} \n Modelo: {coche2.getModelo()} \n velocidad: {coche2.getVelocidad()} \n caballaje: {coche2.getCaballaje()} \n plazas: {coche2.getPlazas()} ")

#print(coche3.marca2)

=======
from coches import *

# Solicitar los datos que posteriormente serán los atributos del objeto

num_coches=int(input("¿Cuantos coches tienes?: "))

for i in range(0, num_coches):
    print(f"\n\t ...Datos del automovil # {i+1}...")
    marca=input("Ingresar la marca: ").upper()
    color=input("Ingresar el color: ").upper()
    modelo=input("Ingresar modelo: ").upper()
    velocidad=int(input("Ingresar Velocidad: "))
    potencia=int(input("Ingresar la potencia: "))
    plazas=int(input("Ingresar el # de plazas: "))

    coche1=Coches(marca, color, modelo, velocidad, potencia, plazas)

    print(f"\n\tDatos del Vehiculo: \n Marca:{coche1.getMarca()} \n color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje: {coche1.getCaballaje()} \n plazas: {coche1.getPlazas()}")




#coche2=Coches("Nissan", "Azul", "2020", 180, 150, 6)
#coche3=Coches("Honda","","",0,0,0)
#coche1.num_serie="B014567890"
#coche4=Coches("","","",0,0,0)
#coche4.marca2="Volvo"
#print(coche4.marca2)

#print(f"Datos del Vehiculo: \n Marca:{coche1.getMarca()} \n color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje: {coche1.getCaballaje()} \n plazas: {coche1.getPlazas()}\n Número de serie: {coche1.num_serie} ")

#print(f"Datos del Vehiculo: \n Marca:{coche2.getMarca()} \n color: {coche2.getColor()} \n Modelo: {coche2.getModelo()} \n velocidad: {coche2.getVelocidad()} \n caballaje: {coche2.getCaballaje()} \n plazas: {coche2.getPlazas()} ")

#print(coche3.marca2)

>>>>>>> b089ef6c5e532afcf47601aa1b79a78263122bd4
