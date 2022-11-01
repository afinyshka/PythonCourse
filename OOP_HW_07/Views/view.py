class View:
    def get_value(self, string_name: str) -> float:
        return input(f'{string_name}: ')

    def get_sign(self, string_name: str) -> str:
        return input(f'{string_name}: ')

    def show_result(string_name: str) -> None:
        print(string_name)
