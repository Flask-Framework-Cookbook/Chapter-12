from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from elasticsearch import Elasticsearch
from flask_caching import Cache
from flask_mail import Mail


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['WHOOSH_BASE'] = '/tmp/whoosh'
db = SQLAlchemy(app)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'gmail_username'
app.config['MAIL_PASSWORD'] = 'gmail_password'
app.config['MAIL_DEFAULT_SENDER'] = ('Sender name', 'sender email')
mail = Mail(app)

app.secret_key = 'some_random_key'

es = Elasticsearch('http://localhost:9200/')
es.indices.create('catalog', ignore=400)

from my_app.catalog.views import catalog
app.register_blueprint(catalog)

db.create_all()
