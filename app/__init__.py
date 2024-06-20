from flask import Flask
from flask_cors import CORS
from .extensions import db
from sqlalchemy.exc import IntegrityError
from .routes import app_routes

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
    
    db.init_app(app)
    app.register_blueprint(app_routes)
    
    # Initialize CORS
    CORS(app, resources={r"/*": {"origins": "*"}})

    from .models import User

    # Create the database tables
    with app.app_context():
        db.create_all()

        # Add some initial data
        try:
            with db.session.begin_nested():
                user1 = User(username='John Doe', email="john@gmail.com")
                user2 = User(username='Jane Smith', email="jane@gmail.com")
                db.session.add(user1)
                db.session.add(user2)
        except IntegrityError:
            db.session.rollback()
        else:
            db.session.commit()

    return app

app = create_app()
