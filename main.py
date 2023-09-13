from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    edad = 18
    return render_template('index.html',edad = edad)

@app.route('/contacto')
def contacto():
    total = 1000
    return '<h1>Información de contacto</h1>'  

@app.route('/proyectos/<string:nombre>/<int:edad>')
def proyectos(nombre, edad= None):
    return render_template('proyectos.html', nombre = nombre, edad = edad)
    
@app.route('/loops')
def loops():
    lista = ["Frutas","Verduras","Limpieza","Abarrotes"]
    return render_template('loops.html',lista = lista)

@app.route('/map/<float(signed=true):lat>/<float(signed=true):long>/<int:zoom>/<int:weidth>/<int:height>/<string:popup_text>')
def map(lat,long,zoom,weidth,height,popup_text):
    return render_template('map.html',lat = lat, long = long, zoom = zoom, weidth = weidth, height = height, popup_text = popup_text)

if __name__ == '__main__':
    app.run(debug=True, host='', port=5000)
