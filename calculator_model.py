"""Model of calculator compose of the calculator component"""
import math
from math import *


class CalculatorModel:
    """Calculator model class that keep all the function of calculator."""
    def __init__(self):
        self.value = ''

    def append_operator(self, button):
        self.value += button

    def append_digit(self, value):
        self.value += value

    def append_other(self, value):
        self.value += "math." + value

    def clear_display(self):
        self.value = ''

    def delete_last_index(self):
        # value = self.value.split()
        self.value = self.value[:-1]

    def calculate_value(self):
        """Calculate and return the result"""
        if not self.value:
            return "Error, It's empty"
        return eval(self.value)

    def get_value(self):
        """Get the value"""
        return self.value
