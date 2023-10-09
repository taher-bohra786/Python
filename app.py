from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, Taher!</h1>"

@app.route("/hello_world2")
def hello_world2():
    return "<h2>Hello, Taher great!</h2>"

@app.route("/hello_world3")
def hello_world3():
    return "<h3>Hello, Taher The Great!</h3>"

@app.route("/test")
def test():
    a = 5+6
    return "This is my func to run app {}".format(a)

@app.route("/test2/test2")
def test2():
    data = request.args.get('x')
    return "this is a data input for my url {}".format(data)

if __name__=="__main__":
    app.run(host="0.0.0.0")
