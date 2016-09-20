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
listaUsuarios = []
listaMedicamentos=[]
listaPrescripcion = []
listaDosis = []
admin = False
logueado = False

def consulta():
    conn = mysql.connector.connect(user='root',password='12345',host='localhost',database='veterinaria')
    mycursor = conn.cursor()
    mycursor.execute("SELECT * FROM animal")

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

def consultaMedicamentos():
    conn =mysql.connector.connect(user='root',password='12345',host='localhost',database='veterinaria')
    mycursor = conn.cursor()
    mycursor.execute("SELECT * FROM medicamentos")

    for element in mycursor.fetchall():
        medi=Medicamentos()
        medi.crear(element[0],element[1],element[2])
        listaMedicamentos.append(medi)

consultaMedicamentos()

def consultaUsuario():
    conn =mysql.connector.connect(user='root',password='12345',host='localhost',database='veterinaria')
    mycursor = conn.cursor()
    mycursor.execute("SELECT * FROM usuario")

    for element in mycursor.fetchall():
        user=Usuario()
        user.crear(element[0],element[1],element[2],element[3],element[4])
        listaUsuarios.append(user)

consultaUsuario()

def consultaPrescripcion():
    conn =mysql.connector.connect(user='root',password='12345',host='localhost',database='veterinaria')
    mycursor = conn.cursor()
    mycursor.execute("SELECT * FROM prescripcion")

    for element in mycursor.fetchall():
        pres=Prescripcion()
        pres.crear(element[0],element[1],element[2],element[3],element[4],element[5])
        listaPrescripcion.append(pres)

consultaPrescripcion()

def consultaDosis():
    conn =mysql.connector.connect(user='root',password='12345',host='localhost',database='veterinaria')
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
    global logueado
    logueado=False
    if request.method == 'POST':
        li = buscarU(listaUsuarios,request.form['username'])
        if li!=[]:
            if li[0].username == request.form['username'] and li[0].admin == 1 and li[0].password == request.form['password']:
                global admin
                logueado=True
                admin = True
                return redirect(url_for('principal'))

            elif li[0].username == request.form['username']and li[0].admin == 0 and li[0].password == request.form['password']:
                logueado= True
                admin= False
                return redirect(url_for('menuUsuarios'))
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
    global admin
    global logueado
    return render_template('principal.html', admin=admin,logueado=logueado,)

@app.route('/menuUsuarios')
def menuUsuarios():
    global admin
    global logueado
    return render_template('menuUsuarios.html',admin=admin,logueado=logueado,)

#================================================================  INSERTARES ==========================================
@app.route('/insertarAnimal', methods=['GET', 'POST'])
def insertarAnimal():
    l=[]
    global admin
    global logueado
    if request.method == 'POST':
        #Para que todos los campos tengan que estar llenos
        if request.form['nombre']!="" and request.form['descripcion']!="" :
            l = buscar(listaAnimales,request.form['nombre'])
            #Para verificar que no exista ese nombre
            if l == []:
                a=request.form['nombre']
                b=request.form['descripcion']
                c=request.form['foto']
                x=Animal()
                x.crear(a,b,c)
                listaAnimales.append(x)
    return render_template('insertarAnimal.html', admin=admin,logueado=logueado,)

@app.route('/insertarEnfermedades', methods=['GET', 'POST'])
def insertarEnfermedades():
    l=[]
    global admin
    global logueado
    if request.method == 'POST':
        #Para que todos los campos tengan que estar llenos
        if request.form['nombre']!="" and request.form['descripcion']!="" :
            l = buscar(listaEnfermedades,request.form['nombre'])
            #Para verificar que no exista ese nombre
            if l == []:
                a=request.form['nombre']
                b=request.form['descripcion']
                c=request.form['foto']
                x=Enfermedad()
                x.crear(a,b,c)
                listaEnfermedades.append(x)
    return render_template('insertarEnfermedades.html', admin=admin,logueado=logueado,)

