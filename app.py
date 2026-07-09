from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
    <h1>Proyecto 2 - DevSecOps</h1>
    <p>La aplicación funciona correctamente.</p>
    """

@app.route("/health")
def health():
    return jsonify({
        "status": "OK"
    })

@app.route("/users")
def users():
    usuarios = [
        {"id": 1, "nombre": "Ana"},
        {"id": 2, "nombre": "Carlos"},
        {"id": 3, "nombre": "Lucía"}
    ]

    return jsonify(usuarios)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)