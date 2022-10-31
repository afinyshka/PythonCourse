from OOP_HW_07.Logic.Calc_logic import CalcLogic, MultLogic, DivLogic, SumLogic, DiffLogic


class ChoseModelFactory:

    def choose_model(self, sign: str, operandList: list):
        my_action = CalcLogic()
        match sign:
            case "*": my_action = MultLogic()
            case "/": my_action = DivLogic()
            case "+": my_action = SumLogic()
            case "-": my_action = DiffLogic()
        my_action.set_x(operandList[0])
        my_action.set_y(operandList[1])
        return my_action
