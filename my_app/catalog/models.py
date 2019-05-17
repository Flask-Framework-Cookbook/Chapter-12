import flask_whooshalchemy
from my_app import db, app

class Product(db.Model):
    __searchable__ = ['name', 'company']

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    price = db.Column(db.Float)
    company = db.Column(db.String(255))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship(
        'Category', backref=db.backref('products', lazy='dynamic')
    )

    def __init__(self, name, price, category, company=''):
        self.name = name
        self.price = price
        self.category = category
        self.company = company

    def __repr__(self):
        return '<Product %d>' % self.id


class Category(db.Model):
    __searchable__ = ['name']

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %d>' % self.id
