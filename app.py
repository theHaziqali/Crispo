from flask import Flask
from flask import render_template
from flask import request
import pymysql

app = Flask(__name__)

# MySQL configuration
host = 'localhost'
user = 'root'
password = ''
database = 'crispo'

@app.route('/')
def index():
    # Connect to MySQL
    conn = pymysql.connect(host=host, user=user, password=password, database=database)
    
    # Create a cursor object
    cursor = conn.cursor()
    
    # Execute a sample query
    cursor.execute("SELECT * FROM mytable")
    
    # Fetch all rows from the result
    rows = cursor.fetchall()
    
    # Close the cursor and connection
    cursor.close()
    conn.close()
    
    return render_template('index.html', rows=rows)

if __name__ == '__main__':
    app.run()