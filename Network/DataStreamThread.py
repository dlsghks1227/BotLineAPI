import threading
import time

from Network.SocketAddress import SocketAddress
from Network.NetworkObject import NetworkObject

from Util.Log import Log


class DataStreamThread(threading.Thread):
    def __init__(self) -> None:
        super().__init__()

        self.__isRunning = True
        self.__networkObject = NetworkObject(SocketAddress("localhost", 8080))

    def onUpdate(self, elapsedTime: float) -> None:
        self.__currentTime = time.perf_counter()
        self.__networkObject.onUpdate(elapsedTime)
        self.__elapsedTime = time.perf_counter() - self.__currentTime

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
        print(dataStreamThread.getData())
    except KeyboardInterrupt:
        dataStreamThread.isRunning = False
        dataStreamThread.join()