from extensions import db

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

# Exercise model
class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# Day model (make sure this exists)
class Day(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

# WorkoutPlan model
class WorkoutPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    difficulty_level = db.Column(db.String(50), nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    day_id = db.Column(db.Integer, db.ForeignKey('day.id'), nullable=False)
    duration_minutes = db.Column(db.Integer, nullable=False)
    calories_burned = db.Column(db.Integer, nullable=False)

# Log model
class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    completed_date = db.Column(db.Date, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.Text, nullable=True)
    workout_id = db.Column(db.Integer, db.ForeignKey('workout_plan.id'), nullable=False)