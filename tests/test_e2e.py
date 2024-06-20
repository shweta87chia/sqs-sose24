from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from faker import Faker
import time
import pytest
from app import create_app, db
from app.models import User

# Initialize faker
fake = Faker()



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

def test_home_page(client):
    driver = webdriver.Chrome()
    driver.get('http://127.0.0.1:5000')
    time.sleep(4)

    assert "Flask App" in driver.title

    heading = driver.find_element(By.TAG_NAME, 'h1').text
    assert "Welcome to Flask App" in heading

    driver.quit()

def test_add_user(client):
    driver = webdriver.Chrome()
    driver.get('http://127.0.0.1:5000/add_user')

    assert "Add User" in driver.title

    username = fake.user_name()
    email = fake.email()

    username_input = driver.find_element(By.ID, 'username')
    time.sleep(1)
    username_input.send_keys(username)
    time.sleep(1)
    email_input = driver.find_element(By.ID, 'email')
    email_input.send_keys(email)
    time.sleep(3)

    submit_button = driver.find_element(By.ID, 'submit')
    submit_button.click()


    message = driver.find_element(By.ID, 'message').text
    time.sleep(5)
    print("Message:", message)  # Debugging line
    print(driver.page_source)  # Print the page source for debugging
    assert "User added successfully" in message


    driver.get('http://127.0.0.1:5000/list_users')
    time.sleep(5)
    driver.quit()

