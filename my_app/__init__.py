from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from elasticsearch import Elasticsearch
from flask_caching import Cache

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['WHOOSH_BASE'] = '/tmp/whoosh'
db = SQLAlchemy(app)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

app.secret_key = 'some_random_key'

es = Elasticsearch('http://localhost:9200/')
es.indices.create('catalog', ignore=400)

from my_app.catalog.views import catalog
app.register_blueprint(catalog)

db.create_all()
