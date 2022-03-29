from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

names = {
    "a7": {"age": 20, "gender": "male"},
    "mg": {"age": 22, "gender": "male"},
    "amit": {"age": 19, "gender": "male"},
    "suman": {"age": 24, "gender": "female"}
}


class HelloWorld(Resource):

    def get(self, name):
        return names[name]

    def post(self):
        return {"data": "posted"}


api.add_resource(HelloWorld, "/helloworld/<string:name>/")


if __name__ == "__main__":
    app.run(debug=True)
