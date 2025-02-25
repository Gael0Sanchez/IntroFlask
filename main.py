from flask import Flask, render_template, request
from flask import g
from flask_wtf.csrf import CSRFProtect
from flask import flash
import forms

app = Flask(__name__)
app.secret_key = "Esta es la clave"
csrf = CSRFProtect()


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.before_request
def before_request():
    print("Before 1")

@app.after_request
def after_request(response):
    print("after 3")
    return response 

@app.route('/')
def index():
    grupo='IDGS803'
    lista=['Gael','Jorge']
    return render_template('index.html',grupo=grupo,lista=lista)

@app.route("/Alumnos", methods=["GET","POST"])
def alumnos():
    mat=""
    nom=""
    edad=""
    correo=""
    ape=""
    alumno_clase=forms.UserForm(request.form)
    if request.method=="POST":
        mat = alumno_clase.matricula.data
        nom = alumno_clase.nombre.data
        edad = alumno_clase.edad.data
        correo = alumno_clase.correo.data
        ape = alumno_clase.apellidos.data
        print("Alumnos")
        mensaje = "Binevenido {}".format(nom)
        flash(mensaje)
    return render_template("Alumnos.html",form=alumno_clase,mat=mat,nom=nom,edad=edad,correo=correo,ape=ape)

@app.route('/OperasBase')
def Operas():
    return render_template('OperasBase.html')

@app.route('/resultado', methods=['POST', 'GET'])
def resultado():
    if request.method == 'POST':
        num1 = request.form.get('n1')
        num2 = request.form.get('n2')
        resultado = int(num1) + int(num2)
        return render_template('OperasBase.html', resultado=resultado)


@app.route('/ejemplo1')#decorador o ruta de la aplicacion
def ejemplo1():
    return render_template('ejemplo1.html')

@app.route('/ejemplo2')#decorador o ruta de la aplicacion
def ejemplo2():
    return render_template('ejemplo2.html')

@app.route('/hola')#decorador o ruta de la aplicacion
def hola(): 
    return 'hola!!!!!'

@app.route('/user/<string:user>')#decorador o ruta de la aplicacion  
def user(user): 
    return f'Hola {user}!!!'

@app.route('/suma/<int:n>')#decorador o ruta de la aplicacion
def numero(n): 
    return 'numero: {}'.format(n)

@app.route('/user/<string:user>/<int:id>')#decorador o ruta de la aplicacion  
def username(user,id): 
    return f'Hola {user} ID:{id}!!!'

@app.route('/suma/<float:n1>/<float:n2>')#decorador o ruta de la aplicacion
def suma(n1,n2): 
    return 'La suma es: {}!!!'.format(n1+n2)

@app.route('/form1')
def form1():
    return '''
        <form>
        <label>Nombre:</label>
        <input type="text" name="nombre" placeholder="Escribe tu nombre">
        </br>
        <label>Nombre:</label>
        <input type="text" name="nombre" placeholder="Escribe tu nombre">
        </br>
        <label>Nombre:</label>
        <input type="text" name="nombre" placeholder="Escribe tu nombre">
        </br>
    '''

@app.route('/cinepolis')#decorador o ruta de la aplicacion
def cinepolis():
    return render_template('cinepolis.html')

@app.route('/entradas', methods=['GET', 'POST'])
def pagar():
    resultado = ""  

    if request.method == 'POST':
        try:
            nombre = request.form['nombre']
            cantidad_compradores = int(request.form['compradores'])  
            cineco = int(request.form['cineco'])
            boletos = int(request.form['boletos'])  
            
            boletos_permitidos = (cantidad_compradores + 1) * 7  

            if boletos > boletos_permitidos:
                resultado = f"Solo se permiten comprar 7 boletos por persona"
            else:
                precioBoleto = 12.00
                total = boletos * precioBoleto

                if boletos > 5:
                    descuento = 0.15
                elif 3 <= boletos <= 5:
                    descuento = 0.10
                else:
                    descuento = 0.0

                totalDescuento = total * (1 - descuento)

                if cineco == 1:
                    totalDescuento *= 0.9  

                resultado = f"${totalDescuento:,.2f}"  
        except ValueError:
            resultado = "Error en los datos ingresados, por favor verifica los campos."

    return render_template('cinepolis.html', resultado=resultado)

if __name__ == '__main__': #indicamos de donde se ejecuta la aplicacion
    csrf.init_app(app)
    app.run(debug=True,port=8080)#el debug es para que se actualice automaticamente
