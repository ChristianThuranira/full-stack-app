from flask import Flask, jsonify
from extensions import db, ma, jwt, cors  
from routes import routes  # Import the blueprint

# Initialize Flask app
app = Flask(__name__)

# Database configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fitness.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_secret_key'  # Change for security

# Initialize extensions with the app
db.init_app(app)
ma.init_app(app)
jwt.init_app(app)
cors.init_app(app)

# Register the blueprint with a prefix
app.register_blueprint(routes, url_prefix='/api')

# Default route to check if the app is running
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Fitness API!"}), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ensure tables are created before running
    app.run(debug=True, port=5555)
