from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api", methods=['GET'])
def teste():
    data = {"message": "Taylor linda"}
    return jsonify(data)

@app.route('/usuario/novo', methods=['POST'])
def criar_novo_usuario():
    novo_usuario = request.json
    print(novo_usuario)
    return jsonify({
        'user': novo_usuario,
        'message': 'Usuário criado com sucesso!'
        })
if __name__ == '__main__':
    app.run(debug=True)