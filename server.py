from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return "Hola Mundo"

@app.route('/dojo')
def dojo():
    return "!Dojo!"

@app.route('/say/<string:nombre>')
def llamar(nombre):
    return f"Hola, {nombre}!"

@app.route('/repeat/<int:num>/<string:name>')
def repeet(num, name):
        output = ''
        for i in range(0, num):
            output += '<p>'+name+'</p>'
        return output


if __name__ == "__main__":
    app.run(debug=True)