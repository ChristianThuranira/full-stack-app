from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

# Initialize extensions
db = SQLAlchemy()
ma = Marshmallow()
cors = CORS()