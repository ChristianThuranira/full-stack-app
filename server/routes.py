from flask import Blueprint, request, jsonify
from extensions import db
from models import User, WorkoutPlan
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required

# Create a Blueprint instead of directly attaching routes to app
routes = Blueprint('routes', __name__)

# ?? Register User
@routes.route('/register', methods=['POST'])
def register():
    data = request.json
    hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')
    new_user = User(username=data['username'], email=data['email'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201

# ?? Login User
@routes.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()
    if user and check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity=user.id)
        return jsonify({"token": access_token}), 200
    return jsonify({"message": "Invalid credentials"}), 401
