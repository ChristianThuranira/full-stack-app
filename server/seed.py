from extensions import db
from models import User, WorkoutPlan, Exercise, Days, Log
from werkzeug.security import generate_password_hash
from datetime import datetime
from app import app  # Import AFTER defining app to avoid circular import

# Run inside Flask app context
with app.app_context():
    db.drop_all()
    db.create_all()

    users = [
        User(username="JohnDoe", email="john@example.com",
             password=generate_password_hash("password123", method='pbkdf2:sha256')),
        User(username="JaneDoe", email="jane@example.com",
             password=generate_password_hash("securepass", method='pbkdf2:sha256'))
    ]

    exercises = [Exercise(name="Push-ups"), Exercise(name="Squats"), Exercise(name="Jump Rope")]
    days = [Days(name="Monday"), Days(name="Tuesday"), Days(name="Wednesday")]

    workout_plans = [
        WorkoutPlan(title="Morning Cardio", description="30-minute run", difficulty_level="Medium",
                    time=datetime(2025, 2, 1, 6, 30), exercise_id=3, user_id=1, duration_minutes=30, 
                    calories_burned=250, day_id=1)
    ]

    logs = [
        Log(completed_date=datetime(2025, 2, 1).date(), rating=5, notes="Felt great!", workout_id=1)
    ]

    db.session.add_all(users)
    db.session.add_all(exercises)
    db.session.add_all(days)
    db.session.add_all(workout_plans)
    db.session.add_all(logs)
    db.session.commit()

    print("? Database seeded successfully!")
