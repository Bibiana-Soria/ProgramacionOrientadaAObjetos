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