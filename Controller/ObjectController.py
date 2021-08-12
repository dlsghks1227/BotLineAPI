from Model.ControlModel import ControlModel
from Model.InformationModel import InformationModel

class ObjectController:
    def __init__(self):
        self.__controlModel = ControlModel()
        self.__InformationModel = InformationModel()

    def createControllMessage(self):
        self.__controlModel.send()
        pass

    def updateJetbotInformation(self):
        return self.__InformationModel.get()