import Calc_logic as cl

class ChoseModelFactory ():

    def choose_model(sign: str, operandList: list) -> cl.Calc_logic:
        my_action = cl.Calc_logic()
        match (sign):
            case "*": my_action = cl.Mult_Logic
            case "/": my_action = cl.Div_Logic
            case "+": my_action = cl.Sum_Logic
            case "-": my_action = cl.Diff_Logic
        my_action.setX(operandList[0])
        my_action.setY(operandList[1])
