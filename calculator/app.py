from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()

    num1 = data['num1']
    num2 = data['num2']
    operation = data['operation']

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
        return jsonify({"error": "Input either -, +, *, /"})
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
