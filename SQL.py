import pymysql
from pymysql import cursors

class Database:
    def __init__(self, host, username, password, database_name):
        self.__host = host
        self.__username = username
        self.__password = password
        self.__database_name = database_name
        self__connection = None
    
    def conexionDB(self):
        self.__connection = pymysql.connect(
        
        host = self.__host, 
        user = self.__username, 
        password = self.__password,
        database = self.__database_name
        )

        self.__connection.cursor()
        print('Conexion Exitosa')

    def cerrarDB(self):
        self.__connection.close()
        print('Conexion con Base de Datos cerrada')

    def fetchAll(self):
        try:
            self.__connection.cursor().execute(sql)
            datos = self.__connection.cursor.fetchall()
            return datos
        except Exception as e:
            raise

    
conexionMySQL = Database('127.0.0.10', 'root','', 'hr')

conexionMySQL.conexionDB()
conexionMySQL.fetchAll('SELECTO country_id,country_name FROM countries')
conexionMySQL.cerrarDB()