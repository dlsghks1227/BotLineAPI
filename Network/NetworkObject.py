from Util.Log import Log

from Network.BaseObject import BaseObject
from Network.SocketAddress import SocketAddress
from Network.Packet import *
from Network.PacketType import *

class NetworkObject(BaseObject):
    def __init__(self, hostAddress: SocketAddress) -> None:
        super().__init__(hostAddress)

    def onUpdate(self, elapsedTime: float) -> None:
        super().onUpdate(elapsedTime)

    def onDestory(self) -> None:
        super().onDestory()

    def getData(self) -> dict:
        return {
            "Jetbot1": {
                "Voltage" : 12.1,
                "Memory" : 50.3,
                "CPU" : 1.2,
                "Disk" : 36.4
            }
        }