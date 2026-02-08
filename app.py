from flask import Flask, render_template, request

app = Flask(__name__)

def calculate(a, b, op):
    a = float(a)
    b = float(b)

    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        if b == 0:
            return "Error"
        return a / b

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        num1 = request.form["num1"]
        num2 = request.form["num2"]
        operator = request.form["operator"]
        result = calculate(num1, num2, operator)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
