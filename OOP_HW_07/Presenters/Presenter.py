from OOP_HW_07.Logic.Calc_logic import CalcLogic
from OOP_HW_07.Logic.Chose_logic_factory import ChoseModelFactory
from OOP_HW_07.Views.View import View
from OOP_HW_07.Loggers import Logger



class Presenter:
    calc = ChoseModelFactory()
    view = View()

    def __init__(self, calc, view):
        self.calc = calc
        self.view = view

    def button_click(self):
        a = self.view.get_value("first number")
        sign = self.view.get_sign("math char")
        b = self.view.get_value("second number")
        my_list = [a, b]
        c = self.calc.choose_model(sign, my_list).result()
        strr = f"{a} {sign} {b} = {c}"
        View.show_result(strr)
        Logger.get_log(c, f"{a} {sign} {b}")

