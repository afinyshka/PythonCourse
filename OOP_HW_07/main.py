from OOP_HW_07.Logic.chose_logic_factory import ChoseModelFactory
from OOP_HW_07.Controllers.controller import Controller
from OOP_HW_07.Views.view import View


pr = Controller(ChoseModelFactory(), View()).button_click()
