from OOP_HW_07.Logic.calc_logic import CalcLogic, MultLogic, DivLogic, SumLogic, DiffLogic


class ChoseModelFactory:

    def choose_model(self, sign: str, operandList: list):
        my_action = CalcLogic(operandList[0], operandList[1])
        match sign:
            case "*":
                my_action = MultLogic(operandList[0], operandList[1])
            case "/":
                my_action = DivLogic(operandList[0], operandList[1])
            case "+":
                my_action = SumLogic(operandList[0], operandList[1])
            case "-":
                my_action = DiffLogic(operandList[0], operandList[1])
        return my_action
