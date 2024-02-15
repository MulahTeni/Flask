from flask import Flask, request, jsonify
import numbers

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()

    num1 = data.get('num1')
    num2 = data.get('num2')
    operation = data.get('operation')

    if not isinstance(num1, numbers.Number) or not isinstance(num2, numbers.Number):
        return jsonify({"error": "'num1' and 'num2' must be numeric values."})
        
    if operation not in ['+', '-', '*', '/']:
        return jsonify({"error": "Invalid operation. Please choose from +, -, *, /"})

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

    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
