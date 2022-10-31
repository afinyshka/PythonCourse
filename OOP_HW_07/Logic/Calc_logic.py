from abc import ABC, abstractmethod

class Calc_logic(ABC):
    x = None
    y = None

    # def __setattr__(self, x, value):
    #     x = value
    #
    # def __setattr__(self, y, value):
    #     y = value

    def set_y(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    # абстрактный метод, который будет необходимо переопределять для каждого подкласса
    @abstractmethod
    def result(self):
        pass

class Mult_Logic (Calc_logic):
    def result(self):
        return self.x * self.y

class Div_Logic (Calc_logic):
    def result(self):
        return self.x / self.y


class Sum_Logic(Calc_logic):
    def result(self):
        return self.x + self.y

class Diff_Logic(Calc_logic):
    def result(self):
        return self.x - self.y


