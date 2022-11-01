from OOP_HW_07.Logic.Chose_logic_factory import ChoseModelFactory
from OOP_HW_07.Presenters.Presenter import Presenter
from OOP_HW_07.Views.View import View


calc = ChoseModelFactory()
view = View()
pr = Presenter(calc, view).button_click()
