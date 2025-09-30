#Implementar el paradigma estructurado vs OO
'''
Elaborar una función que calcule el area de un rectángulo
1.- implementar el paradigma estructurado
2.- implementar el paradigma OO
'''
"""
import os
os.system("cls")
base=float(input("Ingresa el valor de la base: "))
altura=float(input("Ingresa el valor de la altura: "))
def calcular_area(base,altura):
    area=base*altura
    return print(f"El area es: {area}")
calcular_area(base,altura)

"""
#1. ESTRUCTURADO
def areaRectangulo (base, altura):
    area=base*altura
    return area

base=15
altura=7
print(f"El área ddel rectángulo es: {(areaRectangulo(base, altura))}")

#VS OO
class AreaRectangulo:
    def areaRectangulo (self, base, altura):
        area=base*altura
        return area
    
rectangulo=AreaRectangulo()
print(f"El área del rectángulo es: {(rectangulo.areaRectangulo(base, altura))}")

class Arearectangulo:
    def __init__(self, base, altura):
        self.base=base
        self.altura=altura

    def areaRectangulo (self, base, altura):
        area=self.base*self.altura
        return area

    
Rectangulo=Arearectangulo(15, 7)
print(f"El área del rectángulo es: {(rectangulo.areaRectangulo(base, altura))}")