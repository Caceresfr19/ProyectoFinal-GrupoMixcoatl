from core.dx_logic import Logic
from objects.viewBibliotecaObj import viewBibliotecaObj
from prettytable import PrettyTable

class viewBiblioteca(Logic):
    def __init__(self):
        super().__init__("view_biblioteca")

    def getAllBiblioteca(self, sql):
        biblitecaList = super().getAllRows(self.tableName, sql)
        bibliotecaObjList = []
        for element in biblitecaList:
            newCart = self.createBibliotecaObj(element)
            bibliotecaObjList.append(newCart)
        return bibliotecaObjList

    # polimorfismo
    def createBibliotecaObj(self, idUsuario, nombreVideojuego, nombreUsuario, estadoJuego):
        bibliotecaObj = viewBibliotecaObj(idUsuario, nombreVideojuego, nombreUsuario, estadoJuego)
        return bibliotecaObj

    def createBibliotecaObj(self, bibliotecaDict):
        bibliotecaDict = viewBibliotecaObj(
            bibliotecaDict["usuarioId"],
            bibliotecaDict["nombreVideoJuego"],
            bibliotecaDict["nombreUsuario"],
            bibliotecaDict["estadoJuego"],
            
        )
        return bibliotecaDict


    def verBibliteca(self, idUsuario):
        database = self.database
        sql = f"select * from epicgames.view_biblioteca where usuarioId = {idUsuario}"
        
        record = self.getAllBiblioteca(sql) 
        x = PrettyTable(["nombre", "estado"])

        if not record:
            print("No hay ningun producto disponible")
            return None
        else:            
            for biblioteca in record:
                x.add_row([biblioteca.nombreVideojuego, biblioteca.estadoJuego])
        print(x)
