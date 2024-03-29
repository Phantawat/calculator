"""The Controller handles user input and updates the Model accordingly. It also updates the View
based on changes in the Model."""


class CalculatorController:
    """A class for handling user input and updating the Model"""
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def handler_click(self, button):
        """Method for handler clicked"""
        if button in ['+', '-', '*', '/']:
            self.model.append_operator(button)
        elif button == '^':
            self.model.append_operator('**')
        elif button == 'mod':
            self.model.append_operator('%')
        elif button == 'ln':
            self.model.append_other('log(')
        elif button == 'log10':
            self.model.append_other('log10(')
        elif button == 'log2':
            self.model.append_other('log2(')
        elif button == 'sqrt':
            self.model.append_other('sqrt(')
        elif button == 'H':
            if self.view.h == 'open':
                self.view.hide_history()
            elif self.view.h == 'close':
                self.view.show_history()
        elif button == '=':
            result = self.model.calculate_value()
            if result:
                self.view.display_result(str(result))
                self.view.add_to_history(self.model.get_value())
                self.view.add_to_history(str(result))
            else:
                self.view.display_result(str(result))
        elif button == 'CLR':
            self.model.clear_display()
            self.view.display_result('')
        elif button == 'DEL':
            self.model.delete_last_index()
            self.view.display_result(self.model.get_value())
        else:
            self.model.append_digit(button)
            self.view.display_result(self.model.get_value())
