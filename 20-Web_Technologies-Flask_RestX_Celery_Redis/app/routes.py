from celery.result import AsyncResult
from flask import request, jsonify
from flask_restx import Api, Resource,fields

from run import flask_app
from . import tasks

# Create the api object using restx
api = Api(flask_app)

add_model = api.model("add", {
    "a": fields.Integer(0),
    "b": fields.Integer(0)
})

@api.route('/result/<string:id>')
class Result(Resource):
    def get(self, id):
        result = AsyncResult(id)

        ready = result.ready()
        return jsonify({
            "ready": ready,
            "successful": result.successful() if ready else None,
            "value": result.get() if ready else result.result,
        })


@api.route("/add")
@api.expect(add_model)
class Add(Resource):
    def post(self):
        a = int(api.payload["a"])
        b = int(api.payload["b"])
        result = tasks.add.delay(a, b)
        return jsonify({"result_id": result.id})


@api.route("/block")
class Block(Resource):
    def post(self):
        result = tasks.block.delay()
        return jsonify({"result_id": result.id})


@api.route("/process")
class Process(Resource):
    def post(self):
        result = tasks.process.delay(total=request.form.get("total", type=int))
        return jsonify({"result_id": result.id})
