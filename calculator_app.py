import tkinter as tk
from calculator_model import CalculatorModel
from calculator_view import CalculatorView
from calculator_controller import CalculatorController

if __name__ == "__main__":
    root = tk.Tk()
    model = CalculatorModel()
    view = CalculatorView(root, list('e H789456123)0.'), column=3)
    controller = CalculatorController(view, model)
    view.set_controller(controller)
    root.title("Calculator")
    root.geometry('400x490')
    view.pack(expand=True, fill=tk.BOTH)
    root.mainloop()
