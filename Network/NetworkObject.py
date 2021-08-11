from Util.Log import Log
from queue import Queue

from Network.BaseObject import BaseObject
from Network.SocketAddress import SocketAddress
from Network.Packet import *
from Network.PacketType import *


class NetworkObject(BaseObject):
    def __init__(self, hostAddress: SocketAddress) -> None:
        super().__init__(hostAddress)

        self.__sendDataQueue = Queue()

    def onUpdate(self, elapsedTime: float) -> None:
        super().onUpdate(elapsedTime)

        while not self.__sendDataQueue.empty():
            data = self.__sendDataQueue.get()
            self._networkManager.sendTo(data, self._hostAddress)

    def onDestory(self) -> None:
        super().onDestory()

    def addSendData(self, data: OutputPacket) -> None:
        self.__sendDataQueue.put(data)

    def getData(self) -> dict:
        return {
            "Jetbot1": {
                "Voltage": 12.1,
                "Memory": 50.3,
                "CPU": 1.2,
                "Disk": 36.4
            }
        }