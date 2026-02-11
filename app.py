from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "API Flask funcionando!",
        "status": "success",
        "version": "1.0.0"
    })

@app.route('/api/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/api/users/<int:user_id>')
def get_user(user_id):
    return jsonify({
        "id": user_id,
        "name": f"Usuário {user_id}",
        "email": f"user{user_id}@example.com"
    })

@app.route('/api/sum/<int:a>/<int:b>')
def sum_numbers(a, b):
    return jsonify({
        "operation": "sum",
        "a": a,
        "b": b,
        "result": a + b
    })

if __name__ == '__main__':
    print(" Servidor Flask iniciando...")
    print(" Acesse: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)






