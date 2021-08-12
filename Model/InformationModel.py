#dataStreamThread는 model에서만 불러올 수 있다.

import enum
from Network.DataStreamThread import DataStreamThread
from enum import Enum

from Network.Packet import OutputPacket
from Network.PacketType import MessageType, ObjectType


class Message(Enum):
    CONTROL_WEB = 0x11,
    CONTROL_SERVER = 0x12,


# 데이터 처리 모델
class InformationModel:

    # init에서 모든 데이터를 다 선언해줘야하나?
    def __init__(self):
        self.curX = None
        self.curY = None
        self.targetX = None
        self.targetY = None
        self.stateType = ""

    def get(self):
        return self.__dict__

    def set(self):
        pass

    def write(self, threadData : dict):
        keyList = threadData.keys()
    
        for i in keyList:
            self.__setattr__(i, threadData.get(i))
    
    # dataStreamThread.getData() returns dict
    def parse(self, threadData):
        self.write(threadData)

    # Web -> Server
    def createPacket(self):
        outputPacket = OutputPacket(ObjectType.WEB)
        outputPacket.writeCommand(Message.CONTROL_WEB)
        
        outputPacket.writeUInt32(self.__curX)
        outputPacket.writeUInt32(self.__curY)
        outputPacket.writeUInt32(self.__targetX)
        outputPacket.writeUInt32(self.__targetY)

        return outputPacket
    

        #DataStream.addSendTo(outputPacket)