from flask import Flask
from extensions import db, ma, cors  # Import the necessary extensions

# Initialize Flask app
app = Flask(__name__)

# Database URI and configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fitness.db'  # Update to your preferred database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions with the app
db.init_app(app)
ma.init_app(app)
cors.init_app(app)

# Only import routes after initializing the app to avoid circular import
from routes import bp  # Import the blueprint here

# Register the blueprint with the Flask app
app.register_blueprint(bp)

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=5555)