@app.route('/insertarMedicamentos', methods=['GET', 'POST'])
def insertarMedicamentos():
    l=[]
    global admin
    global logueado
    if request.method == 'POST':
        #Para que todos los campos tengan que estar llenos
        if request.form['nombre']!="" and request.form['descripcion']!="" :
            l = buscar(listaMedicamentos, request.form['nombre'])
            #Para verificar que no exista ese nombre
            if l == []:
                a=request.form['nombre']
                b=request.form['descripcion']
                c=request.form['foto']
                x=Medicamentos()
                x.crear(a,b,c)
                listaMedicamentos.append(x)
    return render_template('insertarMedicamentos.html', admin=admin,logueado=logueado,)

@app.route('/insertarUsuario', methods=['GET', 'POST'])
def insertarUsuario():
    global admin
    global logueado
    if request.method == 'POST':
        a = request.form['Username']
        b = request.form['Password']
        c = request.form['Nombre']
        d = request.form['Admin']
        e = request.form['Foto']
        x = Usuario()
        x.crear(a, b, c, d, e)
        listaUsuarios.append(x)
    return render_template('insertarUsuario.html', admin=admin,logueado=logueado,)

@app.route('/insertarDosis', methods=['GET', 'POST'])
def insertarDosis():
    global admin
    global logueado
    if request.method == 'POST':
        a = request.form['ID']
        b = request.form['Animal']
        c = request.form['Medicamento']
        w = request.form['Enfermedad']
        d = request.form['RangoPeso']
        e = request.form['Dosis']
        x = Dosis()
        x.crear(a, b, c, w, d, e)
        listaDosis.append(x)
    return render_template('insertarDosis.html', admin=admin,logueado=logueado,)

@app.route('/insertarPrescripcion', methods=['GET', 'POST'])
def insertarPrescripcion():
    global admin
    global logueado
    if request.method == 'POST':
        w = request.form['ID']
        a = request.form['Usuario']
        b = request.form['Animal']
        c = request.form['Enfermedad']
        d = request.form['Peso']
        e = request.form['Dosis']
        x = Prescripcion()
        x.crear(w, a, b, c, d, e)
        listaPrescripcion.append(x)
    return render_template('insertarPrescripcion.html', admin=admin,logueado=logueado,)

#=======================================================================================================================
@app.route('/animal/<texto>', methods=['GET', 'POST'])
def animaliio(texto):
    search = False
    q = request.args.get('q')
    if q:
        search = True
    li = []
    palBusc = texto
    global admin
    global logueado
    li = buscar(listaAnimales, palBusc)

    page = request.args.get('page', type=int, default=1)
    animales = separar(5, page, len(li), li)
    pagination = Pagination(page=page, total=len(li), per_page=5, search=search)
    # Inicia con todos los elementos
    return render_template('animal.html',
                           animales=animales,
                           pagination=pagination, listaAnimales=animales,admin=admin,logueado=logueado,
                           )

@app.route('/animal', methods=['GET', 'POST'])
def animal():
    search = False
    q = request.args.get('q')
    if q:
        search = True
    li=[]
    global admin
    global logueado
    if request.method == 'POST':
        #Si no se busca una palabra
        if request.form['busc']=="":
            page = request.args.get('page', type=int, default=1)
            animales = separar(5,page,len(listaAnimales),listaAnimales)
            pagination = Pagination(page=page, total=len(listaAnimales),per_page=5, search=search)

        #Si se busca una palabra
        else:
            palBusc = request.form['busc']
            li=buscar(listaAnimales,palBusc)
            if(li==[]):
                li=[[]]
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
                           pagination=pagination,listaAnimales=animales,admin=admin,logueado=logueado,
                           )
@app.route('/enfermedad', methods=['GET', 'POST'])
def enfermedad():
    search = False
    q = request.args.get('q')
    if q:
        search = True
    li=[]
    global admin
    global logueado
    if request.method == 'POST':
        #Si no se busca una palabra
        if request.form['busc']=="":
            page = request.args.get('page', type=int, default=1)
            enfermedad = separar(5,page,len(listaEnfermedades),listaEnfermedades)
            pagination = Pagination(page=page, total=len(listaEnfermedades),per_page=5, search=search)

        #Si se busca una palabra
        else:
            palBusc = request.form['busc']
            li=buscar(listaEnfermedades,palBusc)
            if(li==[]):
                li=[[]]

            page = request.args.get('page', type=int, default=1)
            enfermedad = separar(5,page,len(li),li)
            pagination = Pagination(page=page, total=len(li),per_page=5, search=search)
    #Inicia con todos los elementos
    else:
        page = request.args.get('page', type=int, default=1)
        enfermedad = separar(5,page,len(listaEnfermedades),listaEnfermedades)
        pagination = Pagination(page=page, total=len(listaEnfermedades),per_page=5, search=search)

    return render_template('enfermedad.html',
                           pagination=pagination, listaEnfermedades=enfermedad,admin=admin,logueado=logueado,
                           )

