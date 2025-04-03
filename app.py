from flask import Flask, render_template
from web import health_blueprint
from auth.jwt_routes import auth_bp
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['JWT_TOKEN_LOCATION'] = ['headers']# これを後から足した
app.config['JWT_SECRET_KEY'] = 'your-secret-key'  # 本番環境では環境変数から読み込むことを推奨
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

jwt = JWTManager(app)

app.register_blueprint(health_blueprint)# 「health」を追加
app.register_blueprint(auth_bp)

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