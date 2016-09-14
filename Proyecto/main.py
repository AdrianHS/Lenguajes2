from flask import Flask, render_template,request,redirect,url_for
import mysql.connector
from Clases.Animal import *
from Clases.Enfermedad import *
from Clases.Medicamentos import *
from Clases.Usuario import *
from Clases.Prescripcion import *
from Clases.Dosis import *
from flask_paginate import Pagination
from Funciones import *

listaAnimales=[]
listaEnfermedades=[]
listaMedicamentos=[]
listaUsuarios = []
listaPrescripcion = []
listaDosis = []


def consulta():
    conn =mysql.connector.connect(user='root',password='1234',host='localhost',database='veterinaria')
    mycursor = conn.cursor()
    mycursor.execute("SELECT * FROM animal")

    for element in mycursor.fetchall():
        animal=Animal()
        animal.crear(element[0],element[1],element[2])
        listaAnimales.append(animal)

consulta()

def consultaEnfermedad():
    conn =mysql.connector.connect(user='root',password='1234',host='localhost',database='veterinaria')
    mycursor = conn.cursor()
    mycursor.execute("SELECT * FROM enfermedad")

    for element in mycursor.fetchall():
        enfermedad=Enfermedad()
        enfermedad.crear(element[0],element[1],element[2])
        listaEnfermedades.append(enfermedad)

consultaEnfermedad()

def consultaMedicamentos():
    conn =mysql.connector.connect(user='root',password='1234',host='localhost',database='veterinaria')
    mycursor = conn.cursor()
    mycursor.execute("SELECT * FROM medicamentos")

    for element in mycursor.fetchall():
        medi=Medicamentos()
        medi.crear(element[0],element[1],element[2])
        listaMedicamentos.append(medi)

consultaMedicamentos()

def consultaUsuario():
    conn =mysql.connector.connect(user='root',password='1234',host='localhost',database='veterinaria')
    mycursor = conn.cursor()
    mycursor.execute("SELECT * FROM usuario")

    for element in mycursor.fetchall():
        user=Usuario()
        user.crear(element[0],element[1],element[2],element[3],element[4])
        listaUsuarios.append(user)

consultaUsuario()

def consultaPrescripcion():
    conn =mysql.connector.connect(user='root',password='1234',host='localhost',database='veterinaria')
    mycursor = conn.cursor()
    mycursor.execute("SELECT * FROM prescripcion")

    for element in mycursor.fetchall():
        pres=Prescripcion()
        pres.crear(element[0],element[1],element[2],element[3],element[4],element[5])
        listaPrescripcion.append(pres)

consultaPrescripcion()

def consultaDosis():
    conn =mysql.connector.connect(user='root',password='1234',host='localhost',database='veterinaria')
    mycursor = conn.cursor()
    mycursor.execute("SELECT * FROM dosis")

    for element in mycursor.fetchall():
        dosis=Dosis()
        dosis.crear(element[0],element[1],element[2],element[3],element[4],element[5])
        listaDosis.append(dosis)

consultaDosis()
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            return redirect(url_for('principal'))
        else:
            return redirect(url_for('principal'))
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

@app.route('/principal')
def principal():
    return render_template('principal.html')

@app.route('/animal', methods=['GET', 'POST'])
def animal():
    search = False
    q = request.args.get('q')
    if q:
        search = True
    li=[]

    if request.method == 'POST':
        #Si no se busca una palabra
        if request.form['busc']=="":
            page = request.args.get('page', type=int, default=1)
            animales = separar(5,page,len(listaAnimales),listaAnimales)
            pagination = Pagination(page=page, total=len(listaAnimales),per_page=5, search=search)

        #Si se busca una palabra
        else:
            palBusc = request.form['busc']
            li=[buscar(listaAnimales,palBusc)]

            page = request.args.get('page', type=int, default=1)
            animales = separar(5,page,len(li),li)
            pagination = Pagination(page=page, total=len(li),per_page=5, search=search)
    #Inicia con todos los elementos
    else:
        page = request.args.get('page', type=int, default=1)
        animales = separar(5,page,len(listaAnimales),listaAnimales)
        pagination = Pagination(page=page, total=len(listaAnimales),per_page=5, search=search)

    return render_template('animal.html',
                           animales=animales,
                           pagination=pagination,listaAnimales=animales,
                           )
