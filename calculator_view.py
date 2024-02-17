"""The View represents the user interface.
It displays the data from the Model and sends user inputs to the Controller."""
import tkinter as tk
from tkinter import ttk


class CalculatorView(tk.Frame):
    """Calculator class keep the interface for user"""
    def __init__(self, parent, keynames: list, column):
        super().__init__(parent)
        self.parent = parent
        self.keynames = keynames
        self.column = column
        self.options = {'sticky': tk.NSEW, 'padx': 2, 'pady': 2}
        self.value = tk.StringVar()
        self.other = ''
        self.init_components()

    def init_components(self):
        font = ('Monospace', 16)
        self.option_add('*Font', font)
        self.display = self.make_display()
        self.keypad = self.make_keypad()
        self.oppad = self.make_operator()
        self.make_otherfunc()
        self.pack_components()
        self.configure_pack()

        for button in self.keypad.winfo_children():
            button.bind("<Key>", lambda event, button1=button: self.key_bind(button1))

        for button in self.oppad.winfo_children():
            button.bind("<Key>", lambda event, button1=button: self.key_bind(button1))

    def make_keypad(self):
        """Create the keypad"""
        keypad = tk.Frame()
        row = 0
        for i, num in enumerate(self.keynames):
            tk.Button(keypad, text=num, fg='black', command=lambda x=num: self.controller.handler_click(x)).grid(row=row, column=abs(
                i % 3), **self.options)
            if i % 3 == 2:
                row += 1
        return keypad

    def make_display(self):
        """Create a display view"""
        display = tk.Label(textvariable=self.value, bg='black', foreground='yellow', height=3, anchor=tk.E,
                                justify=tk.RIGHT)
        return display

    def make_operator(self):
        """Make an operator pad"""
        oppad = tk.Frame()
        self.operations = ['+', '-', '*', '/', '^', '=', 'mod', 'DEL', 'CLR']
        for i, op in enumerate(self.operations):
            tk.Button(oppad, text=op, fg='black', bg='orange', command=lambda x=op: self.controller.handler_click(x)).grid(
                row=i, column=0, **self.options)
        other_function = tk.Button(oppad, text='Other', fg='black', bg='orange', command=lambda x=self.other: self.controller.handler_click(self.other))
        other_function.grid(row=len(self.operations)+1, column=0, **self.options)
        return oppad

    def make_otherfunc(self):
        """Make another function box"""
        choicebox = ['ln', 'log10', 'log2', 'sqrt']
        funcbox = tk.Menu()
        self.parent.config(menu=funcbox)
        funcbox_menu = tk.Menu(funcbox, tearoff=0)
        funcbox.add_cascade(label='Others', menu=funcbox_menu)
        for choice in choicebox:
            funcbox_menu.add_radiobutton(label=choice, command=lambda x=choice: self.set_other(x))
        funcbox_menu.add_separator()
        funcbox_menu.add_command(label='Exit', command=self.quit)

    def pack_components(self):
        self.display.pack(side=tk.TOP, fill=tk.X)
        self.keypad.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.oppad.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Place display
        self.display.grid_rowconfigure(0, weight=1)
        self.display.grid_columnconfigure(0, weight=1)

    def set_controller(self, controller):
        self.controller = controller

    def configure_pack(self):
        for i in range(len(self.keynames)):
            self.keypad.rowconfigure(i // self.column, weight=100)
            self.keypad.columnconfigure(i % self.column, weight=100)
        for i in range(len(self.operations)):
            self.oppad.rowconfigure(i % (len(self.operations) + 1), weight=1)
            self.oppad.columnconfigure(0, weight=1)

    def display_result(self, result):
        if result.startswith("math."):
            result = result[len("math."):]
        self.value.set(result)

    def key_bind(self, button):
        print('hi')
        num = button.cget('text')
        self.controller.handler_click(num)

    def set_other(self, choice):
        self.other = choice


if __name__ == '__main__':
    keys = list('789456123 0.')  # = ['7','8','9',...]

    root = tk.Tk()
    root.title("Keypad Demo")
    keypad = CalculatorView(root, keynames=keys, column=3)
    keypad.pack(expand=True, fill=tk.BOTH)
    root.geometry('400x500')
    root.mainloop()
