from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from server.config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import models
from server.models import restaurant, pizza, restaurant_pizza

# Import and register blueprints after app and db are initialized
from server.controllers import register_blueprints
register_blueprints(app)

if __name__ == '__main__':
    app.run(debug=True)