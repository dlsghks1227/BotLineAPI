from flask_restx import Api,Resource,Namespace

Accept_DataStream = Namespace('Accept_DataStream')

@Accept_DataStream.route('/<int:post_id>')
class ClientDataStream(Resource): 
    def get(self,post_id):
        return {"response" : post_id}
    
    def put(self, user_req):
        return {"response" : user_req}

    def delete(self,user_req):
        return {"response" : user_req}

@Accept_DataStream.route('/')
class Post_ClientDataStream(Resource):
    def post(self,user_req):
        return {"response" : "post"}