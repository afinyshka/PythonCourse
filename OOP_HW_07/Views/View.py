from fractions import Fraction
class View:
    def get_value(self, string_name: str) -> float:
        value = input(f'{string_name}: ')
        try:
            value = Fraction(value)
            return value
        except ValueError:
            value = complex(value)
            return value

    def get_sign(self, string_name: str) -> str:
        return input(f'{string_name}: ')

    def show_result(string_name: str) -> None:
        print(string_name)
