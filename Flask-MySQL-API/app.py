# app.py
from flask import Flask, json, request, jsonify
from flask_mysqldb import MySQL,MySQLdb #pip install flask-mysqldb https://github.com/alexferl/flask-mysqldb
 
app = Flask(__name__)
  
app.secret_key = "Thanonchai-2021"
  
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'iotssf'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)
  
@app.route('/')
def index():
   cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
   cur.execute("SELECT * FROM employee")
   rv = cur.fetchall()
   employee = []
   content = {}
   for result in rv:
       content = {'id': result['id'], 'name': result['name'], 'email': result['email']}
       employee.append(content)
       content = {}
   return jsonify(employee) 
    
        
if __name__ == '__main__':
    app.run(debug=True)
