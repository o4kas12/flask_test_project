from flask import Flask
from flask import render_template

app = Flask(__name__)

maintext = ""

@app.route('/')
def hello():
    return render_template('hello.html', x=maintext)


if __name__ == '__main__':
    app.run()
