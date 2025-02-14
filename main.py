from flask import Flask, render_template, request

app = Flask(__name__)#objeto de la aplicacion creando la aplicacion

@app.route('/')#decorador o ruta de la aplicacion
def index():
    grupo='IDGS803'
    lista=['Gael','Jorge']
    return render_template('index.html',grupo=grupo,lista=lista)


@app.route('/OperasBase')#decorador o ruta de la aplicacion
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
    pagar = ""  

    if request.method == 'POST':
        try:
            nombre = request.form['nombre']
            cantidad_compradores = int(request.form['compradores'])  
            cineco = (request.form['cineco'])
            boletos = int(request.form['boletos'])  
            
            boletos_permitidos = (cantidad_compradores + 1) * 7  

            if boletos > boletos_permitidos:
                pagar = f"Solo se permiten comprar 7 boletos por persona"
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
    app.run(debug=True,port=8080)#el debug es para que se actualice automaticamente