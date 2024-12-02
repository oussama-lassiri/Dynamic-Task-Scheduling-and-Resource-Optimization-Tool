from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.models import db, User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods= ['POST'])
def register():
    data = request.get_json()
    
    # Check if username already exists
    if User.query.filter_by(username= data['username']).first():
        return jsonify({"error": "Username already exists"}), 400
    
    # Check if the email already exists
    if User.query.filter_by(email= data['email']).first():
        return jsonify({"error": "Email already exists"}), 400

    # Create new user
    new_user = User(
        username= data['username'], 
        email= data['email'],
        firstName= data['firstName'],
        lastName= data['lastName']
    )   
    new_user.set_password(data['password'])
    
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User created successfully"}), 201

@auth_bp.route('/login', methods= ['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username= data['username']).first()
    
    if user and user.check_password(data['password']):
        access_token = create_access_token(identity= user.id)
        return jsonify({
            "access_token": access_token,
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "firstName": user.firstName,
                "lastName": user.lastName,
            }
        }), 200
    
    return jsonify({"error": "Invalid credentials"}), 401

@auth_bp.route('/profile', methods= ['GET'])
@jwt_required()
def get_profile():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    
    return jsonify({
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "firstName": user.firstName,
        "lastName": user.lastName,
    }), 200