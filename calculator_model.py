"""Model of calculator compose of the calculator component"""
import math
from math import *


class CalculatorModel:
    """Calculator model class that keep all the function of calculator."""

    def __init__(self):
        self.value = ''
        self.history = ''
        self.last_in = []

    def append_operator(self, button):
        self.value += button
        self.last_in.append('operator')

    def append_digit(self, value):
        self.value += value
        self.last_in.append('digit')

    def append_other(self, value):
        self.value += "math." + value
        self.last_in.append('function')

    def clear_display(self):
        self.value = ''
        self.last_in.pop()

    def delete_last_index(self):
        """Delete last string in display"""
        if not self.last_in:
            return
        last = self.last_in[-1]
        if last == 'operator' or last == 'digit':
            self.delete_last_character()
        elif last == 'function':
            self.delete_function_input()
        else:
            self.delete_last_character()
        self.last_in.pop()

    def delete_last_character(self):
        """Delete last number or operation"""
        self.value = self.value[:-1]

    def delete_function_input(self):
        """Delete last function input"""
        if self.value.endswith('sqrt(') or self.value.endswith('log2('):
            self.value = self.value[:-10]
        elif self.value.endswith('log('):
            self.value = self.value[:-9]
        elif self.value.endswith('log10('):
            self.value = self.value[:-11]

    def calculate_value(self):
        """Calculate and return the result"""
        if not self.value:
            return "Error, It's empty"
        result = eval(self.value)
        if result:
            self.history += str(result)
            return result
        return None

    def get_value(self):
        """Get the value"""
        return self.value
