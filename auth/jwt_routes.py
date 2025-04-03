from flask import Blueprint, request, jsonify, render_template
from flask_jwt_extended import create_access_token, jwt_required
from werkzeug.security import check_password_hash, generate_password_hash

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET'])
def show_login():
    return render_template('auth/login.html')

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    access_token = create_access_token(identity=str(1))
    return jsonify({'access_token': access_token}), 200

@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return render_template('auth/protected.html')