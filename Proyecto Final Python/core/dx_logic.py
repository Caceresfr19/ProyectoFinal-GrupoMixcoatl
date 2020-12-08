from core.database_x import Database_x


class Logic:
    def __init__(self, tableName=None):
        self.database = None
        self.tableName = tableName
        self.__createDatabase()

    def __createDatabase(self):
        if self.database is None:
            self.database = Database_x()

    def getAllRows(self, tableName, sql):
        database = self.database
        rowList = database.executeQueryRows(sql)
        return rowList

    def getRowById(self, id, tableName):
        database = self.database
        sql = f"select * from `{database.database}`.`{tableName}` where id={id};"
        rowDict = database.executeQueryOneRow(sql)
        return rowDict

    def deleteRowById(self, id, tableName):
        database = self.database
        sql = f"DELETE FROM `{database.database}`.`{tableName}` WHERE id = {id};"
        rows = database.executeNonQueryRows(sql)
        return rows
