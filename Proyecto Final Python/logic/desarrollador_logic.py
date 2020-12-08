from core.dx_logic import Logic
from objects.desarrolladorObj import desarrolladorObj

class Desarrollador(Logic):
    def __init__(self):
        super().__init__("desarrollador")

    def getAllDesarrollador(self, sql):
        desarrolladorList = super().getAllRows(self.tableName, sql)
        desarrolladorObjList = []
        for element in desarrolladorList:
            newCart = self.createDesarrolladorObj(element)
            desarrolladorObjList.append(newCart)
        return desarrolladorObjList

    # polimorfismo
    def createDesarrolladorObj(self, id, nombre, apellido, usuario, contrasenia):
        desarrolladorObj = desarrolladorObj(id, nombre, apellido, usuario, contrasenia)
        return desarrolladorObj

    def createDesarrolladorObj(self, desarrolladorDict):
        desarrolladorDict = desarrolladorObj(
            desarrolladorDict["id"],
            desarrolladorDict["nombre"],
            desarrolladorDict["apellido"],
            desarrolladorDict["usuario"],
            desarrolladorDict["contrasenia"],
            
        )
        return desarrolladorDict


    def crearCuenta(self, nombre, apellido, usuario, contrasenia):

        database = self.database
        sql = f"""INSERT INTO epicgames.desarrollador
        (nombre, apellido, usuario, contrasenia) VALUES (
        '{nombre}', '{apellido}', '{usuario}', '{contrasenia}') """

            
        cuenta = database.executeNonQueryBool(sql)
        if cuenta == True:
            print("")
            print("La cuenta fue creada correctamente")



    def validarCuenta(self, usuario, contrasenia):
        
        database = self.database
        sql = f"""select * from epicgames.desarrollador where usuario = '{usuario}'
        and contrasenia = '{contrasenia}'"""
            
        record = self.getAllDesarrollador(sql)

        for row in record:
            if row.id:
                print("")
                return (row.id)
            elif not row.id:
                pass

   