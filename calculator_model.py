"""Model of calculator compose of the calculator component"""


class CalculatorModel:
    """Calculator model class that keep all the function of calculator."""
    def __init__(self):
        self.value = ''

    def append_operator(self, button):
        self.value += button

    def append_digit(self, value):
        self.value += value

    def clear_display(self):
        self.value = ''

    def delete_last_index(self):
        self.value = self.value[:-1]

    def calculate_value(self):
        """Calculate and return the result"""
        try:
            result = eval(self.value)
            return result
        except Exception as e:
            return "Error: " + str(e)

    def get_value(self):
        """Get the value"""
        return self.value
