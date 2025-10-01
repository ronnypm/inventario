import mysql.connector


class Database:
    def __init__(self, host="127.0.0.1", user="root", password="", database="tiendita"):
        try:
            self.conexion = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            self.cursor = self.conexion.cursor(dictionary=True)
        except mysql.connector.Error as error:
            print("❌ Error de conexión:", error)
            self.conexion = None
            self.cursor = None

    def execute(self, query, params=None):
        if not self.cursor:
            return None
        self.cursor.execute(query, params or ())
        return self.cursor

    def commit(self):
        if self.conexion:
            self.conexion.commit()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conexion and self.conexion.is_connected():
            self.conexion.close()
            print("🔒 Conexión cerrada")
