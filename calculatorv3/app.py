from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate():
    # Initialize result and error message
    result = None
    error = None

    if request.method == 'POST':
        try:
            num1 = request.form.get("num1", type=float, default=0)
            num2 = request.form.get("num2", type=float, default=0)
            operation = request.form.get("operation")

            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                if num2 != 0:
                    result = num1 / num2
                else:
                    error = "Division by zero is not allowed."
            else:
                error = "Invalid operation selected."
        except ValueError:
            error = "Invalid input. Please enter valid numbers."

    return render_template('form.html', result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True)
