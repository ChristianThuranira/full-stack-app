from flask import Flask, jsonify
from extensions import db, ma, cors, jwt
from config import Config
from routes import api_bp

app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)
ma.init_app(app)
jwt.init_app(app)
cors.init_app(app)

# Register routes
app.register_blueprint(api_bp, url_prefix='/api')

@app.route('/')
def home():
    return jsonify({"message": "Fitness API Running"}), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5555)
