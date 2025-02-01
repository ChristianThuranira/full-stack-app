from flask import Flask
from extensions import db, ma  # Import extensions here
from routes import *  # Routes will be imported here

# Initialize Flask app
app = Flask(__name__)

# Database URI and configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fitness.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions with the app
db.init_app(app)
ma.init_app(app)

if __name__ == '__main__':
    app.run(debug=True, port=5555)
