import socket

from Network.SocketAddress import SocketAddress
from Network.Packet import *


class UDPSocket:
    def __init__(self, address: SocketAddress, bufferSize: int = 2048) -> None:
        self.__bufferSize = bufferSize

        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__socket.setblocking(False)

    def onDestory(self) -> None:
        self.__socket.close()

    def sendTo(self, outputPacket: OutputPacket, address: SocketAddress) -> None:
        self.__socket.sendto(outputPacket.data, address.address)

    def receiveFrom(self) -> tuple:
        try:
            data, address = self.__socket.recvfrom(self.__bufferSize)
            if len(data) >= 0:
                return data, address
        except ConnectionResetError:
            return (-1, )
        except BlockingIOError:
            return (None, )
