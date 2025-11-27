from tkinter import *
from tkinter import messagebox
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
        
        btn_salir=Button(ventana,text="Salir",justify="center",command=ventana.quit)
        btn_salir.pack(pady=10)
    
    @staticmethod
    def menu(ventana,tipo):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana, text=f"..:: Menu de {tipo} ::..", justify="center")
        lbl_titulo.pack(pady=10)
        
        btn_insertar=Button(ventana,text="Insertar",justify="center",command=lambda: View.datos_auto(ventana,tipo))
        btn_insertar.pack(pady=10)
        
        btn_consultar=Button(ventana,text="Consultar",justify="center",command=lambda: View.consultar_auto(ventana,tipo))
        btn_consultar.pack(pady=10)
        
        btn_actualizar=Button(ventana,text="Actualizar",justify="center",command=lambda: View.actualizar_auto(ventana,tipo))
        btn_actualizar.pack(pady=10)
        
        btn_eliminar=Button(ventana,text="Eliminar",justify="center",command=lambda: "")
        btn_eliminar.pack(pady=10)
        
        btn_volver=Button(ventana,text="Regresar",command=lambda: View.menu_principal(ventana))
        btn_volver.pack(pady=10)    
    
    @staticmethod
    def menu_autos(ventana):
        tipo="Auto"
        View.menu(ventana,tipo)
        
    @staticmethod        
    def menu_camionetas(ventana):
        tipo="Camioneta"
        View.menu(ventana,tipo)
    
    @staticmethod    
    def menu_camiones(ventana):
        tipo="Camion"
        View.menu(ventana,tipo)
        
    @staticmethod
    def datos_auto(ventana,tipo):
        View.borrarPantalla(ventana)
        
        lbl_titulo=Label(ventana,text=f"..:.Agregar {tipo} ::..",justify="center")
        lbl_titulo.pack()
        
        lbl_marca=Label(ventana,text="Marca: ",justify="center")
        lbl_marca.pack()
    
        txt_marca=Entry(ventana)
        txt_marca.pack()
        txt_marca.focus
        
        lbl_color=Label(ventana,text="Color: ",justify="center")
        lbl_color.pack()
        
        txt_color=Entry(ventana)
        txt_color.pack()
        
        lbl_modelo=Label(ventana,text="Modelo: ",justify="center")
        lbl_modelo.pack()
        
        txt_modelo=Entry(ventana)
        txt_modelo.pack()
        
        lbl_velocidad=Label(ventana,text="Velocidad: ",justify="center")
        lbl_velocidad.pack()
        
        txt_velocidad=Entry(ventana)
        txt_velocidad.pack()
        
        lbl_caballaje=Label(ventana,text="Caballaje: ",justify="center")
        lbl_caballaje.pack()
        
        txt_caballaje=Entry(ventana)
        txt_caballaje.pack()
        
        lbl_plazas=Label(ventana,text="Plazas: ",justify="center")
        lbl_plazas.pack()
        
        txt_plazas=Entry(ventana)
        txt_plazas.pack()
        
        if tipo=="Camioneta":
            lbl_traccion=Label(ventana,text="Tracción: ",justify="center")
            lbl_traccion.pack()
            
            txt_traccion=Entry(ventana)
            txt_traccion.pack()
            
            lbl_cerrada=Label(ventana,text="Cerrada (SI/NO): ",justify="center")
            lbl_cerrada.pack(pady=5)
            
            txt_cerrada=Entry(ventana)
            txt_cerrada.pack()
        elif tipo=="Camion":
            lbl_eje=Label(ventana,text="Eje: ",justify="center")
            lbl_eje.pack()
            
            txt_eje=Entry(ventana)
            txt_eje.pack()
            
            lbl_capacidadCarga=Label(ventana,text="Capacidad de Carga: ",justify="center")
            lbl_capacidadCarga.pack(pady=5)
            
            txt_cerrada=Entry(ventana)
            txt_cerrada.pack()
                
        btn_guardar=Button(ventana,text="Guardar",justify="center",command=lambda:"")
        btn_guardar.pack(pady=5)
        btn_volver=Button(ventana,text="Regresar",command=lambda: View.menu_autos(ventana))
        btn_volver.pack(pady=10)
        
        
        
    @staticmethod
    def consultar_auto(ventana,tipo):
        View.borrarPantalla(ventana)
        
        lbl_titulo=Label(ventana,text=f"..:: Consultar {tipo} ::..",justify="center")
        lbl_titulo.pack()
        
        if tipo=="Auto":
            registro=[(1,"Nissan","Blanco","2020",100,250,5)] #ejemplo
            autos=f""
            if len(registro)>0:
                num_auto=1
                for fila in registro:
                    autos=autos+f"{tipo} #{num_auto} con ID: {fila[0]}\nMarca: {fila[1]}\nColor: {fila[2]}\nModelo: {fila[3]}\nVelocidad: {fila[4]}\nPotencia: {fila[5]}\nPlazas: {fila[6]}"
                    num_auto+=1
            else:
                messagebox.showinfo("No hay datos para mostrar")
            lbl_resultado=Label(ventana,text=f"{autos}")
            lbl_resultado.pack()
            btn_volver=Button(ventana,text="Regresar",command=lambda: View.menu_autos(ventana))
            btn_volver.pack(pady=10)
        elif tipo=="Camioneta":
            registro=[(2,"Ford","Azul","2020",10,250,8)] #ejemplo
            autos=f""
            if len(registro)>0:
                num_auto=1
                for fila in registro:
                    autos=autos+f"{tipo} #{num_auto} con ID: {fila[0]}\nMarca: {fila[1]}\nColor: {fila[2]}\nModelo: {fila[3]}\nVelocidad: {fila[4]}\nPotencia: {fila[5]}\nPlazas: {fila[6]}"
                    num_auto+=1
            else:
                messagebox.showinfo("No hay datos para mostrar")
            lbl_resultado=Label(ventana,text=f"{autos}")
            lbl_resultado.pack()  
            btn_volver=Button(ventana,text="Regresar",command=lambda: View.menu_camionetas(ventana))
            btn_volver.pack(pady=10)
        elif tipo=="Camion":
            registro=[(3,"Mercedez","Rojo","2025",10,250,30)] #ejemplo
            autos=f""
            if len(registro)>0:
                num_auto=1
                for fila in registro:
                    autos=autos+f"{tipo} #{num_auto} con ID: {fila[0]}\nMarca: {fila[1]}\nColor: {fila[2]}\nModelo: {fila[3]}\nVelocidad: {fila[4]}\nPotencia: {fila[5]}\nPlazas: {fila[6]}"
                    num_auto+=1
            else:
                messagebox.showinfo("No hay datos para mostrar")
            lbl_resultado=Label(ventana,text=f"{autos}")
            lbl_resultado.pack()
            btn_volver=Button(ventana,text="Regresar",command=lambda: View.menu_camiones(ventana))
            btn_volver.pack(pady=10)
    
        

    