from flask import Flask, jsonify, request,abort #importo l oque necesito
import dieta_controller_poo
from dieta_db import create_tables
from exchange_rate import get_xr
from dieta_db import get_db

app = Flask(__name__)

#comienzo a hacer las rutas que son las que va a usar el usuario para acceder a los datos
@app.route('/api/dreamfly/dieta', methods=["GET"])
def get_dietas():
    dietas = dieta_controller_poo.get_dietas()
    dietas_list=[]
    for dieta in dietas:
        elem = dieta.serialize()
        dietas_list.append(elem)
    return jsonify(dietas_list)

@app.route("/api/dreamfly/dieta", methods=["POST"])
def insert_dieta():
    dieta_details = request.get_json()
    id= dieta_details["id"]
    restriction = dieta_details["restriction"]
    restriccion =dieta_details["restriccion"]
    USD = dieta_details["USD"]
    result = dieta_controller_poo.insert_dieta(id,restriction,restriccion,USD)
    return jsonify(result)


@app.route("/api/dreamfly/dieta/eliminate/<id>", methods=["DELETE"])
def delete_dieta(id):
    result = dieta_controller_poo.delete_dieta(id)
    return jsonify(result)


@app.route("/api/dreamfly/dieta/<id>", methods=["GET"])
def get_dieta_by_id(id):
    dieta = dieta_controller_poo.get_by_id(id)
    return jsonify(dieta)


@app.route("/api/dreamfly/dieta/<id>/pais/ARG", methods=["GET"])
def get_dieta_by_id_psa(id):
    try:
        dieta = dieta_controller_poo.get_by_id(id)

        if dieta is None:
            return "El ID de dieta proporcionado no existe.", 404

        xr = get_xr()
        price_usd = dieta['USD'] * xr
        dieta['USD'] = round(price_usd, 2)

        response_text = f"Para el menú {id}, la dieta {dieta['restriccion']} tiene un precio de {price_usd} pesos argentinos."
        return response_text
    except Exception as e:
        return f"Error: {str(e)}", 400


create_tables()

if __name__ == '__main__':
    app.run()
