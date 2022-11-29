from flask import Flask
from flask_restful import Resource, reqparse

from models.user import UserModel


class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, location='form')

    def get(self, user_id):
        user = UserModel.find_by_id(user_id)

        if user is None:
            return {'message': 'There is no user with such id'}, 404
        else:
            return user.to_json()

    def put(self, user_id):
        data = User.parser.parse_args()
        user = UserModel.find_by_id(user_id)

        user.name = data['name']

        user.save_to_db()

        return user.to_json()

    def delete(self, user_id):
        user = UserModel.find_by_id(user_id)
        user.delete_from_db()

        return {'message': 'User deleted'}, 200


class UserList(Resource):
    def get(self):
        return {'users': [user.to_json() for user in UserModel.find_all()]}


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, location='form')

    def post(self):
        data = UserRegister.parser.parse_args()
        user = UserModel(name=data['name'])
        user.save_to_db()

        return {'message': "User created."}, 201
