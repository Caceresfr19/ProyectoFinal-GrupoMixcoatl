from core.dx_logic import Logic
from objects.usuarioObj import usuarioObj

class Usuario(Logic):
    def __init__(self):
        super().__init__("usuario")

    def getAllUsuario(self, sql):
        usuarioList = super().getAllRows(self.tableName, sql)
        usuarioObjList = []
        for element in usuarioList:
            newCart = self.createUsuarioObj(element)
            usuarioObjList.append(newCart)
        return usuarioObjList

    # polimorfismo
    def createUsuarioObj(self, id, nombre, apellido, correo, usuario, contrasenia):
        cartObj = usuarioObj(id, nombre, apellido, correo, usuario, contrasenia)
        return cartObj

    def createUsuarioObj(self, usuarioDict):
        usuarioDict = usuarioObj(
            usuarioDict["id"],
            usuarioDict["nombre"],
            usuarioDict["apellido"],
            usuarioDict["correo"],
            usuarioDict["usuario"],
            usuarioDict["contrasenia"],
            
        )
        return usuarioDict




    def crearCuenta(self, nombre, apellido, correo, usuario, contrasenia):

        database = self.database
        sql = f"""INSERT INTO epicgames.usuario
        (nombre, apellido, correo, usuario, contrasenia) VALUES (
        '{nombre}', '{apellido}', '{correo}', '{usuario}', '{contrasenia}') """
      
        cuenta = database.executeNonQueryBool(sql)
        if cuenta == True:
            print("")
            print("La cuenta fue creada correctamente")



    def validarCuenta(self, usuario, contrasenia):
        
        sql = f"""select * from epicgames.usuario where usuario = '{usuario}'
        and contrasenia = '{contrasenia}'"""
            
        record = self.getAllUsuario(sql)

        for row in record:
            if row.id:
                print("")
                return (row.id)
            elif not row.id:
                pass