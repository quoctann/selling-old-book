from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin


app = Flask(__name__)


# Configuration of MySQL Server
app.secret_key = "y1478whdbh1183132qwchda"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:P@ssw0rd@localhost/oldbook?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


# # Configuration of global name
db = SQLAlchemy(app=app)
login = LoginManager(app=app)
admin = Admin(app=app, name='Products Editor',
              template_mode="bootstrap4")
