# dataStreamThread는 Model에서만 호출
# dataStreamThread는 서버 -> 웹 방향으로 흐른다.


# 총체적인 컨트롤 모델
class ControlModel:

    def __init__(self):
        pass
    
    def send(self):
        print("send")

    