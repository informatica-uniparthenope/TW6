# App flask
from flask import Flask, jsonify, request
from flask_cors import CORS
from codicefiscale import codicefiscale

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route("/")
def root():
    return "Italian Fiscal Code Flask Demo"


#@app.route("/italian-fiscal-code", methods=['GET'])
#def get_italian_fiscal_code():
#    surname = request.args.get('surname', 'Caccamo')
#    name = request.args.get('name', 'Fabio')
#    sex = request.args.get('sex', 'M')
#    birthdate = request.args.get('birthdate', '03/04/1985')
#    birthplace = request.args.get('birthplace', 'Torino')
#    cf = codicefiscale.encode(
#        surname=surname,
#        name=name,
#        sex=sex,
#        birthdate=birthdate,
#        birthplace=birthplace)
#    result = {"italianFiscalCode": cf}
#    return jsonify(result)

@app.route("/api/italian-fiscal-code", methods=['POST'])
def post_italian_fiscal_code():
    surname = request.form.get('surname', 'Caccamo')
    name = request.form.get('name', 'Fabio')
    sex = request.form.get('sex', 'M')
    birthdate = request.form.get('birthdate', '03/04/1985')
    birthplace = request.form.get('birthplace', 'Torino')
    cf = codicefiscale.encode(
        surname=surname,
        name=name,
        sex=sex,
        birthdate=birthdate,
        birthplace=birthplace)
    result = {"italianFiscalCode": cf}
    return jsonify(result)