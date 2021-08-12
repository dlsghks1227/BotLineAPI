from Model.InformationModel import InformationModel
from Model.ControlModel import ControlModel
from queue import Queue

from Network.Packet import *
from Resource.Packeten import InsertDataIntoPacket

# controll, accept

# 통신
class ObjectControl():

    def __init__(self, Dict):
        self.__packetQueue = Queue()
        self.__ControlModel = ControlModel()
            
    def addPacket(self):
        

        
        

 