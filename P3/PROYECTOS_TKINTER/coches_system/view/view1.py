from tkinter import *

class View:
    def __init__(self,ventana):
        self.ventana=ventana
        ventana.title("..: Notas System :..")
        ventana.geometry("800x600")
        ventana.resizable(False,False)
        self.menu_principal(ventana)
        
    @staticmethod
    def borrarPantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()
            
    @staticmethod
    def menu_principal(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text="..:: Menu Principal ::..",justify="center")
        lbl_titulo.pack(pady=10)
        
        btn_autos=Button(ventana,text="Autos",justify="center",command=lambda: View.menu_autos(ventana))
        btn_autos.pack(pady=15)
        
        btn_camionetas=Button(ventana,text="Camionetas",justify="center", command=lambda: View.menu_camionetas(ventana))
        btn_camionetas.pack(pady=15)
        
        btn_camiones=Button(ventana,text="Camiones",justify="center",command=lambda: View.menu_camiones(ventana))
        btn_camiones.pack(pady=15)
        
    @staticmethod
    def menu_autos(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana, text=f"..:: Menu de Autos ::..", justify="center")
        lbl_titulo.pack(pady=10)
        
        btn_insertar=Button(ventana,text="Insertar",justify="center",command=lambda: "")
        btn_insertar.pack(pady=10)
        
        btn_consultar=Button(ventana,text="Consultar",justify="center",command=lambda: "")
        btn_consultar.pack(pady=10)
        
        btn_actualizar=Button(ventana,text="Actualizar",justify="center",command=lambda: "")
        btn_actualizar.pack(pady=10)
        
        btn_eliminar=Button(ventana,text="Eliminar",justify="center",command=lambda: "")
        btn_eliminar.pack(pady=10)
        
        btn_volver=Button(ventana,text="Regresar",command=lambda: View.menu_principal(ventana))
        btn_volver.pack(pady=10)
    
    @staticmethod        
    def menu_camionetas(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana, text=f"..:: Menu de Camionetas ::..", justify="center")
        lbl_titulo.pack(pady=10)
        
        btn_insertar=Button(ventana,text="Insertar",justify="center",command=lambda: "")
        btn_insertar.pack(pady=10)
        
        btn_consultar=Button(ventana,text="Consultar",justify="center",command=lambda: "")
        btn_consultar.pack(pady=10)
        
        btn_actualizar=Button(ventana,text="Actualizar",justify="center",command=lambda: "")
        btn_actualizar.pack(pady=10)
        
        btn_eliminar=Button(ventana,text="Eliminar",justify="center",command=lambda: "")
        btn_eliminar.pack(pady=10)
        
        btn_volver=Button(ventana,text="Regresar",command=lambda: View.menu_principal(ventana))
        btn_volver.pack(pady=10)
    
    @staticmethod    
    def menu_camiones(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana, text=f"..:: Menu de Camiones ::..", justify="center")
        lbl_titulo.pack(pady=10)
        
        btn_insertar=Button(ventana,text="Insertar",justify="center",command=lambda: "")
        btn_insertar.pack(pady=10)
        
        btn_consultar=Button(ventana,text="Consultar",justify="center",command=lambda: "")
        btn_consultar.pack(pady=10)
        
        btn_actualizar=Button(ventana,text="Actualizar",justify="center",command=lambda: "")
        btn_actualizar.pack(pady=10)
        
        btn_eliminar=Button(ventana,text="Eliminar",justify="center",command=lambda: "")
        btn_eliminar.pack(pady=10)
        
        btn_volver=Button(ventana,text="Regresar",command=lambda: View.menu_principal(ventana))
        btn_volver.pack(pady=10)