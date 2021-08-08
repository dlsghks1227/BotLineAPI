import threading
import time

from Network.Packet import *
from Network.SocketAddress import SocketAddress
from Network.NetworkObject import NetworkObject

from Util.Log import Log


class DataStreamThread(threading.Thread):
    def __init__(self) -> None:
        super().__init__()

        self.__isRunning = True
        self.__networkObject = NetworkObject(SocketAddress("localhost", 8080))

    def onUpdate(self, elapsedTime: float) -> None:
        self.__networkObject.onUpdate(elapsedTime)

    def onDestory(self) -> None:
        self.__networkObject.onDestory()

    def run(self) -> None:
        currentTime = 0.0
        elapsedTime = 0.0
        while self.__isRunning:
            currentTime = time.perf_counter()
            self.onUpdate(elapsedTime)
            elapsedTime = time.perf_counter() - currentTime
        self.onDestory()

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
        dataStreamThread = DataStreamThread()
        dataStreamThread.start()

        dataStreamThread.getData()

        outputPacket = OutputPacket(ObjectType.WEB)
        outputPacket.writeCommand(MessageType.CONNECT)
        dataStreamThread.addSendData(outputPacket)

    except KeyboardInterrupt:
        dataStreamThread.isRunning = False
        dataStreamThread.join()
