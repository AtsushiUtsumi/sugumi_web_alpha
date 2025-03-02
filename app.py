from flask import Flask, render_template

from web import health_blueprint

app = Flask(__name__)
app.register_blueprint(health_blueprint)# 「health」を追加

@app.route('/')
@app.route('/home/<name>')
def hello(name=None):
    file = open('test.txt', 'a')
    file.write("HOGE")
    file.close()
    file = open('test.txt', 'r')
    lines = file.readlines()
    file.close()
    if len(lines) > 0:
        return render_template('jss.html', name=lines)
    return render_template('hello.html', name=name)