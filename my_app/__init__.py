from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from pyelasticsearch import ElasticSearch
from pyelasticsearch.exceptions import IndexAlreadyExistsError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['WHOOSH_BASE'] = '/tmp/whoosh'
db = SQLAlchemy(app)

app.secret_key = 'some_random_key'

es = ElasticSearch('http://localhost:9200/')
try:
    es.create_index('catalog')
except IndexAlreadyExistsError, e:
    pass

from my_app.catalog.views import catalog
app.register_blueprint(catalog)

db.create_all()
