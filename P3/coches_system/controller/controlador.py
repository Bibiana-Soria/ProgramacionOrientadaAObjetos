from model import cochesBD
from tkinter import messagebox

class controlador_coches:
    @staticmethod
    def respuesta_sql(resultado):
        if resultado:
            messagebox.showinfo(message=f" Acción Realizada con Éxito ",icon="info")
        else:
            messagebox.showinfo(message="\n\t...No fue posible realizar la acción correctamente, vuelva a intentar...",icon="info")
     
    
    @staticmethod
    def insertar_coches(marca,color,modelo,velocidad,caballaje,plazas):
        resultado=cochesBD.Autos.insertar(marca,color,modelo,velocidad,caballaje,plazas)
        controlador_coches.respuesta_sql(resultado)
        
    @staticmethod
    def consultar_coches():
        registros=cochesBD.Autos.consultar()
        return registros
    
    @staticmethod
    def actualizar_coches(marca,color,modelo,velocidad,caballaje,plazas,id_):
        resultado=cochesBD.Autos.actualizar(marca,color,modelo,velocidad,caballaje,plazas,id_)
        controlador_coches.respuesta_sql(resultado)
    
    @staticmethod
    def eliminar_coches(id_):
        resultado=cochesBD.Autos.eliminar(id_)
        controlador_coches.respuesta_sql(resultado)
    
    @staticmethod
    def buscar_coches(id_):
        resultado=cochesBD.Autos.buscar(id_)
        return resultado
    
class controlador_camionetas:
    @staticmethod
    def respuesta_sql(resultado): 
        if resultado:
            messagebox.showinfo(message=f" Acción Realizada con Éxito ",icon="info")
        else:
            messagebox.showinfo(message="\n\t...No fue posible realizar la acción correctamente, vuelva a intentar...",icon="info")   
            
    @staticmethod
    def insertar_camionetas(marca,color,modelo,velocidad,caballaje,plazas,traccion, cerrada):
        if cerrada=="si":
            cerrada=True
        elif cerrada=="no":
            cerrada=False
        resultado=cochesBD.Camionetas.insertar(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada)
        controlador_coches.respuesta_sql(resultado)
        
    @staticmethod
    def consultar_camionetas():
        registros=cochesBD.Camionetas.consultar()
        return registros
    
    @staticmethod
    def actualizar_camionetas(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada,id_):
        if cerrada=="si":
            cerrada=True
        elif cerrada=="no":
            cerrada=False
        resultado=cochesBD.Camionetas.actualizar(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada,id_)
        controlador_coches.respuesta_sql(resultado)
    
    @staticmethod
    def eliminar_camionetas(id_):
        resultado=cochesBD.Camionetas.eliminar(id_)
        controlador_coches.respuesta_sql(resultado)
    
    @staticmethod
    def buscar_camionetas(id_):
        resultado=cochesBD.Camionetas.buscar(id_)
        return resultado        