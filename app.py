from flask import Flask, request, jsonify
from flask_cors import CORS
 
app = Flask(__name__)
CORS(app)
 
usuarios = [
    'Rennan',
    'Malta',
    'Lanna',
    'Julia',
]
 
@app.route('/usuarios/', methods=['GET'])
def get_users():
    return jsonify(usuarios)
 
@app.route('/usuario/procurar/<int:id>', methods=['GET']) 
def procurar_usuario(id):
    parsedID = int(id)
    usuario = usuarios[id]
   
    data = {"user": f"{usuario}"}
    return jsonify(data)
 
if __name__ == '__main__':
    app.run(port=3000)