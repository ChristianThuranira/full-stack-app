from extensions import db  # Import db from extensions

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class WorkoutPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    difficulty_level = db.Column(db.String(50), nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    duration_minutes = db.Column(db.Integer, nullable=False)
    calories_burned = db.Column(db.Integer, nullable=False)
    day_id = db.Column(db.Integer, db.ForeignKey('days.id'), nullable=False)

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class Days(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    completed_date = db.Column(db.Date, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.Text, nullable=True)
    workout_id = db.Column(db.Integer, db.ForeignKey('workout_plan.id'), nullable=False)
