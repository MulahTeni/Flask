from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def welcome():

    return render_template('form.html')


@app.route('/', methods=['POST'])
def calculate():

    num1 = request.form.get("num1", type=int, default=0)
    num2 = request.form.get("num2", type=int, default=0)
    operation = request.form.get("operation")

    result = 0

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return jsonify({"error": "Division by zero is not allowed"})
    else:
        return jsonify({"error": "Input either -, +, *, / into the operation box"})
        
    return render_template('form.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
