from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

POKEAPI_URL = "https://pokeapi.co/api/v2/pokemon/"

@app.route('/pokemon/<name>', methods=['GET'])
def get_pokemon(name):
    try:
        # Solicitud a PokeAPI
        response = requests.get(f"{POKEAPI_URL}{name}")
        
        # Verificar si la respuesta es exitosa
        if response.status_code == 200:
            data = response.json()
            return jsonify({
                "name": data["name"],
                "id": data["id"],
                "height": data["height"],
                "weight": data["weight"],
                "types": [t["type"]["name"] for t in data["types"]]
            }), 200
        elif response.status_code == 404:
            return jsonify({"error": "Pokémon not found"}), 404
        else:
            return jsonify({"error": "Error fetching data from PokeAPI"}), response.status_code

    except requests.exceptions.RequestException:
        # Error de conexión o problemas con PokeAPI
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True)
