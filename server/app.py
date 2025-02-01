from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fitness.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_secret_key'  # Change this for security

db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)
CORS(app)  # Enable CORS for Postman and frontend requests

from routes import *

if __name__ == '__main__':
    app.run(debug=True, port=5555)
