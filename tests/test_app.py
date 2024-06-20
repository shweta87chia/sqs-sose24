import pytest
import sys
import os
from flask import Blueprint


# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))


from app import create_app, db
from app.models import User


@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"
    })

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()
    
@pytest.fixture
def client(app):
    return app.test_client()


def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert "Flask App" in response.text

def test_get_all_users(client, app):
    with app.app_context():
        # Add some dummy users to the database
        user1 = User(username='user1', email='user1@example.com')
        user2 = User(username='user2', email='user2@example.com')
        db.session.add_all([user1, user2])
        db.session.commit()

    response = client.get('/users')
    assert response.status_code == 200
    data = response.json
    assert len(data['users']) == 4  # Check if the correct number of users are returned

def test_get_user_by_id(client, app):
    with app.app_context():
        # Add a dummy user to the database
        user = User(username='test_user', email='test_user@example.com')
        db.session.add(user)
        db.session.commit()

        # No need to explicitly refresh the user here
        user_id = user.id

    response = client.get(f'/users/{user_id}')
    assert response.status_code == 200
    data = response.json
    assert data['username'] == 'test_user'
    assert data['email'] == 'test_user@example.com'

def test_add_user(client, app):
    with app.app_context():
        # Ensure the database is empty before adding the user
        db.session.query(User).delete()
        db.session.commit()

        user_data = {'username': 'new_user', 'email': 'new_user@example.com'}
        response = client.post('/users', json=user_data)
        assert response.status_code == 201  # Assuming 201 is the expected status code for successful creation

        # Clean up
        db.session.query(User).delete()
        db.session.commit()

def test_apitester(client, monkeypatch):
    # Mock the get_data_from_api function
    def mock_get_data_from_api(api_url):
        return {'key': 'value'}

    monkeypatch.setattr('app.routes.get_data_from_api', mock_get_data_from_api)

    response = client.get('/get')
    assert response.status_code == 200
    data = response.json
    assert data == {'key': 'value'}
