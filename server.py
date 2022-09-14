from flask import Flask  # Importa Flask para permitirnos crear nuestra aplicación
app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"
@app.route('/')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def hola_mundo():
    return '¡Hola Mundo!'  # Devuelve la cadena '¡Hola Mundo!' como respuesta

@app.route('/dojo')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def dojo():
    return '¡Dojo!'

@app.route('/users/<name>') # para una ruta '/users/____/____', dos parámetros en la url se pasan como nombre de usuario e id
def name(name):
    return "Hola, " + name 

@app.route('/repeat/<val>/<text>') # para una ruta '/users/____/____', dos parámetros en la url se pasan como nombre de usuario e id
def repeat(val, text):
    valores=[]
    for x in range(int(val)):
        valores.append(text)
    return valores

if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración.

