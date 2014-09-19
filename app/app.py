from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/version/')
@app.route('/version/<host>')
def hello(host=None):
    return render_template('versions.html', host=host)

if __name__ == '__main__':
    app.debug = True
    app.run(port=4000)
