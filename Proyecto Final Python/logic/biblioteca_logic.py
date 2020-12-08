from core.dx_logic import Logic
from objects.bibliotecaObj import bibliotecaObj

class BibliotecaLogic(Logic):
    def __init__(self):
        super().__init__("biblioteca")

    def crearBiblioteca(self, idVideoJuego, idUsuario, estadoJuego):

        database = self.database
        sql = f"""INSERT INTO epicgames.biblioteca
        (id_videojuego, id_usuario, estadoJuego) VALUES (
        {idVideoJuego}, {idUsuario}, '{estadoJuego}') """
 
        cuenta = database.executeNonQueryBool(sql)
        if cuenta == True:
            print("")
            print("El juego fue comprado correctamente\n")

    def eliminarBiblioteca(self, idVideoJuego):

        database = self.database
        sql = f"""DELETE FROM epicgames.biblioteca WHERE id_videojuego = {idVideoJuego}"""
        cuenta = database.executeNonQueryBool(sql)
        if cuenta == True:
            print("")
            print("El videoojuego fue eliminado\n")