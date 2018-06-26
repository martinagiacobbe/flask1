from flask import Flask, render_template, request, json
from flaskext.mysql  import MySQL
app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')

@app.route("/")

def main():
    return render_template('index2.html')


def hello():
    return "Hello world"
if __name__=="__main__":
    app.run()
