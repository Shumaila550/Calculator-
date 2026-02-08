class Calculator:
    def calculate(self, a, b, op):
        a, b = float(a), float(b)

        if op == "+": return a + b
        if op == "-": return a - b
        if op == "*": return a * b
        if op == "/": return "Error" if b == 0 else a / b

    def percent(self, a):
        return float(a)/100

    def square(self, a):
        return float(a)**2

    def sqrt(self, a):
        return float(a)**0.5

    def inverse(self, a):
        return "Error" if float(a) == 0 else 1/float(a)
