from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from database import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    orders = db.relationship('OrderModel', backref='order')

    @classmethod
    def find_by_id(cls, user_id):
        return cls.query.filter_by(id=user_id).first()

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
        orders = [order.to_json() for order in self.orders]

        return {
            'id': self.id,
            'name': self.name,
            'orders': orders
        }
