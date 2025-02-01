from flask import Blueprint, request, jsonify
from extensions import db
from models import User, WorkoutPlan, Exercise, Log
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

api_bp = Blueprint('api', __name__)

### AUTH ROUTES ###
@api_bp.route('/auth/register', methods=['POST'])
def register():
    data = request.json
    hashed_password = generate_password_hash(data['password'])
    user = User(username=data['username'], email=data['email'], password=hashed_password)
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User registered"}), 201

@api_bp.route('/auth/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()
    if user and check_password_hash(user.password, data['password']):
        token = create_access_token(identity=user.id)
        return jsonify({"token": token}), 200
    return jsonify({"message": "Invalid credentials"}), 401

### WORKOUT ROUTES ###
@api_bp.route('/workouts', methods=['GET', 'POST'])
@jwt_required()
def handle_workouts():
    if request.method == 'GET':
        workouts = WorkoutPlan.query.all()
        return jsonify([{"title": w.title, "description": w.description} for w in workouts]), 200

    if request.method == 'POST':
        data = request.json
        new_workout = WorkoutPlan(
            title=data['title'],
            description=data['description'],
            difficulty_level=data['difficulty_level'],
            time=data['time'],
            exercise_id=data['exercise_id'],
            user_id=get_jwt_identity(),
            duration_minutes=data['duration_minutes'],
            calories_burned=data['calories_burned'],
            day_id=data['day_id']
        )
        db.session.add(new_workout)
        db.session.commit()
        return jsonify({"message": "Workout created"}), 201

@api_bp.route('/workouts/<int:id>', methods=['PATCH', 'DELETE'])
@jwt_required()
def update_delete_workout(id):
    workout = WorkoutPlan.query.get_or_404(id)
    if request.method == 'PATCH':
        data = request.json
        for key, value in data.items():
            setattr(workout, key, value)
        db.session.commit()
        return jsonify({"message": "Workout updated"}), 200
    
    if request.method == 'DELETE':
        db.session.delete(workout)
        db.session.commit()
        return jsonify({"message": "Workout deleted"}), 200

### EXERCISE ROUTES ###
@api_bp.route('/exercises', methods=['GET', 'POST'])
def handle_exercises():
    if request.method == 'GET':
        exercises = Exercise.query.all()
        return jsonify([{"id": e.id, "name": e.name} for e in exercises]), 200
    
    if request.method == 'POST':
        data = request.json
        new_exercise = Exercise(name=data['name'])
        db.session.add(new_exercise)
        db.session.commit()
        return jsonify({"message": "Exercise added"}), 201

### LOG ROUTES ###
@api_bp.route('/logs', methods=['GET', 'POST'])
def handle_logs():
    if request.method == 'GET':
        logs = Log.query.all()
        return jsonify([{"id": l.id, "rating": l.rating, "notes": l.notes} for l in logs]), 200
    
    if request.method == 'POST':
        data = request.json
        new_log = Log(
            completed_date=data['completed_date'],
            rating=data['rating'],
            notes=data['notes'],
            workout_id=data['workout_id']
        )
        db.session.add(new_log)
        db.session.commit()
        return jsonify({"message": "Log added"}), 201
