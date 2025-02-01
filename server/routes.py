from flask import Blueprint, request, jsonify
from extensions import db
from models import User, WorkoutPlan, Exercise, Log
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required

# Create a blueprint for routes
api_bp = Blueprint('api', __name__)

# Register a new user
@api_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    hashed_password = generate_password_hash(data['password'], method='bcrypt')
    new_user = User(username=data['username'], email=data['email'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201

# Login user (returns JWT token)
@api_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()
    if user and check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity=user.id)
        return jsonify({"token": access_token}), 200
    return jsonify({"message": "Invalid credentials"}), 401

# Create a workout plan
@api_bp.route('/workout_plans', methods=['POST'])
@jwt_required()  # Ensure the user is logged in
def create_workout_plan():
    data = request.json
    new_workout_plan = WorkoutPlan(
        title=data['title'],
        description=data['description'],
        difficulty_level=data['difficulty_level'],
        time=data['time'],
        exercise_id=data['exercise_id'],
        user_id=data['user_id'],
        duration_minutes=data['duration_minutes'],
        calories_burned=data['calories_burned'],
        day_id=data['day_id']
    )
    db.session.add(new_workout_plan)
    db.session.commit()
    return jsonify({"message": "Workout plan created successfully"}), 201

# Get all workout plans
@api_bp.route('/workout_plans', methods=['GET'])
@jwt_required()
def get_workout_plans():
    workout_plans = WorkoutPlan.query.all()
    return jsonify([{
        'id': plan.id,
        'title': plan.title,
        'description': plan.description,
        'difficulty_level': plan.difficulty_level,
        'time': plan.time,
        'user_id': plan.user_id,
        'exercise_id': plan.exercise_id,
        'day_id': plan.day_id,
        'duration_minutes': plan.duration_minutes,
        'calories_burned': plan.calories_burned
    } for plan in workout_plans]), 200

# Update an existing workout plan
@api_bp.route('/workout_plans/<int:id>', methods=['PATCH'])
@jwt_required()
def update_workout_plan(id):
    workout_plan = WorkoutPlan.query.get(id)
    if workout_plan:
        data = request.json
        for key, value in data.items():
            setattr(workout_plan, key, value)
        db.session.commit()
        return jsonify({"message": "Workout plan updated successfully"}), 200
    return jsonify({"message": "Workout plan not found"}), 404

# Delete a workout plan
@api_bp.route('/workout_plans/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_workout_plan(id):
    workout_plan = WorkoutPlan.query.get(id)
    if workout_plan:
        db.session.delete(workout_plan)
        db.session.commit()
        return jsonify({"message": "Workout plan deleted successfully"}), 200
    return jsonify({"message": "Workout plan not found"}), 404

# Log workout completion
@api_bp.route('/log', methods=['POST'])
@jwt_required()
def log_workout():
    data = request.json
    workout_log = Log(
        completed_date=data['completed_date'],
        rating=data['rating'],
        notes=data['notes'],
        workout_id=data['workout_id']
    )
    db.session.add(workout_log)
    db.session.commit()
    return jsonify({"message": "Workout log added successfully"}), 201
