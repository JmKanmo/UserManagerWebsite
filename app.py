import os
from flask import Flask
from flask import render_template
from models import db
from api_version1 import api as API_VERSION1

app = Flask(__name__)
app.register_blueprint(API_VERSION1, url_prefix='/api/v1')

@app.route('/register')
def register():
    return render_template('register.htm')

@app.route('/')
def hello():
    return 'Hello World'
    
basedir = os.path.abspath(os.path.dirname(__file__)) # 현재 파일의 주소 반환
dbfile = os.path.join(basedir,'db.sqlite') # 현재 파일의 주소 + 'dp.sqlite'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile # SQLALCHEMY URI옵션추가
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True # SQLALCHEMY Commit 옵션 True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # 버전에따른 호환성문제로 False
app.config['SECRET_KEY'] = 'AK47TRG21M4A6GATLEINGGUNSHOT' #CSRF 해쉬값적용

db.init_app(app)
db.app = app
db.create_all()

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
