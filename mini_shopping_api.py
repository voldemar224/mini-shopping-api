import os

from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

from resources.user import User, UserList, UserRegister
from resources.order import Order, OrderCreate, OrdersList
from resources.product import Product, ProductList, ProductCreate

from database import db


def create_app():
    app = Flask(__name__)

    # basedir = os.path.abspath(os.path.dirname(__file__))
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'mini_shopping_api_db.db')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mini_shopping_api_db.db'

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    @app.route('/')
    def hello():
        return "hello123"

    api = Api(app)

    api.add_resource(User, '/user/<int:user_id>')
    api.add_resource(UserList, '/users')
    api.add_resource(UserRegister, '/register')

    api.add_resource(Order, '/order/<int:order_id>')
    api.add_resource(OrderCreate, '/create-order')
    api.add_resource(OrdersList, '/orders')

    api.add_resource(Product, '/product/<int:product_id>')
    api.add_resource(ProductList, '/products')
    api.add_resource(ProductCreate, '/create-product')

    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='127.0.0.1', port=5000)
