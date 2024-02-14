"""The Controller handles user input and updates the Model accordingly. It also updates the View
based on changes in the Model."""
import tkinter as tk
from calculator_view import CalculatorView
from calculator_model import CalculatorModel


class CalculatorController:
    """A class for handling user input and updating the Model"""
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def bind(self, *args):
        self.view.display_result(args)

    def handler_click(self, button):
        if button in ['+', '-', '*', '/', '^', 'mod']:
            self.model.append_operator(button)
        elif button == '=':
            result = self.model.calculate_value()
            self.view.display_result(result)
        elif button == 'CLR':
            self.model.clear_display()
            self.view.display_result('')
        elif button == 'DEL':
            self.model.delete_last_index()
            self.view.display_result(self.model.get_value())
        else:
            self.model.append_digit(button)
            self.view.display_result(self.model.get_value())


if __name__ == '__main__':
    root = tk.Tk()
    model = CalculatorModel()
    view = CalculatorView(root, list('789456123 0.'), column=3)
    controller = CalculatorController(view, model)
    view.set_controller(controller)
    view.mainloop()
