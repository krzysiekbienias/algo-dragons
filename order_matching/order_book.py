
class OrderBookInterface:
    def __init__(self):
        pass

    def validate_command(self):
        pass

    def add_new_trade(self):
        pass

    def ammend_trade(self):
        pass

    def match(self):
        pass

    def generate_random_trade(self):
        pass

    def cancel_trade(self):
        pass


class Commandhandler:
    def __init__(self, command: str) -> None:
        self._command = command

    def parse_command_2_hm(self):
        pass