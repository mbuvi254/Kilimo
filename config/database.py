import pymysql

class Database:
    def __init__(self):
        self.host="localhost"
        self.user="cyberma3_cm"
        self.password="2024Cybermaisha@"
        self.database="kilimo_high_school_db"
        
    def get_connection(self):
        return pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            cursorclass=pymysql.cursors.DictCursor 
        )
        