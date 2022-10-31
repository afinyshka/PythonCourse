from abc import ABC, abstractmethod

class CalcLogic():
    x = None
    y = None

    # def __setattr__(self, x, value):
    #     x = value
    #
    # def __setattr__(self, y, value):
    #     y = value

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
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


