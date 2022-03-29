from flask import Flask, jsonify, render_template, jsonify
from flask_mysqldb import MySQL

app=Flask(__name__)

#conexion MySQL
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] =''
app.config['MYSQL_DB'] = 'amortizacion'

conexion = MySQL(app)

@app.route('/')
def index():
    cursos=['php','python','c#','MySql']
    data={
        'title' : 'index',
        'content' : 'Hi every body',
        'cursos' : cursos,
        'cantidad' :  len(cursos)
    }
    return render_template('index.html', data=data)

@app.route('/clients')
def list_clients():
    data={}
    try:
        cursor=conexion.connection.cursor()
        sql= "SELECT id, name, loan_amount, rate, time_in_months, date, total_per_due FROM clients"
        cursor.execute(sql)
        clients = cursor.fetchall()
        data['mensaje'] = 'Exito'
        data['clients'] = clients
    except Exception as ex:
        data['mensaje'] = 'Error'
    return jsonify(data)

if __name__ =='__main__':
    app.run(debug=True, port=5000)