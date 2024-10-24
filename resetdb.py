from flask import Flask
from flask_mysqldb import MySQL
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = 'library_db'

mysql = MySQL(app)

def reset_database():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("DROP DATABASE IF EXISTS library_db")
        cur.execute("CREATE DATABASE library_db")
        cur.execute("USE library_db")
        cur.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            author VARCHAR(255) NOT NULL,
            genre VARCHAR(100),
            available BOOLEAN DEFAULT TRUE
        )
        """)
        cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(100) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL
        )
        """)
        mysql.connection.commit()
        cur.close()
        print("Database reset successful.")

if __name__ == '__main__':
    reset_database()
