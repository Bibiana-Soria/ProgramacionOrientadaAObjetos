from tkinter import *
from tkinter import messagebox
from controller import controlador

class Vista:
    def __init__(self,ventana):
        self.ventana=ventana
        ventana.title("..: Coches System :..")
        ventana.geometry("600x700")
        ventana.resizable(False,False)
        self.menu_principal(ventana)
    
    @staticmethod
    def borrarPantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()
    
    @staticmethod
    def menu_principal(ventana):
        Vista.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text="..:: Menu Principal ::..",justify="center")
        lbl_titulo.pack(pady=5)
        
        marco_botones=Frame(ventana,height=200,width=500,bg="lightblue")
        marco_botones.pack_propagate(False)
        marco_botones.pack(pady=10)
        
        btn_autos=Button(marco_botones,text="Autos",command= lambda: Vista.menu_acciones(ventana,"Autos"))
        btn_autos.grid(column=0,row=0,padx=5,pady=5)
        
        btn_camionetas=Button(marco_botones,text="Camionetas",command= lambda: Vista.menu_acciones(ventana,"Camionetas"))
        btn_camionetas.grid(column=1,row=0,padx=5,pady=5)
        
        btn_camiones=Button(marco_botones,text="Camiones",command= lambda: Vista.menu_acciones(ventana,"Camiones"))
        btn_camiones.grid(column=2,row=0,padx=5,pady=5)
        
        btn_salir=Button(ventana,text="Salir",justify="center",command=ventana.quit)
        btn_salir.pack(pady=10)
    
    @staticmethod
    def menu_acciones(ventana,tipo):
        Vista.borrarPantalla(ventana)
        
        lbl_titulo=Label(ventana,text=f"..:: Menu {tipo} ::..",justify="center")
        lbl_titulo.pack(pady=5)
        
        marco_botones=Frame(ventana,height=200,width=500,bg="lightblue")
        marco_botones.pack_propagate(False)
        marco_botones.pack(pady=10)
        
        if tipo=="Autos":
            btn_insertar=Button(marco_botones,text="Insertar",command= lambda: Vista.insertar_autos(ventana))
            btn_insertar.grid(column=0,row=0,padx=5,pady=5)
            
            btn_consultar=Button(marco_botones,text="Consultar",command= lambda: Vista.consultar_autos(ventana))
            btn_consultar.grid(padx=5,pady=5,column=1,row=0)
            
            btn_actualizar=Button(marco_botones,text="Actualizar",command= lambda: Vista.buscar_id(ventana,tipo,"cambiar"))
            btn_actualizar.grid(column=0,row=1,padx=5,pady=5)
            
            btn_eliminar=Button(marco_botones,text="Eliminar",command= lambda: Vista.buscar_id(ventana,tipo,"borrar"))
            btn_eliminar.grid(column=1,row=1,padx=5,pady=5)
        elif tipo=="Camionetas":
            btn_insertar=Button(marco_botones,text="Insertar",command= lambda: Vista.insertar_camionetas(ventana))
            btn_insertar.grid(column=0,row=0,padx=5,pady=5)
            
            btn_consultar=Button(marco_botones,text="Consultar",command= lambda: Vista.consultar_camionetas(ventana))
            btn_consultar.grid(padx=5,pady=5,column=1,row=0)
            
            btn_actualizar=Button(marco_botones,text="Actualizar",command= lambda: Vista.buscar_id(ventana,tipo,"cambiar"))
            btn_actualizar.grid(column=0,row=1,padx=5,pady=5)
            
            btn_eliminar=Button(marco_botones,text="Eliminar",command= lambda: Vista.buscar_id(ventana,tipo,"borrar"))
            btn_eliminar.grid(column=1,row=1,padx=5,pady=5)
        elif tipo=="Camiones":
            btn_insertar=Button(marco_botones,text="Insertar",command= lambda: Vista.insertar_camiones(ventana))
            btn_insertar.grid(column=0,row=0,padx=5,pady=5)
            
            btn_consultar=Button(marco_botones,text="Consultar",command= lambda: Vista.consultar_camiones(ventana))
            btn_consultar.grid(padx=5,pady=5,column=1,row=0)
            
            btn_actualizar=Button(marco_botones,text="Actualizar",command= lambda: Vista.buscar_id(ventana,tipo,"cambiar"))
            btn_actualizar.grid(column=0,row=1,padx=5,pady=5)
            
            btn_eliminar=Button(marco_botones,text="Eliminar",command= lambda: Vista.buscar_id(ventana,tipo,"borrar"))
            btn_eliminar.grid(column=1,row=1,padx=5,pady=5)
        btn_regresar=Button(ventana,text="Regresar",justify="center",command=lambda:Vista.menu_principal(ventana))
        btn_regresar.pack(pady=10)
    
    @staticmethod
    def insertar_autos(ventana):
        Vista.borrarPantalla(ventana)
        
        lbl_titulo=Label(ventana,text=f"..:: Insertar Autos ::..",justify="center")
        lbl_titulo.pack(pady=5)
        
        lbl_marca=Label(ventana,text="Marca: ",justify="center")
        lbl_marca.pack(pady=5)
        
        txt_marca=Entry(ventana)
        txt_marca.focus()
        txt_marca.pack(pady=3)
        
        lbl_color=Label(ventana,text="Color: ",justify="center")
        lbl_color.pack(pady=5)
        
        txt_color=Entry(ventana)
        txt_color.pack(pady=3)
        
        lbl_modelo=Label(ventana,text="Modelo: ",justify="center")
        lbl_modelo.pack(pady=5)
        
        txt_modelo=Entry(ventana)
        txt_modelo.pack(pady=3)
        
        lbl_velocidad=Label(ventana,text="Velocidad: ",justify="center")
        lbl_velocidad.pack(pady=5)
        
        txt_velocidad=Entry(ventana)
        txt_velocidad.pack(pady=3)
        
        lbl_caballaje=Label(ventana,text="Caballaje: ",justify="center")
        lbl_caballaje.pack(pady=5)
        
        txt_caballaje=Entry(ventana)
        txt_caballaje.pack(pady=3)
        
        lbl_plazas=Label(ventana,text="Plazas: ",justify="center")
        lbl_plazas.pack(pady=5)
        
        txt_plazas=Entry(ventana)
        txt_plazas.pack(pady=3)
        
            
        btn_guardar=Button(ventana,text="Guardar",command=lambda: controlador.controlador_coches.insertar_coches(txt_marca.get(),txt_color.get(),txt_modelo.get(),txt_velocidad.get(),txt_caballaje.get(),txt_plazas.get()),justify="center")
        btn_guardar.pack(pady=10)

        btn_regresar=Button(ventana,text="Regresar",justify="center",command=lambda:Vista.menu_acciones(ventana,"Autos"))
        btn_regresar.pack(pady=10)
    
    @staticmethod
    def consultar_autos(ventana):
        Vista.borrarPantalla(ventana)
        
        lbl_titulo=Label(ventana,text=f"..:: Consultar Autos ::..",justify="center")
        lbl_titulo.pack(pady=5)
        
        registros=controlador.controlador_coches.consultar_coches()
        filas=""
        num_auto=1
        if len(registros)>0:
            for fila in registros:
                filas=filas+f"Auto: {num_auto} \nID: {fila[0]}.- Marca: {fila[1]} Color: {fila[2]} \n Modelo {fila[3]} Velocidad: {fila[4]} \n Caballaje: {fila[5]} Plazas {fila[6]}" 
                num_auto+=1
        else:
            messagebox.showinfo(icon="warning",message="No existen datos para mostrar")
        
        lbl_resultado=Label(ventana,text=f"{filas}")
        lbl_resultado.pack(pady=10)
        
        btn_regresar=Button(ventana,text="Regresar",justify="center",command=lambda:Vista.menu_acciones(ventana,"Autos"))
        btn_regresar.pack(pady=10)
        
    @staticmethod
    def buscar_id(ventana,tipo,accion):
        Vista.borrarPantalla(ventana)
        
        lbl_titulo=Label(ventana,text=f"..:: Buscar {tipo} ::..",justify="center")
        lbl_titulo.pack(pady=5)
        
        lbl_id=Label(ventana,text=f"ID de {tipo} a buscar: ")
        lbl_id.pack(pady=5)
        id=IntVar()
        txt_id=Entry(ventana,textvariable=id,width=5,justify="right")
        txt_id.focus()
        txt_id.pack(pady=5)
        if tipo=="Autos":
            if accion=="cambiar":
                Button(ventana,text="Buscar",command=lambda:Vista.cambiar_auto(ventana,txt_id.get())).pack(pady=5)
            elif accion=="borrar":
                Button(ventana,text="Buscar",command=lambda:Vista.eliminar_auto(ventana,txt_id.get())).pack(pady=5)
        elif tipo=="Camionetas":
            if accion=="cambiar":
                Button(ventana,text="Buscar",command=lambda:Vista.cambiar_camionetas(ventana)).pack(pady=5)
            elif accion=="borrar":
                Button(ventana,text="Buscar",command=lambda:Vista.eliminar_camionetas(ventana)).pack(pady=5)
        elif tipo=="Camiones":
            if accion=="cambiar":
                Button(ventana,text="Buscar",command=lambda:Vista.cambiar_camiones(ventana)).pack(pady=5)
            elif accion=="borrar":
                Button(ventana,text="Buscar",command=lambda:Vista.eliminar_camiones(ventana)).pack(pady=5)   
    
    @staticmethod
    def cambiar_auto(ventana,id_):
        registro=controlador.controlador_coches.buscar_coches(id_)
        if registro is None:
            messagebox.showinfo(icon="info",message="No existe en la BD")
        else:
            Vista.borrarPantalla(ventana)
            lbl_1=Label(ventana,text=f".:: Cambiar Auto ::.")
            lbl_1.pack(pady=10)

            lbl_id=Label(ventana,text="ID: ")
            lbl_id.pack(pady=5)
            id=IntVar()
            txt_id=Entry(ventana,textvariable=id,width=5,justify="right",state="readonly")
            txt_id=Entry(ventana,textvariable=id,width=5,justify="right",state="readonly")
            id.set(id_)
            txt_id.pack(pady=3)
            
            lbl_marca=Label(ventana,text="Marca: ",justify="center")
            lbl_marca.pack(pady=5)
            txt_marca=Entry(ventana)
            txt_marca.pack(pady=3)

            lbl_color=Label(ventana,text="Color: ",justify="center")
            lbl_color.pack(pady=5)
            txt_color=Entry(ventana)
            txt_color.pack(pady=3)

            lbl_modelo=Label(ventana,text="Modelo: ",justify="center")
            lbl_modelo.pack(pady=5)
            txt_modelo=Entry(ventana)
            txt_modelo.pack(pady=3)

            lbl_velocidad=Label(ventana,text="Velocidad: ",justify="center")
            lbl_velocidad.pack(pady=5)
            txt_velocidad=Entry(ventana)
            txt_velocidad.pack(pady=3)

            lbl_potencia=Label(ventana,text="Potencia: ",justify="center")
            lbl_potencia.pack(pady=5)
            txt_potencia=Entry(ventana)
            txt_potencia.pack(pady=5)

            lbl_plazas=Label(ventana,text="No. Plazas: ",justify="center")
            lbl_plazas.pack(pady=5)
            txt_plazas=Entry(ventana)
            txt_plazas.pack(pady=3)
            
            btn_guardar=Button(ventana,text="Guardar",command=lambda:controlador.controlador_coches.actualizar_coches(txt_marca.get(),txt_color.get(),txt_modelo.get(),txt_velocidad.get(),txt_potencia.get(),txt_plazas.get(),id.get()),justify="center")
            btn_guardar.pack(pady=10)

            btn_regresar=Button(ventana,text="Regresar",command=lambda:Vista.menu_acciones(ventana,"Autos"),justify="center")
            btn_regresar.pack(pady=10)

    @staticmethod
    def eliminar_auto(ventana,id_):
        registro=controlador.controlador_coches.buscar_coches(id_)
        if registro is None:
            messagebox.showinfo(icon="info",message="No existe en la BD")
        else:
            Vista.borrarPantalla(ventana)
            lbl_1=Label(ventana,text=f"..:: Eliminar un Auto ::..")
            lbl_1.pack(pady=10)

            lbl_2=Label(ventana,text="ID: ")
            lbl_2.pack(pady=5)
            id=IntVar()

            txt_id_eliminar=Entry(ventana,textvariable=id,width=5)
            txt_id_eliminar.focus()
            txt_id_eliminar.pack(pady=5)

            btn_eliminar=Button(ventana,text="Eliminar",command=lambda:controlador.controlador_coches.eliminar_coches(txt_id_eliminar.get()),justify="center")
            btn_eliminar.pack(pady=10)

            btn_regresar=Button(ventana,text="Regresar",command=lambda:Vista.menu_acciones(ventana,"Autos"),justify="center")
            btn_regresar.pack(pady=10)

    @staticmethod
    def insertar_camionetas(ventana):
        Vista.borrarPantalla(ventana)

        lbl_titulo=Label(ventana,text=f"..:: Insertar Camionetas ::..",justify="center")
        lbl_titulo.pack(pady=5)
        
        lbl_marca=Label(ventana,text="Marca: ",justify="center")
        lbl_marca.pack(pady=5)
        
        txt_marca=Entry(ventana)
        txt_marca.focus()
        txt_marca.pack(pady=3)
        
        lbl_color=Label(ventana,text="Color: ",justify="center")
        lbl_color.pack(pady=5)
        
        txt_color=Entry(ventana)
        txt_color.pack(pady=3)
        
        lbl_modelo=Label(ventana,text="Modelo: ",justify="center")
        lbl_modelo.pack(pady=5)
        
        txt_modelo=Entry(ventana)
        txt_modelo.pack(pady=3)
        
        lbl_velocidad=Label(ventana,text="Velocidad: ",justify="center")
        lbl_velocidad.pack(pady=5)
        
        txt_velocidad=Entry(ventana)
        txt_velocidad.pack(pady=3)
        
        lbl_caballaje=Label(ventana,text="Caballaje: ",justify="center")
        lbl_caballaje.pack(pady=5)
        
        txt_caballaje=Entry(ventana)
        txt_caballaje.pack(pady=3)
        
        lbl_plazas=Label(ventana,text="Plazas: ",justify="center")
        lbl_plazas.pack(pady=5)
        
        txt_plazas=Entry(ventana)
        txt_plazas.pack(pady=3)
        
        lbl_traccion=Label(ventana,text="Traccion: ",justify="center")
        lbl_traccion.pack(pady=5)
            
        txt_traccion=Entry(ventana)
        txt_traccion.pack(pady=3)
            
        lbl_cerrada=Label(ventana,text="Cerrada (SI/NO)",justify="center")
        lbl_cerrada.pack(pady=5)
            
        txt_cerrada=Entry(ventana)
        txt_cerrada.pack(pady=3)
        
        btn_guardar=Button(ventana,text="Guardar",command=lambda:"",justify="center")
        btn_guardar.pack(pady=10)

        btn_regresar=Button(ventana,text="Regresar",justify="center",command=lambda:Vista.menu_acciones(ventana,"Camionetas"))
        btn_regresar.pack(pady=10)
        
    @staticmethod
    def consultar_camionetas(ventana):
        Vista.borrarPantalla(ventana)
        
        lbl_titulo=Label(ventana,text=f"..:: Consultar Camionetas ::..",justify="center")
        lbl_titulo.pack(pady=5)
        
        registros=[(1,"Nissan","Blanco","2020",200,50,5,"4x4","SI")]
        filas=""
        num_auto=1
        if len(registros)>0:
            for fila in registros:
                filas=filas+f"Camioneta: {num_auto} \nID: {fila[0]}.- Marca: {fila[1]} Color: {fila[2]} \n Modelo {fila[3]} Velocidad: {fila[4]} \n Caballaje: {fila[5]} Plazas {fila[6]} \n Traccion: {fila[7]} Cerrada: {fila[8]}" 
                num_auto+=1
        else:
            messagebox.showinfo(icon="warning",message="No existen datos para mostrar")
                
        lbl_resultado=Label(ventana,text=f"{filas}")
        lbl_resultado.pack(pady=10)
        btn_regresar=Button(ventana,text="Regresar",justify="center",command=lambda:Vista.menu_acciones(ventana,"Camionetas"))
        btn_regresar.pack(pady=10)
               
    @staticmethod
    def eliminar_camionetas(ventana):
        Vista.borrarPantalla(ventana)
        
        registro=""
        if registro is None:
            messagebox.showinfo(icon="info",message="No existen este registro en la BD")
        else:
            Vista.borrarPantalla(ventana)
            lbl_1=Label(ventana,text=f"..:: Eliminar Camioneta::..")
            lbl_1.pack(pady=10)

            lbl_2=Label(ventana,text="ID: ")
            lbl_2.pack(pady=5)
            id=IntVar()

            txt_id_eliminar=Entry(ventana,textvariable=id,width=5)
            txt_id_eliminar.focus()
            txt_id_eliminar.pack(pady=5)

            btn_eliminar=Button(ventana,text="Eliminar",command=lambda:"",justify="center")
            btn_eliminar.pack(pady=10)

            btn_regresar=Button(ventana,text="Regresar",command=lambda:Vista.menu_acciones(ventana,"Camionetas"),justify="center")
            btn_regresar.pack(pady=10)   
            
    @staticmethod
    def cambiar_camionetas(ventana):
        Vista.borrarPantalla(ventana)   
        
        lbl_1=Label(ventana,text=f".:: Cambiar Camionetas ::.")
        lbl_1.pack(pady=10)

        lbl_id=Label(ventana,text="ID: ")
        lbl_id.pack(pady=5)
        id=IntVar()
        txt_id=Entry(ventana,textvariable=id,width=5,justify="right",state="readonly")
        txt_id.focus()
        txt_id.pack(pady=3)
        
        lbl_marca=Label(ventana,text="Marca: ",justify="center")
        lbl_marca.pack(pady=5)
        txt_marca=Entry(ventana)
        txt_marca.pack(pady=3)

        lbl_color=Label(ventana,text="Color: ",justify="center")
        lbl_color.pack(pady=5)
        txt_color=Entry(ventana)
        txt_color.pack(pady=3)

        lbl_modelo=Label(ventana,text="Modelo: ",justify="center")
        lbl_modelo.pack(pady=5)
        txt_modelo=Entry(ventana)
        txt_modelo.pack(pady=3)

        lbl_velocidad=Label(ventana,text="Velocidad: ",justify="center")
        lbl_velocidad.pack(pady=5)
        txt_velocidad=Entry(ventana)
        txt_velocidad.pack(pady=3)

        lbl_potencia=Label(ventana,text="Potencia: ",justify="center")
        lbl_potencia.pack(pady=5)
        txt_potencia=Entry(ventana)
        txt_potencia.pack(pady=5)

        lbl_plazas=Label(ventana,text="No. Plazas: ",justify="center")
        lbl_plazas.pack(pady=5)
        txt_plazas=Entry(ventana)
        txt_plazas.pack(pady=3)
        
        lbl_traccion=Label(ventana,text="Traccion: ",justify="center")
        lbl_traccion.pack(pady=5)
        
        txt_traccion=Entry(ventana)
        txt_traccion.pack(pady=3)
        
        lbl_cerrada=Label(ventana,text="Cerrada (SI/NO)",justify="center")
        lbl_cerrada.pack(pady=5)
        
        txt_cerrada=Entry(ventana)
        txt_cerrada.pack(pady=3)
        
        btn_guardar=Button(ventana,text="Guardar",command=lambda:"",justify="center")
        btn_guardar.pack(pady=10)

        btn_regresar=Button(ventana,text="Regresar",command=lambda:Vista.menu_acciones(ventana,"Camionetas"),justify="center")
        btn_regresar.pack(pady=10)
        
    @staticmethod
    def insertar_camiones(ventana):
        Vista.borrarPantalla(ventana)
        
        lbl_titulo=Label(ventana,text=f"..:: Insertar Autos ::..",justify="center")
        lbl_titulo.pack(pady=5)
        
        lbl_marca=Label(ventana,text="Marca: ",justify="center")
        lbl_marca.pack(pady=5)
        
        txt_marca=Entry(ventana)
        txt_marca.focus()
        txt_marca.pack(pady=3)
        
        lbl_color=Label(ventana,text="Color: ",justify="center")
        lbl_color.pack(pady=5)
        
        txt_color=Entry(ventana)
        txt_color.pack(pady=3)
        
        lbl_modelo=Label(ventana,text="Modelo: ",justify="center")
        lbl_modelo.pack(pady=5)
        
        txt_modelo=Entry(ventana)
        txt_modelo.pack(pady=3)
        
        lbl_velocidad=Label(ventana,text="Velocidad: ",justify="center")
        lbl_velocidad.pack(pady=5)
        
        txt_velocidad=Entry(ventana)
        txt_velocidad.pack(pady=3)
        
        lbl_caballaje=Label(ventana,text="Caballaje: ",justify="center")
        lbl_caballaje.pack(pady=5)
        
        txt_caballaje=Entry(ventana)
        txt_caballaje.pack(pady=3)
        
        lbl_plazas=Label(ventana,text="Plazas: ",justify="center")
        lbl_plazas.pack(pady=5)
        
        txt_plazas=Entry(ventana)
        txt_plazas.pack(pady=3)
        
        lbl_eje=Label(ventana,text="Ejes",justify="center")
        lbl_eje.pack(pady=5)
        
        txt_eje=Entry(ventana)
        txt_eje.pack(pady=3)
        
        lbl_carga=Label(ventana,text="Capacidad de Carga: ",justify="center")
        lbl_carga.pack(pady=5)
        
        txt_carga=Entry(ventana)
        txt_carga.pack(pady=3)
        
        btn_guardar=Button(ventana,text="Guardar",command=lambda:"",justify="center")
        btn_guardar.pack(pady=10)

        btn_regresar=Button(ventana,text="Regresar",justify="center",command=lambda:Vista.menu_acciones(ventana,"Camiones"))
        btn_regresar.pack(pady=10)
         
    @staticmethod
    def consultar_camiones(ventana):
        Vista.borrarPantalla(ventana)
        
        lbl_titulo=Label(ventana,text=f"..:: Consultar Camiones ::..",justify="center")
        lbl_titulo.pack(pady=5)
        
        registros=[(1,"Nissan","Blanco","2020",200,50,5,4,1000)]
        filas=""
        num_auto=1
        if len(registros)>0:
            for fila in registros:
                filas=filas+f" Camion: {num_auto} \nID: {fila[0]}.- Marca: {fila[1]} Color: {fila[2]} \n Modelo {fila[3]} Velocidad: {fila[4]} \n Caballaje: {fila[5]} Plazas {fila[6]} Eje: {fila[7]} Capacidad de Carga: {fila[8]}" 
                num_auto+=1
        else:
            messagebox.showinfo(icon="warning",message="No existen datos para mostrar")
        
        lbl_resultado=Label(ventana,text=f"{filas}")
        lbl_resultado.pack(pady=10)
        
        btn_regresar=Button(ventana,text="Regresar",justify="center",command=lambda:Vista.menu_acciones(ventana,"Camiones"))
        btn_regresar.pack(pady=10)
          
    @staticmethod
    def cambiar_camiones(ventana):
        Vista.borrarPantalla(ventana)
        
        registro=""
        if registro is None:
            messagebox.showinfo(icon="info",message="No existe en la BD")
        else:
            Vista.borrarPantalla(ventana)
            lbl_1=Label(ventana,text=f".:: Cambiar Camiones ::.")
            lbl_1.pack(pady=10)

            lbl_id=Label(ventana,text="ID: ")
            lbl_id.pack(pady=5)
            id=IntVar()
            txt_id=Entry(ventana,textvariable=id,width=5,justify="right",state="readonly")
            txt_id.focus()
            txt_id.pack(pady=3)
            
            lbl_marca=Label(ventana,text="Marca: ",justify="center")
            lbl_marca.pack(pady=5)
            txt_marca=Entry(ventana)
            txt_marca.pack(pady=3)

            lbl_color=Label(ventana,text="Color: ",justify="center")
            lbl_color.pack(pady=5)
            txt_color=Entry(ventana)
            txt_color.pack(pady=3)

            lbl_modelo=Label(ventana,text="Modelo: ",justify="center")
            lbl_modelo.pack(pady=5)
            txt_modelo=Entry(ventana)
            txt_modelo.pack(pady=3)

            lbl_velocidad=Label(ventana,text="Velocidad: ",justify="center")
            lbl_velocidad.pack(pady=5)
            txt_velocidad=Entry(ventana)
            txt_velocidad.pack(pady=3)

            lbl_potencia=Label(ventana,text="Potencia: ",justify="center")
            lbl_potencia.pack(pady=5)
            txt_potencia=Entry(ventana)
            txt_potencia.pack(pady=5)

            lbl_plazas=Label(ventana,text="No. Plazas: ",justify="center")
            lbl_plazas.pack(pady=5)
            txt_plazas=Entry(ventana)
            txt_plazas.pack(pady=3)
            
            lbl_eje=Label(ventana,text="Ejes",justify="center")
            lbl_eje.pack(pady=5)
            
            txt_eje=Entry(ventana)
            txt_eje.pack(pady=3)
            
            lbl_carga=Label(ventana,text="Capacidad de Carga: ",justify="center")
            lbl_carga.pack(pady=5)
            
            txt_carga=Entry(ventana)
            txt_carga.pack(pady=3)
            
            btn_guardar=Button(ventana,text="Guardar",command=lambda:"",justify="center")
            btn_guardar.pack(pady=10)

            btn_regresar=Button(ventana,text="Regresar",command=lambda:Vista.menu_acciones(ventana,"Camiones"),justify="center")
            btn_regresar.pack(pady=10)
    
    @staticmethod
    def eliminar_camiones(ventana):
        Vista.borrarPantalla(ventana)
        
        registro=""
        if registro is None:
            messagebox.showinfo(icon="info",message="No existen esta registros la BD")
        else:
            Vista.borrarPantalla(ventana)
            lbl_1=Label(ventana,text=f"..:: Eliminar un Camion ::..")
            lbl_1.pack(pady=10)

            lbl_2=Label(ventana,text="ID: ")
            lbl_2.pack(pady=5)
            id=IntVar()

            txt_id_eliminar=Entry(ventana,textvariable=id,width=5)
            txt_id_eliminar.focus()
            txt_id_eliminar.pack(pady=5)

            btn_eliminar=Button(ventana,text="Eliminar",command=lambda:"",justify="center")
            btn_eliminar.pack(pady=10)

            btn_regresar=Button(ventana,text="Regresar",command=lambda:Vista.menu_acciones(ventana,"Camiones"),justify="center")
            btn_regresar.pack(pady=10)
