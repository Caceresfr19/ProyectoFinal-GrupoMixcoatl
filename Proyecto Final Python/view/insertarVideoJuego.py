from logic.videojuego_logic import Videojuego
videojuego = Videojuego()

class insertarVideoJuego:
    def __init__(self):
        super().__init__()

    def insertarVideoJuego(self, idUsuario):
        nombre = input("ponga el nombre del videojuego: ")
        categoria = input("ponga el nombre de la categoria: ")
        idCategoria = videojuego.validarCategoria(categoria)
        descripcion = input("ponga la descripcion del videojuego: ")
        precio = input("ponga el precio del videojuego: ")
        año = input("ponga el año que se creo el videojuego: ")
        version = input("ponga la version del videojuego: ")
        videojuego.crearVideoJuego(nombre, idCategoria, idUsuario, descripcion, precio, año, version)