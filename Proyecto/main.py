from flask import Flask, render_template,request,redirect,url_for
import mysql.connector
from Clases.Animal import *
from Clases.Enfermedad import *
from flask_paginate import Pagination

listaAnimales=[]
listaEnfermedades=[]
listaMedicamentos=[]

def consulta():
    conn =mysql.connector.connect(user='root',password='12345',host='localhost',database='veterinaria')
    mycursor = conn.cursor()
    mycursor.execute("SELECT * FROM animal")
    #print("ID     Nombre   edad   descripcion")

    for element in mycursor.fetchall():
        animal=Animal()
        animal.crear(element[0],element[1],element[2])
        listaAnimales.append(animal)

consulta()

def consultaEnfermedad():
    conn =mysql.connector.connect(user='root',password='12345',host='localhost',database='veterinaria')
    mycursor = conn.cursor()
    mycursor.execute("SELECT * FROM enfermedad")

    for element in mycursor.fetchall():
        enfermedad=Enfermedad()
        enfermedad.crear(element[0],element[1],element[2])
        listaEnfermedades.append(enfermedad)

consultaEnfermedad()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            return redirect(url_for('animal'))
        else:
            return redirect(url_for('animal'))
    return render_template('login.html')

#Metodo para hacer paginacion
def separar(num,pagina,count,lista1):
    a=count%num
    list=[]
    lista=[]
    if(a==0):
        for x in range(count):
            if (x % num == 0 ):
                list.append(lista)
                lista=[]
            lista.append(lista1[x])
        list.append(lista)
        return list[pagina]
    else:
        for x in range(count - (a - 1)):
            if (x % num == 0):
                list.append(lista)
                lista = []
            lista.append(lista1[x])
        list.append(lista1[count - a:])
        return list[pagina]

@app.route('/animal')
def animal():
    search = False
    q = request.args.get('q')
    if q:
        search = True

    page = request.args.get('page', type=int, default=1)
    animales = separar(5,page,17,listaAnimales)
    pagination = Pagination(page=page, total=17,per_page=5, search=search)
    return render_template('animal.html',
                           animales=animales,
                           pagination=pagination,lista=animales
                           )
@app.route('/enfermedad')
def enfermedad():
    search = False
    q = request.args.get('q')
    if q:
        search = True

    page = request.args.get('page', type=int, default=1)
    enfermedad = separar(5,page,len(listaEnfermedades),listaEnfermedades)
    pagination = Pagination(page=page, total=len(listaEnfermedades),per_page=5, search=search)
    return render_template('enfermedad.html',
                           animales=enfermedad,
                           pagination=pagination, lista=enfermedad
                           )

#Es el encargado de correr el programa
if __name__ == "__main__":
    app.run(debug=True,port=8080)


  #  dfsghjk.lfytynrtfdvycxbhstr jg