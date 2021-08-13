import threading
import time

from Network.Packet import *
from Network.SocketAddress import SocketAddress
from Network.NetworkObject import NetworkObject

from Util.Log import Log


class DataStream:
    def __init__(self) -> None:
        super().__init__()

        self.__currentTime = 0.0
        self.__elapsedTime = 0.0

        self.__isRunning = True
        self.__networkObject = NetworkObject(SocketAddress("localhost", 8000))

    def onUpdate(self) -> None:
        self.__currentTime = time.perf_counter()
        self.__networkObject.onUpdate(self.__elapsedTime)
        self.__elapsedTime = time.perf_counter() - self.__currentTime

    def onDestory(self) -> None:
        self.__networkObject.onDestory()

    def addSendData(self, data: OutputPacket) -> None:
        self.__networkObject.addSendData(data)

    def getData(self) -> dict:
        return self.__networkObject.getData()

    @property
    def isRunning(self) -> bool:
        return self.__isRunning

    @isRunning.setter
    def isRunning(self, isRunning: bool) -> None:
        self.__isRunning = isRunning


if __name__ == "__main__":
    try:
        dataStreamThread = DataStream()
        dataStreamThread.start()

        dataStreamThread.getData()

        # outputPacket = OutputPacket(ObjectType.WEB)
        # outputPacket.writeCommand(MessageType.CONNECT)
        # .addSendData(outputPacket)

    except KeyboardInterrupt:
        dataStreamThread.isRunning = False
        dataStreamThread.join()