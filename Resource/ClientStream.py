from flask_restx import Api,Resource,Namespace
from queue import Queue


from Network.PacketType import ObjectType
from Controller.ObjectController import ObjectController

objectController = ObjectController()


Accept_DataStream = Namespace('Accept_DataStream')

@Accept_DataStream.route('/<int:post_id>')
class ClientDataStream(Resource): 
    def get(self,post_id):
   
        return {"response" : post_id}
    
    def put(self, post_id):
        return {"response" : post_id}

    def delete(self,post_id):
        return {"response" : post_id}


@Accept_DataStream.route('/')
class Post_ClientDataStream(Resource):
    def post(self):

        requestJson ={
            "curX" : 0,
            "curY" : 0,
            "targetX" : 2,
            "targetY" : 2,
            "stateType" : "CONTROL_WEB"
        }
        
        objectController.writeJetbotInformation(requestJson)


        