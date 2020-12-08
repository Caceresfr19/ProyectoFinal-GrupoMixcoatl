from core.dx_logic import Logic
from objects.viewVideojuegoObj import viewVideojuegoObj
from prettytable import PrettyTable

class viewVideojuego(Logic):
    def __init__(self):
        super().__init__("view_videojuego")

    def getAllVideoJuego(self, sql):
        videojuegoList = super().getAllRows(self.tableName, sql)
        videojuegoObjList = []
        for element in videojuegoList:
            newCart = self.createVideojuegoObj(element)
            videojuegoObjList.append(newCart)
        return videojuegoObjList

    # polimorfismo
    def createVideojuegoObj(self, idDesarrollador, nombre, categoria, nombreDesarrollador, descripcion, precio, anio, version):
        cartObj = viewVideojuegoObj(idDesarrollador, nombre, categoria, nombreDesarrollador, descripcion, precio, anio, version)
        return cartObj

    def createVideojuegoObj(self, videojuegoDict):
        videojuegoDict = viewVideojuegoObj(
            videojuegoDict["idDesarrollador"],
            videojuegoDict["nombreVideoJuego"],
            videojuegoDict["categoria"],
            videojuegoDict["nombreDesarrollador"],
            videojuegoDict["descripcion"],
            videojuegoDict["precio"],
            videojuegoDict["anio"],
            videojuegoDict["version"],
            
        )
        return videojuegoDict


    
    def verVideoJuegosDesarrollador(self, idDesarrollador):
        database = self.database
        sql = f"select * from epicgames.view_videojuego where idDesarrollador = {idDesarrollador}"

        record = self.getAllVideoJuego(sql)
        x = PrettyTable(["nombre", "categoria", "descripcion", "precio", "año", "version"])

        if not record:
            print("No hay ningun producto disponible")
            return None
        else:            
            for videojuego in record:
                x.add_row([videojuego.nombre, videojuego.categoria,videojuego.descripcion, 
                           videojuego.precio, videojuego.anio, videojuego.version])
        print(x)
    
    def verNombreVideoJuegos(self):

        sql = "select * from epicgames.view_videojuego"

        record = self.getAllVideoJuego(sql)
        x = PrettyTable(["nombre"])

        if not record:
            print("No hay ningun producto disponible")
            return None
        else:            
            for biblioteca in record:
                x.add_row([biblioteca.nombre])
        print(x)

    
    def seleccionarIdVideoJuego(self, videoJuego):
        
        database = self.database
        sql = f"select * from epicgames.videojuego where nombre = '{videoJuego}'"

        record = database.executeQueryRows(sql)

        if record:  
            for row in record:    
                if row.id:
                    return row.id
        
        else:
            return None
