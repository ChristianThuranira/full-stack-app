from flask import Flask
from extensions import db, ma, cors
from routes import bp
import os

# Initialize Flask app
app = Flask(__name__)

# Configurations
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///fitness.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "your_secret_key")

# Initialize extensions
db.init_app(app)
ma.init_app(app)
cors.init_app(app)

# Register Blueprint
app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(debug=True, port=5555)
