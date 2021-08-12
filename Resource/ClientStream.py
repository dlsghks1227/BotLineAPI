from flask_restx import Api, Resource, Namespace
from Controller.ObjectController import ObjectController

Accept_DataStream = Namespace('Accept_DataStream')

objectController = ObjectController()

@Accept_DataStream.route('/<int:post_id>')
class ClientDataStream(Resource): 
    def get(self,post_id):
        objectController.createControllMessage()
        return {"response" : post_id}
    
    # def put(self, user_req):
    #     return {"response" : user_req}

    # def delete(self,user_req):
    #     return {"response" : user_req}

@Accept_DataStream.route('/')
class Post_ClientDataStream(Resource):
    def post(request):
        objectController.updateJetbotInformation()
        return {"response" : "post"}