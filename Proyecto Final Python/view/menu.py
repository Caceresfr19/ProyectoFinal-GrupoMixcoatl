from logic.desarrollador_logic import Desarrollador
from view.insertarVideoJuego import insertarVideoJuego
from logic.videojuego_logic import Videojuego
from logic.usuario_logic import Usuario
from logic.biblioteca_logic import BibliotecaLogic
from logic.viewBiblioteca_logic import viewBiblioteca
from view.biblioteca import Biblioteca
from logic.viewVideojuego_logic import viewVideojuego

cuentaDes = Desarrollador()
insertarVideojuego = insertarVideoJuego()
videojuego = Videojuego()
biblioteca = Biblioteca()
bibliotecaDb = BibliotecaLogic()
viewbiblioteca = viewBiblioteca()
cuentaUsuario = Usuario()
viewvideojuego = viewVideojuego()

class MenuPrincipal:
    def __init__(self):
        super().__init__()

    def iniciar(self):
        print("presione 1 si es desarrollador")
        print("presione 2 si es usuario")
        opcion = input()

        if opcion == "1":
            self.sesionDesarrollador() 
        elif opcion == "2":
            self.sesionUsuario()
        else:
            print("Error, el numero no esta en las opciones")
            self.iniciar()

    def sesionDesarrollador(self):
        print("presione 1 para crear una cuenta")
        print("presione 2 para iniciar sesion")
        opcion = input("")

        if opcion == "1":
            nombre = input("introduzca su nombre: ")
            apellido = input("introduzca su apellido: ")
            usuario = input("introduzca su nombre de usuario: ")
            contrasenia = input("introduzca una contraseña: ")
            cuentaDes.crearCuenta(nombre, apellido, usuario, contrasenia)
            self.sesionDesarrollador()
        elif opcion == "2":
            usuario = input("introduzca su usuario: ")
            contrasenia = input("introduzca su contraseña: ")
            idUsuario = cuentaDes.validarCuenta(usuario, contrasenia)
            while idUsuario is None:
                print()
                print("por favor ponga una cuenta correcta")
                usuario = input("introduzca su usuario: ")
                contrasenia = input("introduzca su contraseña: \n")
                idUsuario = cuentaDes.validarCuenta(usuario, contrasenia)
                
            self.menuPrincipalDesarrollador(idUsuario)
        else:
            print("Error, el numero no esta en las opciones")
            self.sesionDesarrollador()

    
    def menuPrincipalDesarrollador(self, idUsuario):
        print("presione 1 para añadir un juego nuevo")
        print("presione 2 para actualizar un juego")
        print("presione 3 para ver sus juegos")
        print("presione 4 para regresar al menu principal")
        opcion = input("")

        if opcion == "1":
            insertarVideojuego.insertarVideoJuego(idUsuario)
        elif opcion == "2":
            viewvideojuego.verVideoJuegosDesarrollador(idUsuario)
            nombreJuego = input("inserte el nombre del videojuego que quiere actualizar: ")
            idVideoJuego = videojuego.seleccionarIdVideoJuego(nombreJuego)
            nuevaVersion = input("inserte la nueva version del juego: ")
            videojuego.actualizarVideoJuego(idVideoJuego, nuevaVersion)
        elif opcion == "3":
            viewvideojuego.verVideoJuegosDesarrollador(idUsuario)
        elif opcion == "4":
            self.iniciar()
            pass
        else:
            print("Error, el numero no esta en las opciones")
            self.menuPrincipalDesarrollador(idUsuario)
            
        self.menuPrincipalDesarrollador(idUsuario)

#----------------------------------------------------------


    def sesionUsuario(self):
        print("presione 1 para crear una cuenta")
        print("presione 2 para iniciar sesion")
        opcion = input("")

        if opcion == "1":
            nombre = input("introduzca su nombre: ")
            apellido = input("introduzca su apellido: ")
            correo = input("introduzca su correo: ")
            usuario = input("introduzca su nombre de usuario: ")
            contrasenia = input("introduzca una contraseña: ")
            cuentaUsuario.crearCuenta(nombre, apellido, correo, usuario, contrasenia)
            self.sesionUsuario()
        elif opcion == "2":
            usuario = input("introduzca su usuario: ")
            contrasenia = input("introduzca su contraseña: ")
            idUsuario = cuentaUsuario.validarCuenta(usuario, contrasenia)
            while idUsuario is None:
                print()
                print("por favor ponga una cuenta correcta")
                usuario = input("introduzca su usuario: ")
                contrasenia = input("introduzca su contraseña: ")
                idUsuario = cuentaUsuario.validarCuenta(usuario, contrasenia)
                
            self.menuPrincipalUsuario(idUsuario)
        else:
            print("Error, el numero no esta en las opciones")
            self.sesionUsuario()

    
    def menuPrincipalUsuario(self, idUsuario):
        print("presione 1 para ver sus videojuegos")
        print("presione 2 para comprar un juego")
        print("presione 3 para eliminar un videojuego")
        print("presione 4 para volver al menu principal")
        opcion = input("")
        if opcion == "1":
            viewbiblioteca.verBibliteca(idUsuario)
        elif opcion == "2":
            biblioteca.crearBiblioteca(idUsuario)
        elif opcion == "3":
            viewbiblioteca.verBibliteca(idUsuario)
            nombreVideoJuego = input("ponga el nombre del videojuego que quiere eliminar: ")
            idVideoJuego = videojuego.seleccionarIdVideoJuego(nombreVideoJuego)
            bibliotecaDb.eliminarBiblioteca(idVideoJuego)
        elif opcion == "4":
            self.iniciar()
            pass
        else:
            print("Error, el numero no esta en las opciones")
            self.menuPrincipalUsuario(idUsuario)

        self.menuPrincipalUsuario(idUsuario)

