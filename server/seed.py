from app import app  # Import the app from app.py
from extensions import db  # Import db from extensions
from models import User, WorkoutPlan, Exercise, Day, Log  # Make sure 'Day' is correctly imported
from werkzeug.security import generate_password_hash
from datetime import datetime

# Ensure we are inside the Flask application context
with app.app_context():
    # Reset the database (Drop all tables and recreate)
    db.drop_all()
    db.create_all()

    # Seed Users
    users = [
        User(username="JohnDoe", email="john@example.com",
             password=generate_password_hash("password123", method='pbkdf2:sha256')),

        User(username="JaneDoe", email="jane@example.com",
             password=generate_password_hash("securepass", method='pbkdf2:sha256'))
    ]

    # Seed Exercises
    exercises = [
        Exercise(name="Push-ups"),
        Exercise(name="Squats"),
        Exercise(name="Jump Rope"),
        Exercise(name="Bench Press"),
    ]

    # Seed Days
    days = [
        Day(name="Monday"),
        Day(name="Tuesday"),
        Day(name="Wednesday"),
        Day(name="Thursday"),
        Day(name="Friday"),
        Day(name="Saturday"),
        Day(name="Sunday"),
    ]

    # Seed Workout Plans
    workout_plans = [
        WorkoutPlan(title="Morning Cardio", description="30-minute run", difficulty_level="Medium",
                    time=datetime(2025, 2, 1, 6, 30), exercise_id=3, user_id=1, duration_minutes=30, 
                    calories_burned=250, day_id=1),

        WorkoutPlan(title="Leg Day", description="Squats and lunges", difficulty_level="Hard",
                    time=datetime(2025, 2, 2, 17, 0), exercise_id=2, user_id=2, duration_minutes=45,
                    calories_burned=350, day_id=2)
    ]

    # Seed Logs
    logs = [
        Log(completed_date=datetime(2025, 2, 1).date(), rating=5, notes="Felt great!", workout_id=1),
        Log(completed_date=datetime(2025, 2, 2).date(), rating=4, notes="Legs were burning!", workout_id=2)
    ]

    # Add everything to the database session
    db.session.add_all(users)
    db.session.add_all(exercises)
    db.session.add_all(days)
    db.session.add_all(workout_plans)
    db.session.add_all(logs)

    # Commit to save changes in the database
    db.session.commit()

    print("? Database seeded successfully!")