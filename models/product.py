from flask import Flask
from flask_sqlalchemy import SQLAlchemy


from models.order import OrderProduct


from database import db


class ProductModel(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    @classmethod
    def find_by_id(cls, product_id):
        return cls.query.filter_by(id=product_id).first()

    @classmethod
    def find_all(cls, ):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def to_json(self):
        return {
            'id': self.id,
            'product_name': self.name,
            'product_price': self.price,
        }

    def order_product_to_json(self, order):
        quantity = OrderProduct.query.filter_by(order_id=order.id).filter_by(product_id=self.id).first().quantity
        return {
            'product_id': self.id,
            'product_name': self.name,
            'product_price': self.price,
            'quantity': quantity,
        }
