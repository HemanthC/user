from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy.sql import func
import json
import urllib.request
import os
import json

db = SQLAlchemy()
DB_NAME = "database.db"

app = Flask(__name__)

app.config['SECRET_KEY'] = 'qwwqretrqwwq'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db.init_app(app)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150),unique=True)
    name= db.Column(db.String(150))
    
with app.app_context():
        db.create_all()

@app.route('/user',methods=['GET', 'POST'])
def user():
    
    if request.method=='POST':

       cur_name = request.form.get('name')
       cur_email=request.form.get('email')

       new_user = User(name=cur_name, email=cur_email)
       db.session.add(new_user)
       db.session.commit()
       dict={}
       dict['user_name']=cur_name
       dict['email']=cur_email
       return dict
    else:
       return render_template('newuser.html')
     

@app.route('/',methods=['GET','POST'])
def verify_user():
    #print("hghg")
    username = request.args.get('user')
    print(username)
    user=User.query.filter_by(name=username).first()
    
    if user:
        return "T"
    else:
        return "F"
    return "hello"

if __name__ == '__main__':
    app.run(debug=True,port=5000)