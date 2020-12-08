from logic.biblioteca_logic import BibliotecaLogic
from logic.viewVideojuego_logic import viewVideojuego
from logic.videojuego_logic import Videojuego
biblioteca = BibliotecaLogic()
viewVideojuego = viewVideojuego()
videoJuego = Videojuego()



class Biblioteca():
    def __init__(self):
        super().__init__()

    def crearBiblioteca(self, idUsuario):
        viewVideojuego.verNombreVideoJuegos()
        opcion = input("seleccione el juego que quiere: ")
        idVideoJuego = videoJuego.seleccionarIdVideoJuego(opcion)
        while idVideoJuego is None:
            opcion = input("Error, seleccione un juego que si este en la base de datos: ")
            idVideoJuego = videoJuego.seleccionarIdVideoJuego(opcion) 
        biblioteca.crearBiblioteca(idVideoJuego, idUsuario, "actualizado")
    
    


    