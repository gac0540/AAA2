from flask import Flask

app = Flask(__name__)

sql1 = 'alsdkjflaskdfja'
sql2 = 'fsafdsdadfdsa'

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route()

if __name__ == '__main__':
    app.run()
