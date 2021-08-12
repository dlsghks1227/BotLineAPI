import sys
import threading
sys.path.append('C:\\Users\\lh122\\Desktop\\BotLineAPI')

from flask import Flask, Blueprint
from flask_restx import Api,Resource,Namespace
from Resource.ClientStream import Accept_DataStream
from GlobalVariable import dataStream

# flask에서 rest api를 공부해보고
# 코드를 짜본다
app = Flask(__name__)
api = Api(app)

api.add_namespace(Accept_DataStream, '/Accept_DataStream')

class WebServer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        # 다른 스레드에서 실행하려면 디버그 모드를 해제해야합니다.
        # 디버그 모드에서는 리로더가 활성화되고 리로더는 기본적으로 기본 스레드에서 실행되어야합니다.
        app.run(debug=False)

if __name__ == '__main__':
    try:
        webServer = WebServer()
        webServer.daemon = True
        webServer.start()

        while True:
            dataStream.onUpdate()
    except KeyboardInterrupt:
        dataStream.onDestory()