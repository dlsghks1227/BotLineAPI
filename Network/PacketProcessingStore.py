from typing import Callable

from Network.SocketAddress import SocketAddress
from Network.Packet import *


class PacketProcessingStore:
    def __init__(self) -> None:
        self.__commands = dict()

    def add(self, command: MessageType, handler: Callable[[InputPacket, SocketAddress], OutputPacket]) -> None:
        self.__commands[command] = handler

    def run(self, command: MessageType, inputPacket: InputPacket, address: SocketAddress) -> OutputPacket:
        if command in self.__commands:
            return self.__commands[command](inputPacket, address)
        else:
            return None