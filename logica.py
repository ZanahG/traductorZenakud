from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__, static_folder='.', template_folder='.')
CORS(app)

# Función para cargar los significados desde un archivo
def cargar_significados(archivo):
    significados = {}
    try:
        with open(archivo, 'r') as file:
            for line in file:
                parte = line.strip().split(' = ')
                if len(parte) == 2:
                    combinacion, significado = parte
                    significados[combinacion] = significado
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
    return significados

# Función para traducir el texto usando los significados cargados
def traducir_texto(texto, significados):

    letras_permitidas = {'A','D','E','J','K','M','N','O','S','W'}
    if not set(texto).issubset(letras_permitidas):
        return "Zenakud solo usa 8 letras para escribir: D,E,J,K,M,N,O,W prueba intentando con una combinación de estas letras."
    
    traduccion = []
    i = 0
    while i < len(texto):
        # Probar combinaciones de longitud decreciente para encontrar la más larga posible
        encontrado = False
        for j in range(min(8, len(texto) - i), 0, -1):  # Asumiendo que la combinación más larga tiene hasta 6 letras
            parte = texto[i:i+j]
            if parte in significados:
                traduccion.append(significados[parte])
                i += j
                encontrado = True
                break
        if not encontrado:  # Si no se encuentra, avanzar un carácter
            traduccion.append(texto[i])
            i += 1
    return ' '.join(traduccion)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/traducir', methods=['POST'])
def traducir():
    data = request.get_json()
    texto = data.get('texto', '')
    # Suponiendo que 'archivo.txt' está en el mismo directorio que este script
    significados = cargar_significados('words.txt')
    traduccion = traducir_texto(texto, significados)
    return jsonify({'traduccion': traduccion})

if __name__ == '__main__':
    app.run(debug=True)
