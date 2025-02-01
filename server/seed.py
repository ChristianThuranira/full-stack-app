from app import db
from models import User, WorkoutPlan, Exercise, Days, Log
from werkzeug.security import generate_password_hash
from datetime import datetime

# Reset the database (Drop all tables and recreate)
db.drop_all()
db.create_all()

# ? Seed Users
users = [
    User(username="JohnDoe", email="john@example.com", password=generate_password_hash("password123", method='bcrypt')),
    User(username="JaneDoe", email="jane@example.com", password=generate_password_hash("securepass", method='bcrypt'))
]

# ? Seed Exercises
exercises = [
    Exercise(name="Push-ups"),
    Exercise(name="Squats"),
    Exercise(name="Jump Rope"),
    Exercise(name="Bench Press"),
]

# ? Seed Days
days = [
    Days(name="Monday"),
    Days(name="Tuesday"),
    Days(name="Wednesday"),
    Days(name="Thursday"),
    Days(name="Friday"),
    Days(name="Saturday"),
    Days(name="Sunday"),
]

# ? Seed Workout Plans
workout_plans = [
    WorkoutPlan(title="Morning Cardio", description="30-minute run", difficulty_level="Medium",
                time=datetime(2025, 2, 1, 6, 30), exercise_id=3, user_id=1, duration_minutes=30, 
                calories_burned=250, day_id=1),

    WorkoutPlan(title="Leg Day", description="Squats and lunges", difficulty_level="Hard",
                time=datetime(2025, 2, 2, 17, 0), exercise_id=2, user_id=2, duration_minutes=45,
                calories_burned=350, day_id=2)
]

# ? Seed Logs
logs = [
    Log(completed_date=datetime(2025, 2, 1).date(), rating=5, notes="Felt great!", workout_id=1),
    Log(completed_date=datetime(2025, 2, 2).date(), rating=4, notes="Legs were burning!", workout_id=2)
]

# ? Add everything to the session
db.session.add_all(users)
db.session.add_all(exercises)
db.session.add_all(days)
db.session.add_all(workout_plans)
db.session.add_all(logs)

# ? Commit to save changes
db.session.commit()

print("? Database seeded successfully!")
