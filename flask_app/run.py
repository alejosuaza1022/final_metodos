from flask_cors import CORS
from flask import Flask, jsonify, request
import os
import boto3
from dotenv import load_dotenv
# ours
from helpers.upload_files import graph_rk, graph_lr
from helpers.methods import rk4, superior, modelo_regresion
from error_handler import set_error_handler

load_dotenv('.env')


app = Flask(__name__)
CORS(app)
set_error_handler(app)

s3_client = boto3.client('s3', aws_access_key_id=os.getenv(
    'AWS_ACCESS_KEY_ID'), aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))


@app.route('/linear_regression', methods=['POST'])
def index():
    data = request.json
    x, y = data.get('x'), data.get('y')
    if len(x) != len(y):
        raise Exception(
            'Error on length of the arrays, the arrays has to have the same')
    CoefCorr, intercepto, pendiente, yest = modelo_regresion(x, y)
    link = graph_lr(s3_client, 'linear_regression', x, y, yest, CoefCorr)
    return jsonify({"R": CoefCorr, "intercepto": intercepto, "pendiente": pendiente, "yest": yest.tolist(), "link": link})


@app.route('/rk-4', methods=['POST'])
def rk4_post():
    data = request.json
    x, y, f, h, xi, xf = data.get('x'), data.get('y'), data.get(
        'f'), data.get('h'), data.get('xi'), data.get('xf')
    x, y = rk4(float(x), float(y), f, float(h), float(xi), float(xf))
    link = graph_rk(s3_client, 'runge_kutta_4to_orden', x, y, f, aux=1)
    return jsonify({"link": link, "x": x, "y": y})


@app.route('/rk-orden-superior', methods=['POST'])
def rks():
    data = request.json
    x, y, f, h, xi, xf = data.get('x'), data.get('y'), data.get(
        'f'), data.get('h'), data.get('xi'), data.get('xf')
    x, y = superior(float(x), float(y), f, float(h), float(xi), float(xf))
    link = graph_rk(s3_client, 'runge_kutta_orden_superior', x, y, f)
    return jsonify({"link": link, "x": x, "y": y})


if __name__ == '__main__':
    app.run(debug=True)
