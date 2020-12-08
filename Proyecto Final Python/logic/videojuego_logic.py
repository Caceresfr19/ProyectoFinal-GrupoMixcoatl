from core.dx_logic import Logic
from objects.videojuegoObj import videojuegoObj
from prettytable import PrettyTable

class Videojuego(Logic):
    def __init__(self):
        super().__init__("videojuego")

    def getAllVideoJuego(self, sql):
        videojuegoList = super().getAllRows(self.tableName, sql)
        videojuegoObjList = []
        for element in videojuegoList:
            newCart = self.createVideojuegoObj(element)
            videojuegoObjList.append(newCart)
        return videojuegoObjList

    # polimorfismo
    def createVideojuegoObj(self, id, nombre, idCategoria, descripcion, precio, anio, version):
        cartObj = videojuegoObj(id, nombre, idCategoria, descripcion, precio, anio, version)
        return cartObj

    def createVideojuegoObj(self, videojuegoDict):
        videojuegoDict = videojuegoObj(
            videojuegoDict["id"],
            videojuegoDict["nombre"],
            videojuegoDict["id_categoria"],
            videojuegoDict["descripcion"],
            videojuegoDict["precio"],
            videojuegoDict["anio"],
            videojuegoDict["version"],
            
        )
        return videojuegoDict


    
    def crearCategoria(self, categoria):

        database = self.database
        sql = f"""INSERT INTO epicgames.categoria
        (categoria) VALUES (
        '{categoria}') """
 
        cuenta = database.executeNonQueryBool(sql)
        if cuenta == True:
            print("")
            print("La categoria fue creada correctamente")

    def validarCategoria(self, categoria):

        database = self.database
        sql= f"""select * from epicgames.categoria where categoria = '{categoria}' """

        record = database.executeQueryRows(sql)


        if record:
            for row in record:
                if row["id"]:
                    return row["id"]
        else:
            self.crearCategoria(categoria)
            idCategoria = self.validarCategoria(categoria)
            return idCategoria


    def crearVideoJuego(self, nombre, idCategoria, idDesarrollador, descripcion, precio, anio, version):

        database = self.database
        sql = f"""INSERT INTO epicgames.videojuego
        (nombre, id_categoria, id_desarrollador, descripcion, precio, anio, version) VALUES (
        '{nombre}', {idCategoria}, {idDesarrollador}, '{descripcion}', {precio}, {anio}, {version}) """

            
        cuenta = database.executeNonQueryBool(sql)
        if cuenta == True:
            print("")
            print("El videojuego fue creado correctamente")

    
    def actualizarVideoJuego(self, idVideoJuego, nuevaVersion):

        try:
            database = self.database

            sql = f"""UPDATE epicgames.videojuego SET version = {nuevaVersion} WHERE id = {idVideoJuego}"""
            
            count = database.executeNonQueryRows(sql)

            if count > 0:
                print()
                print("El videojuego se actualizo correctamente\n")

                sql = f"""UPDATE epicgames.biblioteca SET estadoJuego = 'actualizacion pendiente' WHERE id_videojuego = {idVideoJuego};"""
                database.executeNonQueryRows(sql)


        except Exception:
            print()
            print("no se pudo actualizar correctamente")

        finally:
            pass


    def seleccionarIdVideoJuego(self, videoJuego):
        
        database = self.database
        sql = f"select * from epicgames.videojuego where nombre = '{videoJuego}'"

        record = self.getAllVideoJuego(sql)

        if record:   
            for row in record:    
                if row.id:
                    return row.id
        
        else:
            return None
