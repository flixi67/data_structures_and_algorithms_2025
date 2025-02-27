from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/hello/<city>")
def hello(city):
    return f"<h1>Hello, {city}!</h1>"

@app.route('/')
def home():
    return render_template('calc.html')

@app.route('/calculate', methods=['POST'])  # associating the POST method with this route
def calculate():

    # using the request method from flask to request the values that were sent to the server through the POST method
    value1 = request.form['value1']
    value2 = request.form['value2']
    operation = str(request.form['operation'])

    # convert the input to floating points
    value1 = float(value1)
    value2 = float(value2)

    if operation == 'addition':
        return render_template('calc.html', printed_result=str(value1 + value2))
    if operation == "substraction":
        return render_template('calc.html', printed_result=str(value1 - value2))
    if operation == "multiplication":
        return render_template('calc.html', printed_result=str(value1 * value2))
    if operation == "division":
        return render_template('calc.html', printed_result=str(value1 / value2))
    else:
        return render_template('calc.html', printed_result='Operation must be "addition"')

if __name__ == '__main__':
    app.run(debug=True)