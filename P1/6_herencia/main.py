from coches import *

# Solicitar los datos que posteriormente serán los atributos del objeto

#num_coches=int(input("¿Cuantos coches tienes?: "))

#for i in range(0, num_coches):
    #print(f"\n\t ...Datos del automovil # {i+1}...")
    #marca=input("Ingresar la marca: ").upper()
    #color=input("Ingresar el color: ").upper()
    #modelo=input("Ingresar modelo: ").upper()
    #velocidad=int(input("Ingresar Velocidad: "))
    #potencia=int(input("Ingresar la potencia: "))
    #plazas=int(input("Ingresar el # de plazas: "))

    #coche1=Coches(marca, color, modelo, velocidad, potencia, plazas)

    #print(f"\n\tDatos del Vehiculo: \n Marca:{coche1.marca} \n color: {coche1.color} \n Modelo: {coche1.modelo} \n velocidad: {coche1.velocidad} \n caballaje: {coche1.caballaje} \n plazas: {coche1.plazas}")


coche=Coches("Vw", "Blanco", "2020", 220,180,4)
print(coche.color, coche.acelerar())

camion=Camiones("Vw", "Blanco aperlado", "2020", 220,180,4, 2, 2500)
print(camion.color, camion.acelerar())

camioneta=Camionetas("Vw","Azul", "2020", 220,180,4,"delantera", True)
print(camioneta.color, camioneta.acelerar())

#coche2=Coches("Nissan", "Azul", "2020", 180, 150, 6)
#coche3=Coches("Honda","","",0,0,0)
#coche1.num_serie="B014567890"
#coche4=Coches("","","",0,0,0)
#coche4.marca2="Volvo"
#print(coche4.marca2)

#print(f"Datos del Vehiculo: \n Marca:{coche1.getMarca()} \n color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje: {coche1.getCaballaje()} \n plazas: {coche1.getPlazas()}\n Número de serie: {coche1.num_serie} ")

#print(f"Datos del Vehiculo: \n Marca:{coche2.getMarca()} \n color: {coche2.getColor()} \n Modelo: {coche2.getModelo()} \n velocidad: {coche2.getVelocidad()} \n caballaje: {coche2.getCaballaje()} \n plazas: {coche2.getPlazas()} ")

#print(coche3.marca2)

