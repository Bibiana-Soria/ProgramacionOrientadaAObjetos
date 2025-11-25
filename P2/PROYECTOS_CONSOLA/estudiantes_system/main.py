from estudiantes.estudiante import Estudiante
from usuarios.usuario import Usuario
import os
import getpass


def borrarPantalla():
    """Limpia la pantalla: usa 'cls' en Windows y 'clear' en Unix-like."""
    os.system('cls' if os.name == 'nt' else 'clear')

def esperarTecla():
    input("\nPresiona ENTER para continuar...")

class App:
    def __init__(self):
        self.menu_principal()

    def menu_principal(self):
        while True:
            borrarPantalla()
            print("""
        .:: Sistema de Estudiantes ::.
            1.- Registro
            2.- Login
            3.- Salir
            """)
            opcion = input("\t Elige una opción: ").upper()

            if opcion in ['1', 'REGISTRO']:
                borrarPantalla()
                print("\n\t ..:: Registro en el Sistema ::..")
                nombre = input("\t Nombre: ")
                apellidos = input("\t Apellidos: ")
                email = input("\t Email: ")
                password = getpass.getpass("\t Contraseña: ")
                if Usuario.registrar(nombre, apellidos, email, password):
                    print(f"\n\t  Usuario {nombre} registrado correctamente.")
                else:
                    print("\n\t  Error al registrar el usuario.")
                esperarTecla()

            elif opcion in ['2', 'LOGIN']:
                borrarPantalla()
                print("\n\t ..:: Inicio de Sesión ::..")
                email = input("\t Email: ")
                password = getpass.getpass("\t Contraseña: ")
                usuario = Usuario.iniciar_sesion(email, password)
                if usuario:
                    print(f"\n\t Bienvenido {usuario[1]} {usuario[2]} 👋")
                    esperarTecla()
                    self.menu_estudiantes(usuario)
                else:
                    print("\n\t  Credenciales incorrectas.")
                    esperarTecla()

            elif opcion in ['3', 'SALIR']:
                print("\n\t  ¡Hasta luego!")
                break
            else:
                print("\n\t  Opción no válida.")
                esperarTecla()

    def datos_estudiante(self, tipo=None):
        nombre = input("\t Nombre del estudiante: ")
        nota = float(input("\t Nota: "))
        return nombre, nota

    def menu_acciones(self, tipo):
        borrarPantalla()
        print(f"\n\t\t ...:: Menu de {tipo}::.. \n\t1.-Insertar \n\t2.-Consultar \n\t3.-Actualizar \n\t4.-Eliminar \n\t5.-Regresar")
        opcion = input("\n\t Elige una opción: ").upper().strip()
        return opcion

    def respuesta_sql(self, respuesta):
        if respuesta:
            print("\n\t  Operación realizada con éxito.")
        else:
            print("\n\t  Error en la operación.")
        esperarTecla()

    def menu_estudiantes(self):
        while True:
            borrarPantalla()
            opcion = self.menu_acciones("Estudiantes")
            if opcion == "1" or opcion == "INSERTAR":
                nombre, nota = self.datos_estudiante()
                respuesta = Estudiante.insertar(nombre, nota)
                self.respuesta_sql(respuesta)
            elif opcion == "2" or opcion == "CONSULTAR":
                borrarPantalla()
                registros = Estudiante.consultar()
                if len(registros) > 0:
                    for fila in registros:
                        estado = "Aprobado" if fila[2] >= 7 else "Reprobado"
                        print(f"ID: {fila[0]} | Nombre: {fila[1]} | Nota: {fila[2]} | {estado}")
                    esperarTecla()
                else:
                    print("\n\t\t ...¡No existen datos que mostrar por el momento!...")
                    esperarTecla()
            elif opcion == "3" or opcion == "ACTUALIZAR":
                borrarPantalla()
                id = input("Ingrese el ID a actualizar: ").strip()
                nombre, nota = self.datos_estudiante()
                respuesta = Estudiante.actualizar(nombre,nota,id)
                self.respuesta_sql(respuesta)
            elif opcion == "4" or opcion == "ELIMINAR":
                borrarPantalla()
                id = input("Ingrese el ID a eliminar: ").strip()
                respuesta = Estudiante.eliminar(id)
                self.respuesta_sql(respuesta)
            elif opcion == "5" or opcion == "REGRESAR":
                break
            else:
                print("Opción no válida Intente de nuevo")
                esperarTecla()
                
if __name__ == "__main__":
    app = App()