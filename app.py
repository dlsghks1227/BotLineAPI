from flask import Flask, Blueprint
from flask_restx import Api,Resource,Namespace
from Resource.ClientStream import Accept_DataStream
# flask에서 rest api를 공부해보고
# 코드를 짜본다
app = Flask(__name__)
api = Api(app)

api.add_namespace(Accept_DataStream, '/Accept_DataStream')


if __name__ == '__main__':
    app.run()
