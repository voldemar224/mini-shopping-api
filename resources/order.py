from flask import Flask
from flask_restful import Resource, reqparse

from models.order import OrderModel, OrderProduct
from models.product import ProductModel


class Order(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('product_id', type=str, location='form')
    parser.add_argument('quantity', type=int, location='form', default=1)

    def get(self, order_id):
        order = OrderModel.find_by_id(order_id)

        return order.to_json()

    def put(self, order_id):
        data = Order.parser.parse_args()
        order = OrderModel.find_by_id(order_id)
        product = ProductModel.find_by_id(data['product_id'])
        order.add_product(product)

        order_product = OrderProduct.query.filter_by(order_id=order_id).filter_by(product_id=product.id).first()
        order_product.increase_quantity_by_n(data['quantity'])

        order.save_to_db()

        return order.to_json()

    def delete(self, order_id):
        data = Order.parser.parse_args()
        order = OrderModel.find_by_id(order_id)

        print(f"{data['product_id']} is None and {data['quantity']} is None")

        if data['product_id'] is None and data['quantity'] == 1:
            order.delete_from_db()

            return {'message': 'Order deleted'}, 200
        else:
            product = ProductModel.find_by_id(data['product_id'])

            order_product = OrderProduct.query.filter_by(order_id=order_id).filter_by(product_id=product.id).first()
            order_product.decrease_quantity_by_n(data['quantity'])

            if order_product.quantity == 0:
                order_product.delete_from_db()

            order.save_to_db()

            return order.to_json()


class OrderCreate(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('user_id', type=int, location='form')

    def post(self):
        data = OrderCreate.parser.parse_args()
        order = OrderModel(user_id=data['user_id'])

        order.save_to_db()

        return {'message': 'Order created'}, 201


class OrdersList(Resource):
    def get(self):
        return {'orders': [order.to_json() for order in OrderModel.find_all()]}
