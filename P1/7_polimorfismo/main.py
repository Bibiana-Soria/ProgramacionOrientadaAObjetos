from coches import *
import os
# Solicitar los datos que posteriormente serán los atributos del objeto
os.system("cls")
def autos():
  print(f"\n\t ...Datos del vehículo...")
  marca=input("Ingresar la marca: ").upper()
  color=input("Ingresar el color: ").upper()
  modelo=input("Ingresar modelo: ").upper()
  velocidad=int(input("Ingresar Velocidad: "))
  potencia=int(input("Ingresar la potencia: "))
  plazas=int(input("Ingresar el # de plazas: "))
 
  coche=Coches(marca, color, modelo, velocidad, potencia, plazas)

  print(f"\n\tDatos del Vehiculo: \n Marca:{coche.marca} \n color: {coche.color} \n Modelo: {coche.modelo} \n velocidad: {coche.velocidad} \n caballaje: {coche.caballaje} \n plazas: {coche.plazas}")

def camionetas():   
  print(f"\n\t ...Datos del vehiculo...")
  marca=input("Ingresar la marca: ").upper()
  color=input("Ingresar el color: ").upper()
  modelo=input("Ingresar modelo: ").upper()
  velocidad=int(input("Ingresar Velocidad: "))
  potencia=int(input("Ingresar la potencia: "))
  plazas=int(input("Ingresar el # de plazas: "))
  traccion=input("Ingresar el tipo de tracción: ").upper()
  cerrada=input("Ingresar SI/NO si es cerrada o no: ").upper().strip()
  if cerrada=="SI":
      cerrada=True
  else: 
      cerrada=False
    
  coche1=Camionetas(marca, color, modelo, velocidad, potencia, plazas,traccion,cerrada)

  print(f"\n\tDatos del Vehiculo: \n Marca:{coche1.marca} \n color: {coche1.color} \n Modelo: {coche1.modelo} \n velocidad: {coche1.velocidad} \n caballaje: {coche1.caballaje} \n plazas: {coche1.plazas}\n tracción: {coche1.traccion}\n cerrada: {coche1.cerrada}")


def camiones():   
  print(f"\n\t ...Datos del vehiculo...")
  marca=input("Ingresar la marca: ").upper()
  color=input("Ingresar el color: ").upper()
  modelo=input("Ingresar modelo: ").upper()
  velocidad=int(input("Ingresar Velocidad: "))
  potencia=int(input("Ingresar la potencia: "))
  plazas=int(input("Ingresar el # de plazas: "))
  eje=int(input("Ingresar el número de ejes: "))  
  capacidadCarga=int(input("Ingresar la czapacidad de carga: "))
  coche1=Camiones(marca, color, modelo, velocidad, potencia, plazas,eje,capacidadCarga)

  print(f"\n\tDatos del Vehiculo: \n Marca:{coche1.marca} \n color: {coche1.color} \n Modelo: {coche1.modelo} \n velocidad: {coche1.velocidad} \n caballaje: {coche1.caballaje} \n plazas: {coche1.plazas}\n eje: {coche1.eje}\n capacidad de carga: {coche1.capacidadCarga}")

opcion=1
while opcion!="4":
    os.system("cls")
    opcion=input("\n\t\t ::: Menu Principal :::\n\t1.-Autos\n\t2.-Camionetas\n\t3.-Camiones\n\t4.-Salir\n\tElige una opción:  ").lower().strip()
    match opcion:
        case "1": 
            autos()
            input("Oprima tecla para continuar")
        case "2":
            camionetas()
            input("Oprima tecla para continuar")
        case "3":
            camiones()
            input("Oprima tecla para continuar")
        case "4":
            input("Salir del sistema")
        case _:
            input("Opción inválida... vuelva a intentarlo...")










#coche=Coches("Vw", "Blanco", "2020", 220,180,4)
#print(coche.color, coche.acelerar())

#camion=Camiones("Vw", "Blanco aperlado", "2020", 220,180,4, 2, 2500)
#print(camion.color, camion.acelerar())

#camioneta=Camionetas("Vw","Azul", "2020", 220,180,4,"delantera", True)
#print(camioneta.color, camioneta.acelerar())

#coche2=Coches("Nissan", "Azul", "2020", 180, 150, 6)
#coche3=Coches("Honda","","",0,0,0)
#coche1.num_serie="B014567890"
#coche4=Coches("","","",0,0,0)
#coche4.marca2="Volvo"
#print(coche4.marca2)

#print(f"Datos del Vehiculo: \n Marca:{coche1.getMarca()} \n color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje: {coche1.getCaballaje()} \n plazas: {coche1.getPlazas()}\n Número de serie: {coche1.num_serie} ")

#print(f"Datos del Vehiculo: \n Marca:{coche2.getMarca()} \n color: {coche2.getColor()} \n Modelo: {coche2.getModelo()} \n velocidad: {coche2.getVelocidad()} \n caballaje: {coche2.getCaballaje()} \n plazas: {coche2.getPlazas()} ")

#print(coche3.marca2)

