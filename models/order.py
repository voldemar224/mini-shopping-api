from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from database import db


class OrderProduct(db.Model):
    __tablename__ = 'ordered_products'

    id = db.Column(db.Integer, primary_key=True)

    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))

    quantity = db.Column(db.Integer, default=0)

    def increase_quantity_by_n(self, num=1):
        self.quantity += num
        self.save_to_db()

    def decrease_quantity_by_n(self, num=1):
        self.quantity -= num
        self.save_to_db()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        

class OrderModel(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    products = db.relationship('ProductModel', secondary='ordered_products', backref='product')

    @classmethod
    def find_by_id(cls, product_id):
        return cls.query.filter_by(id=product_id).first()

    @classmethod
    def find_all(cls, ):
        return cls.query.all()

    def add_product(self, product):
        self.products.append(product)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def to_json(self):
        products = [product.order_product_to_json(self) for product in self.products]

        return {
            'order_id': self.id,
            'user_id': self.user_id,
            'products': products
        }
