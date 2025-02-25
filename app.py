from flask import Flask, request, jsonify
from flask_cors import CORS
 
app = Flask(__name__)
 
usuarios = [
    'Duda',
    'Maite',
    'Sofia',
    'Helena',
    'Elisa',
    'TinkerBell'
]
 
@app.route('/users', methods=['GET'])
def pegar_usuarios():
    return jsonify({'users': usuarios})
 
@app.route('/user/<numero>', methods=['GET'])
def pegar_usuario(numero):
    localNumber = int(numero)
 
    return jsonify({'users': usuarios[localNumber]})
 
 
if __name__ == '__main__':
    app.run(port=3000)