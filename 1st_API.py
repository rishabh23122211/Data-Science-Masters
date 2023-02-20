from flask import Flask
from flask import request

app = Flask(__name__) ##object variable

@app.route("/")        ##decorate with route
def hello_world():
    return "Hello, World!"

@app.route("/hello1")        ##decorate with route
def hello_world1():
    return "Hello, World!1"

@app.route("/hello2")        ##decorate with route
def hello_world2():
    return "Hello, World!2"
@app.route('/test_fun')
def test():
    a=5+6
    return "This is my fun in flask:  {}".format(a)

@app.route('/input_url')
def rishabh():
    data=request.args.get('x')
    return "This is my input from URL {}".format(data)


if __name__=="__main__":
    app.run(host="0.0.0.0") ##https protocol
