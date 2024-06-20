from flask import Blueprint, jsonify, request, current_app, render_template
from app import db
from .models import User
from .api import get_data_from_api
import requests
from sqlalchemy.exc import IntegrityError

app_routes = Blueprint('app_routes', __name__)

@app_routes.route('/')
def home():
    return render_template('home.html')


@app_routes.route('/users', methods=['GET'])
def get_all_users():
    try:
        users = User.query.all()
        user_dicts = [user.to_dict() for user in users]
        return jsonify(users=user_dicts)
    except Exception as e:
        current_app.logger.error(f'Error fetching users: {str(e)}')
        return jsonify({'error': 'Failed to fetch users'}), 500


@app_routes.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user = db.session.get(User, user_id)  # Use the new Session.get() method
        if not user:
            return jsonify({'error': 'User not found'}), 404
        return jsonify({'username': user.username, 'email': user.email})
    except Exception as e:
        current_app.logger.error(f'Error fetching user with ID {user_id}: {str(e)}')
        return jsonify({'error': 'Failed to fetch user'}), 500


@app_routes.route('/users', methods=['POST'])
def add_user():
    try:
        data = request.get_json()
        if not data or 'username' not in data or 'email' not in data:
            return jsonify({'error': 'Invalid request data'}), 400

        username = data['username']
        email = data['email']

        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()
        return jsonify(message='User added successfully'), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Username or email already exists'}), 409
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(f'Error adding user: {str(e)}')
        return jsonify({'error': 'Failed to add user'}), 500


@app_routes.route('/get', methods=['GET'])
def apitester():
    api_url = 'https://jsonplaceholder.typicode.com/todos/1'  # Replace with your actual API URL
    try:
        data = get_data_from_api(api_url)
        return jsonify(data), 200
    except requests.exceptions.RequestException as e:
        current_app.logger.error(f'Error fetching data from API: {str(e)}')
        return jsonify({'error': 'Failed to fetch data from API'}), 500
    except Exception as e:
        current_app.logger.error(f'Unexpected error: {str(e)}')
        return jsonify({'error': 'An unexpected error occurred'}), 500


@app_routes.route('/add_user')
def add_user_page():
    return render_template('add_user.html')


@app_routes.route('/list_users')
def list_users_page():
    return render_template('list_users.html')