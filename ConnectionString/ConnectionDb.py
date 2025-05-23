import mysql.connector
from mysql.connector import Error
import hashlib

class DatabaseConnection:
    def __init__(self):
        self.connection = None
        self.cursor = None
    
    def connect(self):
        """Establish connection to MySQL database"""
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                database='orderingdb',
                user='root',
                password='',
                autocommit=True
            )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
                db_info = self.connection.get_server_info()
                print(f"Connected to MySQL Server version {db_info}")
                return True
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return False
    
    def disconnect(self):
        """Close database connection"""
        if self.connection and self.connection.is_connected():
            if self.cursor:
                self.cursor.close()
            self.connection.close()
            print("MySQL connection is closed")

    def insert_user(self, userID, name, username, password, roleID):
        """Insert a new user with hashed password"""
        try:
            # Hash the password using SHA-256
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            
            sql = """
            INSERT INTO appuser (userID, name, username, password, roleID)
            VALUES (%s, %s, %s, %s, %s)
            """
            values = (userID, name, username, hashed_password, roleID)
            self.cursor.execute(sql, values)
            print("User inserted successfully.")
        except Error as e:
            print(f"Error inserting user: {e}")

# ---------- Run the insertion ----------
db = DatabaseConnection()
if db.connect():
    db.insert_user(
        userID='user-101',
        name='janeabustan',
        username='admin',
        password='123',  # plain password
        roleID='user-101'
    )
    db.disconnect()
