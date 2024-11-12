from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from controller.user_controller import UserController

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"msg": "Faltan datos"}), 400
    
    response, status = UserController.register_user(username, password)
    return jsonify(response), status


@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"msg": "Faltan datos"}), 400

    user = UserController.authenticate_user(username, password)
    if not user:
        return jsonify({"msg": "Credenciales incorrectas"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200


@user_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
