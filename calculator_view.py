"""The View represents the user interface.
It displays the data from the Model and sends user inputs to the Controller."""
import tkinter as tk
from  playsound import playsound
from tkinter import ttk


class CalculatorView(tk.Frame):
    """Calculator class keep the interface for user"""
    def __init__(self, parent, keynames: list, column):
        super().__init__(parent)
        self.h = 'close'
        self.parent = parent
        self.keynames = keynames
        self.column = column
        self.options = {'sticky': tk.NSEW, 'padx': 2, 'pady': 2}
        self.value = tk.StringVar()
        self.history_list = []
        self.other = ''
        self.init_components()

    def init_components(self):
        font = ('Monospace', 16)
        self.option_add('*Font', font)
        self.display = self.make_display()
        self.keypad = self.make_keypad()
        self.oppad = self.make_operator()
        self.history = self.make_history_chooser()
        self.history.pack_forget()
        self.make_otherfunc()
        self.pack_components()
        self.configure_pack()

        # for button in self.keypad.winfo_children():
        #     button.bind("<Button-1>", self.invalid_input)
        #
        # for button in self.oppad.winfo_children():
        #     button.bind("<Button-1>", self.invalid_input)

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

    def make_history_chooser(self):
        """A menu for get history back"""
        history_list = tk.Listbox(self, height=5, width=50)
        history_list.bind('<Double-Button-1>', self.recall_history)
        return history_list

    def recall_history(self, event):
        """Recall history back"""
        index = self.history.curselection()[0]
        value = self.history_list[index]
        self.display_result(value)

    def pack_components(self):
        self.display.pack(side=tk.TOP, fill=tk.X)
        self.keypad.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.oppad.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Place display
        self.display.grid_rowconfigure(0, weight=1)
        self.display.grid_columnconfigure(0, weight=1)

    def set_controller(self, controller):
        self.controller = controller

    def set_value(self, value):
        self.value.set(value)

    def configure_pack(self):
        for i in range(len(self.keynames)):
            self.keypad.rowconfigure(i // self.column, weight=100)
            self.keypad.columnconfigure(i % self.column, weight=100)
        for i in range(len(self.operations)):
            self.oppad.rowconfigure(i % (len(self.operations) + 1), weight=1)
            self.oppad.columnconfigure(0, weight=1)

    def display_result(self, result):
        if "math." in result:
            result = result.replace("math.", "", 1)
        if result == 'None':
            self.display.config(fg='red')
        else:
            self.value.set(result)

    def add_to_history(self, entry):
        self.history_list.append(entry)
        self.history.insert(tk.END, entry)

    def recall_from_history(self, event):
        index = self.history.curselection()[0]
        value = self.history_list[index]
        self.display_result(value)

    def show_history(self):
        self.history.pack(side=tk.TOP, fill=tk.X)
        self.h = 'open'

    def hide_history(self):
        self.history.pack_forget()
        self.h = 'close'

    def invalid_input(self, *args):
        """Check input if it's a number"""
        value = self.value.get()
        try:
            eval(value)
            self.display.config(fg='yellow')
        except SyntaxError:
            self.display.config(fg='red')

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
