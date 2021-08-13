import queue
from Model.InformationModel import InformationModel
from Model.ControlModel import ControlModel

from queue import Queue

from GlobalVariable import dataStream

# controll, accept
# 통신
class ObjectController():

    def __init__(self):
        self.__ControlModel = ControlModel()
        self.__InformationModel = InformationModel()

    def add(self):
        packet = self.__InformationModel.insert()
        self.__packetQueue.put(packet)

    # jetbot 정보 담는 공간
    def writeInformation(self):
        data = dataStream.getData()
        self.__InformationModel.parse(data)

    def sendPacket(self):
        self.__ControlModel

    def updateJetbotInformation(self):
        pass

    def writeServerControlInformation(self):
        pass


        
        

 