@app.route('/medicamentos', methods=['GET', 'POST'])
def medicamentos():
    search = False
    q = request.args.get('q')
    if q:
        search = True
    li=[]
    global admin
    global logueado
    if request.method == 'POST':
        #Si no se busca una palabra
        if request.form['busc']=="":
            page = request.args.get('page', type=int, default=1)
            medi = separar(5,page,len(listaMedicamentos),listaMedicamentos)
            pagination = Pagination(page=page, total=len(listaMedicamentos),per_page=5, search=search)

        #Si se busca una palabra
        else:
            palBusc = request.form['busc']
            li=buscar(listaMedicamentos,palBusc)
            if(li==[]):
                li=[[]]

            page = request.args.get('page', type=int, default=1)
            medi = separar(5,page,len(li),li)
            pagination = Pagination(page=page, total=len(li),per_page=5, search=search)
    #Inicia con todos los elementos
    else:
        page = request.args.get('page', type=int, default=1)
        medi = separar(5,page,len(listaMedicamentos),listaMedicamentos)
        pagination = Pagination(page=page, total=len(listaMedicamentos),per_page=5, search=search)

    return render_template('medicamentos.html',
                           pagination=pagination, listaMedicamentos=medi,admin=admin,logueado=logueado,
                           )

@app.route('/usuario')
def usuario():
    search = False
    q = request.args.get('q')
    if q:
        search = True
    global admin
    global logueado
    page = request.args.get('page', type=int, default=1)
    user = separar(5,page,len(listaUsuarios),listaUsuarios)
    pagination = Pagination(page=page, total=len(listaUsuarios),per_page=5, search=search)
    return render_template('usuario.html',
                           pagination=pagination, listaUsuarios=user, admin=admin,logueado=logueado,
                           )

@app.route('/prescripcion', methods=['GET', 'POST'])
def prescripcion():
    search = False
    q = request.args.get('q')
    if q:
        search = True
    li = []
    global admin
    global logueado
    if request.method == 'POST':
        # Si no se busca una palabra
        if request.form['busc'] == "":
            page = request.args.get('page', type=int, default=1)
            pres = separar(5, page, len(listaPrescripcion), listaPrescripcion)
            pagination = Pagination(page=page, total=len(listaPrescripcion), per_page=5, search=search)

        # Si se busca una palabra
        else:
            palBusc = request.form['busc']
            li = buscarP(listaPrescripcion, palBusc)
            if(li==[]):
                li=[[]]

            page = request.args.get('page', type=int, default=1)
            pres = separar(5, page, len(li), li)
            pagination = Pagination(page=page, total=len(li), per_page=5, search=search)

    # Inicia con todos los elementos
    else:
        page = request.args.get('page', type=int, default=1)
        pres = separar(5, page, len(listaPrescripcion), listaPrescripcion)
        pagination = Pagination(page=page, total=len(listaPrescripcion), per_page=5, search=search)

    return render_template('prescripcion.html',
                           pagination=pagination, listaPrescripcion=pres, admin=admin,logueado=logueado,
                           )

@app.route('/dosis')
def dosis():
    search = False
    q = request.args.get('q')
    if q:
        search = True
    global admin
    global logueado
    page = request.args.get('page', type=int, default=1)
    dos = separar(5,page,len(listaDosis),listaDosis)
    pagination = Pagination(page=page, total=len(listaDosis),per_page=5, search=search)
    return render_template('dosis.html',
                           pagination=pagination, listaDosis=dos, admin=admin,logueado=logueado,
                           )


#Es el encargado de correr el programa
if __name__ == "__main__":
    app.run(debug=True)
