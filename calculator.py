import tkinter as tk
from tkinter import messagebox
import ast
import operator

# -----------------------------
# Safe Calculator Logic
# -----------------------------
OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.USub: operator.neg
}

def safe_eval(expression):
    """
    Safely evaluate a mathematical expression using AST
    """
    try:
        return eval_node(ast.parse(expression, mode='eval').body)
    except Exception:
        return "Error"

def eval_node(node):
    if isinstance(node, ast.Num):
        return node.n
    elif isinstance(node, ast.BinOp):
        return OPERATORS[type(node.op)](
            eval_node(node.left),
            eval_node(node.right)
        )
    elif isinstance(node, ast.UnaryOp):
        return OPERATORS[type(node.op)](
            eval_node(node.operand)
        )
    else:
        raise ValueError("Invalid Expression")

# -----------------------------
# GUI Application
# -----------------------------
class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Professional Python Calculator")
        self.geometry("320x420")
        self.resizable(False, False)

        self.expression = tk.StringVar()

        self.create_display()
        self.create_buttons()

    def create_display(self):
        entry = tk.Entry(
            self,
            textvariable=self.expression,
            font=("Segoe UI", 20),
            bd=8,
            relief=tk.RIDGE,
            justify="right"
        )
        entry.pack(fill="x", padx=10, pady=10)

    def create_buttons(self):
        buttons = [
            ("7", self.add), ("8", self.add), ("9", self.add), ("/", self.add),
            ("4", self.add), ("5", self.add), ("6", self.add), ("*", self.add),
            ("1", self.add), ("2", self.add), ("3", self.add), ("-", self.add),
            ("0", self.add), (".", self.add), ("=", self.calculate), ("+", self.add),
        ]

        frame = tk.Frame(self)
        frame.pack()

        row, col = 0, 0
        for text, cmd in buttons:
            tk.Button(
                frame,
                text=text,
                width=6,
                height=2,
                font=("Segoe UI", 14),
                command=lambda t=text, c=cmd: c(t)
            ).grid(row=row, column=col, padx=5, pady=5)

            col += 1
            if col == 4:
                col = 0
                row += 1

        # Control Buttons
        control_frame = tk.Frame(self)
        control_frame.pack(pady=5)

        tk.Button(
            control_frame,
            text="Clear",
            width=12,
            height=2,
            font=("Segoe UI", 12),
            bg="#e0e0e0",
            command=self.clear
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            control_frame,
            text="⌫ Back",
            width=12,
            height=2,
            font=("Segoe UI", 12),
            bg="#e0e0e0",
            command=self.backspace
        ).grid(row=0, column=1, padx=5)

    def add(self, value):
        self.expression.set(self.expression.get() + value)

    def clear(self):
        self.expression.set("")

    def backspace(self):
        self.expression.set(self.expression.get()[:-1])

    def calculate(self, _=None):
        result = safe_eval(self.expression.get())
        self.expression.set(result)

# -----------------------------
# Run App
# -----------------------------
if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
