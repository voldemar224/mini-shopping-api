from flask import Flask
from flask_restful import Resource, reqparse

from models.product import ProductModel


class Product(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, location='form')
    parser.add_argument('price', type=str, location='form')

    def get(self, product_id):
        product = ProductModel.find_by_id(product_id)
        return product.to_json()

    def put(self, product_id):
        data = Product.parser.parse_args()
        product = ProductModel.find_by_id(product_id)

        if product is None:
            return {'message': "This product doesn't exist, to edit, you should choose existing product_id"}, 404
        else:
            product.name = data['name'] if data['name'] else product.name
            product.price = data['price'] if data['price'] else product.price

        product.save_to_db()

        return product.to_json()

    def delete(self, product_id):
        product = ProductModel.find_by_id(product_id)
        product.delete_from_db()

        return {'message': 'Product deleted'}, 200


class ProductList(Resource):
    def get(self):
        return {'products': [product.to_json() for product in ProductModel.find_all()]}


class ProductCreate(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, location='form')
    parser.add_argument('price', type=str, location='form')

    def post(self):
        data = ProductCreate.parser.parse_args()
        product = ProductModel(name=data['name'], price=data['price'])
        product.save_to_db()

        return {'message': "Product created."}, 201
