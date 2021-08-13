
#dataStreamThread는 model에서만 불러올 수 있다.

import enum
from enum import Enum
from typing import ValuesView

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
        for key, value in threadData.values():
            self.__setattr__(key, value)
    
    # dataStreamThread.getData() returns dict
    def parse(self, threadData):
        self.write(threadData)

    def update(self):
        outputPacket = OutputPacket(ObjectType.WEB)
        outputPacket.writeCommand(Message.CONTROL_WEB)

        for value in self.__dict__.values():
            outputPacket.writeUInt32(value)

        return outputPacket

        


        

