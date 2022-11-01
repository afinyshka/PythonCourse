from abc import ABC, abstractmethod

class CalcLogic():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # абстрактный метод, который будет необходимо переопределять для каждого подкласса
    # @abstractmethod
    def result(self):
        pass

    def choose_model(self, sign: str, operandList: list):
        pass

class MultLogic (CalcLogic):
    def result(self):
        return self.x * self.y

class DivLogic (CalcLogic):
    def result(self):
        return self.x / self.y


class SumLogic(CalcLogic):
    def result(self):
        return self.x + self.y

class DiffLogic(CalcLogic):
    def result(self):
        return self.x - self.y


