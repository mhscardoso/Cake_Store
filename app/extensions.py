from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import app

db = SQLAlchemy()
migrate = Migrate()