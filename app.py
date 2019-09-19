from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/register')
def register():
    return render_template('register.htm')


@app.route('/')
def hello():
    return 'Hello World'


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
