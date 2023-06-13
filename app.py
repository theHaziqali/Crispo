from flask import Flask
from flask import render_template
from flask import request,jsonify
import pymysql
from user import User

app = Flask(__name__)

# MySQL configuration
host = 'localhost'
user = 'root'
password = ''
database = 'Crispo'

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/user', methods=['POST'])
def create_user():
    #json request to get data
    data = request.get_json()

    # Extracting data from the request
    username = data['username']
    email = data['email']
    passwd = data['password']
    # print(username)
    # print(email)
    # print(passwd)

    try:
        # Connect to MySQL
        conn = pymysql.connect(host=host, user=user, password=password, database=database)
        cursor = conn.cursor()

        # Check if the username or email already exists in the user table
        query = "SELECT * FROM user WHERE username = %s OR email = %s"
        cursor.execute(query, (username, email))
        result = cursor.fetchall()

        if result:
            return 'Username or email already exists.', 400

        # Insert the user into the user table
        query = "INSERT INTO user (username, email, password) VALUES (%s, %s, %s)"
        cursor.execute(query, (username, email, passwd))
        conn.commit()
        #closing the connection
        cursor.close()
        conn.close()
        new_user = User(username, email, password)

        return 'User registered successfully.', 200
    except pymysql.connector.Error as error:
        return f"Error connecting to MySQL: {error}", 500

if __name__ == '__main__':
    app.run()