from flask import Flask
from extensions import db, ma, jwt, cors  # Import extensions here
from routes import *  # Import routes

# Initialize Flask app
app = Flask(__name__)

# Database URI and configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fitness.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_secret_key'  # Change for security

# Initialize extensions with the app
db.init_app(app)
ma.init_app(app)
jwt.init_app(app)
cors.init_app(app)

if __name__ == '__main__':
    app.run(debug=True, port=5555)
