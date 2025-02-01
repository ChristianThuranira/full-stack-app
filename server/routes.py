from flask import request, jsonify
from app import app, db
from models import User, WorkoutPlan, Exercise, Days, Log
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required

# ?? Register User
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    hashed_password = generate_password_hash(data['password'], method='bcrypt')
    new_user = User(username=data['username'], email=data['email'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201

# ?? Login User
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()
    if user and check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity=user.id)
        return jsonify({"token": access_token}), 200
    return jsonify({"message": "Invalid credentials"}), 401

# ?? Get All Workout Plans
@app.route('/workout_plans', methods=['GET'])
@jwt_required()
def get_workout_plans():
    plans = WorkoutPlan.query.all()
    return jsonify([{"id": p.id, "title": p.title, "description": p.description} for p in plans]), 200

# ? Create Workout Plan
@app.route('/workout_plans', methods=['POST'])
@jwt_required()
def create_workout_plan():
    data = request.json
    new_plan = WorkoutPlan(**data)
    db.session.add(new_plan)
    db.session.commit()
    return jsonify({"message": "Workout plan created"}), 201

# ?? Update Workout Plan
@app.route('/workout_plans/<int:id>', methods=['PATCH'])
@jwt_required()
def update_workout_plan(id):
    plan = WorkoutPlan.query.get(id)
    if not plan:
        return jsonify({"message": "Workout not found"}), 404
    data = request.json
    for key, value in data.items():
        setattr(plan, key, value)
    db.session.commit()
    return jsonify({"message": "Workout updated"}), 200

# ? Delete Workout Plan
@app.route('/workout_plans/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_workout_plan(id):
    plan = WorkoutPlan.query.get(id)
    if not plan:
        return jsonify({"message": "Workout not found"}), 404
    db.session.delete(plan)
    db.session.commit()
    return jsonify({"message": "Workout deleted"}), 200
