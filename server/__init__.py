from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/Grzegorz/Documents/Porg/hakaton/server/db.db'
app.config['SECRET_KEY'] = '6be575743c714c0250e548de'

db = SQLAlchemy(app)

with app.app_context():
    db.create_all()


from server import routes 