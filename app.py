from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World :)</h1>'


# @app.route('/greet')
# def greet():
#     return 'Hello'
#
#
# @app.route('/greet/<name>')
# def greet(name=""):
#     return f"Hello {name}"


def calculate_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


@app.route('/calculate/<value>')
def calculate(value=0.0):
    return f"{calculate_fahrenheit(value)}" # IDK I dont get this


if __name__ == '__main__':
    app.run()
