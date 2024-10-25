import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = 'library_db' 


mysql = MySQL(app)


def setup_database():
    try:
        conn = mysql.connection
        cursor = conn.cursor()
        
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS library_db")
        cursor.execute(f"USE library_db")
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            author VARCHAR(255) NOT NULL,
            genre VARCHAR(100),
            available BOOLEAN DEFAULT TRUE
        )
        """)
        conn.commit()  

        cursor.close()
        print(f"Database library_db and table 'books' checked/created successfully.")
    except Exception as e:
        print(f"Error during database setup: {e}")

@app.route('/')
def index():
    setup_database()
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM books")
    books = cur.fetchall()
    cur.close()
    return render_template('index.html', books=books)

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        available = 'available' in request.form 
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO books (title, author, genre, available) VALUES (%s, %s, %s, %s)", 
                    (title, author, genre, available))
        mysql.connection.commit()
        cur.close()
        flash("Book added successfully!")
        return redirect(url_for('index'))
    return render_template('add.html')


@app.route('/delete/<int:id>')
def delete_book(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM books WHERE id=%s", (id,))
    mysql.connection.commit()
    cur.close()
    flash("Book deleted successfully!")
    return redirect(url_for('index'))

@app.route('/toggle/<int:id>')
def toggle_availability(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT available FROM books WHERE id=%s", (id,))
    available = cur.fetchone()[0]
    new_status = not available
    cur.execute("UPDATE books SET available=%s WHERE id=%s", (new_status, id))
    mysql.connection.commit()
    cur.close()
    flash("Book availability updated!")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