@app.route('/enfermedad', methods=['GET', 'POST'])
def enfermedad():
    search = False
    q = request.args.get('q')
    if q:
        search = True

    li=[]
    if request.method == 'POST':
        #Si no se busca una palabra
        if request.form['busc']=="":
            page = request.args.get('page', type=int, default=1)
            enfermedad = separar(5,page,len(listaEnfermedades),listaEnfermedades)
            pagination = Pagination(page=page, total=len(listaEnfermedades),per_page=5, search=search)

        #Si se busca una palabra
        else:
            palBusc = request.form['busc']
            li=[buscar(listaEnfermedades,palBusc)]

            page = request.args.get('page', type=int, default=1)
            enfermedad = separar(5,page,len(li),li)
            pagination = Pagination(page=page, total=len(li),per_page=5, search=search)
    #Inicia con todos los elementos
    else:
        page = request.args.get('page', type=int, default=1)
        enfermedad = separar(5,page,len(listaEnfermedades),listaEnfermedades)
        pagination = Pagination(page=page, total=len(listaEnfermedades),per_page=5, search=search)

    return render_template('enfermedad.html',
                           pagination=pagination, listaEnfermedades=enfermedad,
                           )

@app.route('/medicamentos', methods=['GET', 'POST'])
def medicamentos():
    search = False
    q = request.args.get('q')
    if q:
        search = True
    li=[]
    if request.method == 'POST':
        #Si no se busca una palabra
        if request.form['busc']=="":
            page = request.args.get('page', type=int, default=1)
            medi = separar(5,page,len(listaMedicamentos),listaMedicamentos)
            pagination = Pagination(page=page, total=len(listaMedicamentos),per_page=5, search=search)

        #Si se busca una palabra
        else:
            palBusc = request.form['busc']
            li=[buscar(listaMedicamentos,palBusc)]

            page = request.args.get('page', type=int, default=1)
            medi = separar(5,page,len(li),li)
            pagination = Pagination(page=page, total=len(li),per_page=5, search=search)
    #Inicia con todos los elementos
    else:
        page = request.args.get('page', type=int, default=1)
        medi = separar(5,page,len(listaMedicamentos),listaMedicamentos)
        pagination = Pagination(page=page, total=len(listaMedicamentos),per_page=5, search=search)

    return render_template('medicamentos.html',
                           pagination=pagination, listaMedicamentos=medi,
                           )

@app.route('/usuario')
def usuario():
    search = False
    q = request.args.get('q')
    if q:
        search = True

    page = request.args.get('page', type=int, default=1)
    user = separar(5,page,len(listaUsuarios),listaUsuarios)
    pagination = Pagination(page=page, total=len(listaUsuarios),per_page=5, search=search)
    return render_template('usuario.html',
                           pagination=pagination, listaUsuarios=user,
                           )

@app.route('/prescripcion')
def prescripcion():
    search = False
    q = request.args.get('q')
    if q:
        search = True

    page = request.args.get('page', type=int, default=1)
    pres = separar(5,page,len(listaPrescripcion),listaPrescripcion)
    pagination = Pagination(page=page, total=len(listaPrescripcion),per_page=5, search=search)
    return render_template('prescripcion.html',
                           pagination=pagination, listaPrescripcion=pres,
                           )

@app.route('/dosis')
def dosis():
    search = False
    q = request.args.get('q')
    if q:
        search = True

    page = request.args.get('page', type=int, default=1)
    dos = separar(5,page,len(listaDosis),listaDosis)
    pagination = Pagination(page=page, total=len(listaDosis),per_page=5, search=search)
    return render_template('dosis.html',
                           pagination=pagination, listaDosis=dos,
                           )


#Es el encargado de correr el programa
if __name__ == "__main__":
    app.run(debug=True,port=8080)

#prueba