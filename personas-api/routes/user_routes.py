from os import access
from flask_restful import reqparse
from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, create_access_token
from werkzeug.security import safe_str_cmp
from models.user import User


user_blueprint = Blueprint('user', __name__)


class UserParser:
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True)
    parser.add_argument('password', type=str, required=True)


@user_blueprint.route('/login', methods=['POST'])
def login():
    data = UserParser.parser.parse_args()
    user = User.get_user(data['username'])
    if user and safe_str_cmp(user.password, data['password']):
        access_token = create_access_token(identity=str(user.id))
        return jsonify(access_token=access_token, user=user.username, admin=user.is_admin)
    return jsonify(message='Não foi possível realizar o login'), 401


@user_blueprint.route('/create_user', methods=['POST'])
@jwt_required()
def create_user():
    data = UserParser.parser.parse_args()
    if User.get_user(data['username']):
        return jsonify(message='Usuário ja existente'), 400
    try:
        user = User.create_user(data['username'], data['password'])
        return jsonify(usernam=user.username, password=user.password, is_admin=user.is_admin), 201
    except Exception as e:
        return jsonify(message=e), 500