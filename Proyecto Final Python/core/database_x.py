import pymysql

class Database_x:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = "12345"
        self.database = "epicgames"
        self.cursorType = pymysql.cursors.DictCursor
        self.connection = self.createConnection()

    def createConnection(self):
        connection = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            db=self.database,
            cursorclass=self.cursorType,
        )
        return connection

    def executeNonQueryBool(self, sql):
        currentCursor = self.connection.cursor()
        currentCursor.execute(sql)
        self.connection.commit()
        success = False
        if currentCursor.rowcount > 0:
            success = True
        return success

    def executeNonQueryRows(self, sql):     
        
        currentCursor = self.connection.cursor()
        currentCursor.execute(sql)
        self.connection.commit()
        return currentCursor.rowcount
        
        

    def executeQueryRows(self, sql):    
        currentCursor = self.connection.cursor()
        currentCursor.execute(sql)
        return currentCursor.fetchall()

    def executeQueryOneRow(self, sql):      
        currentCursor = self.connection.cursor()
        currentCursor.execute(sql)
        return currentCursor.fetchone()

    def endConnection(self):
        if self.connection.open:
            self.connection.close()

    def startConnection(self):
        if not self.connection.open:
            self.connection = self.createConnection()
   