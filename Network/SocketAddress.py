class SocketAddress:
    def __init__(self, ip="0.0.0.0", port=0) -> None:
        self.__ip = ip
        self.__port = port

    @property
    def address(self) -> tuple:
        return self.__ip, self.__port
