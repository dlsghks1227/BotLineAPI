from Model.InformationModel import InformationModel
from Model.ControlModel import ControlModel

from queue import Queue

# controll, accept

# 통신
class ObjectController():

    def __init__(self):
        self.__packetQueue = Queue()
        self.__ControlModel = ControlModel()
        self.__InformationModel = InformationModel()

    def add(self):
        packet = self.__InformationModel.createPacket()
        self.__packetQueue.put(packet)

    # jetbot 정보 담는 공간
    def writeInformation(self):
        #data = dataStream().getData
        self.__InformationModel.parse(data)

    def updateJetbotInformation(self):
        pass

    def writeServerControlInformation(self):
        pass

    def sendPaceket(self):
        pass

        
        

 