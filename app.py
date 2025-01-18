from flask import Flask, render_template

from web import health_blueprint

app = Flask(__name__)
app.register_blueprint(health_blueprint)

@app.route('/')
@app.route('/home/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)