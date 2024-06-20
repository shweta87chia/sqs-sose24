Flask Application Documentation
Project Structure
 

flask_app/

├── app/

│   ├── __init__.py

│   ├── models.py

│   ├── routes.py

│   ├── api.py

│   ├── templates/

│   │   ├── base.html

│   │   ├── home.html

│   ├── static/

│       ├── css/

│       │   ├── style.css

│       └── js/

│           ├── script.js

├── tests/

│   ├── __init__.py

│   ├── test_app.py

│   ├── test_api.py

│   ├── test_e2e.py

├── migrations/

├── stucer/

├── locustfile.py

├── config.py

├── requirements.txt

├── README.md

├── run.py

Description
This project is a Flask web application with user management functionality, including API interaction, database operations, and testing. It is designed with modularity and scalability in mind.

Application Components
__init__.py
•     Initializes the Flask application.

•     Sets up the database using SQLAlchemy.

•     Registers the application routes.

•     Uses Flask-CORS for handling cross-origin requests.

•     Populates the database with initial user data.

models.py
•     Defines the User model with fields for id, username, and email.

•     Provides a to_dict method for converting model instances to dictionaries.

routes.py
•     Contains the route definitions for the application.

•     Includes routes for:

•     Rendering the home page.

•     Retrieving all users.

•     Retrieving a user by ID.

•     Adding a new user.

•     Testing API data retrieval.

api.py
•     Contains the function get_data_from_api for making HTTP GET requests to external APIs.

•     Handles exceptions and returns appropriate error messages.

extensions.py
•     Initializes and configures the SQLAlchemy extension for database operations.

Testing Components
tests/test_app.py
•     Uses pytest fixtures to set up the application and client for testing.

•     Contains tests for:

•     Home page rendering.

•     Retrieving all users.

•     Retrieving a user by ID.

•     Adding a new user.

•     API data retrieval with a mocked function.

tests/test_api.py
•     Mocks the requests.get method to test the get_data_from_api function.

•     Ensures the function returns the expected data.

tests/test_e2e.py
•     Uses Selenium for end-to-end testing of the home page.

•     Checks the page title and specific elements on the page.

Configuration
config.py
•     Contains the application configuration class.

•     Sets up the secret key and database URI.

Load Testing
locustfile.py
•     Defines a Locust test for load testing the home page.

•     Simulates user behavior by sending GET requests to the home page.

Running the Application
1.   Install Dependencies: Ensure all required dependencies are installed.

pip install -r requirements.txt

2.   Set Up the Database: Initialize the database and populate it with initial data.

 

flask db init

flask db migrate

flask db upgrade

3.   Run the Application: Start the Flask development server.
**********************************************************************************************************************************************************************************************************************************************************

 

flask run

Running Tests
1.   Unit and Integration Tests: Use pytest to run the tests.

 

pytest

2.   End-to-End Tests: Use Selenium to run the end-to-end tests.

 

pytest tests/test_e2e.py

3.   Load Testing: Use Locust for load testing.

 

locust

Dependencies
•     Flask

•     Flask-SQLAlchemy

•     Flask-CORS

•     pytest

•     Selenium

•     Locust

Environment Variables
•     SECRET_KEY: Secret key for Flask application.

•     DATABASE_URL: Database URL for SQLAlchemy.

Example Requests
Get All Users
 

GET /users

Response:

{

  "users": [

    {"id": 1, "username": "user1", "email": "user1@example.com"},

    {"id": 2, "username": "user2", "email": "user2@example.com"}

  ]

}

Get User by ID
 

GET /users/1

Response:

{

  "username": "user1",

  "email": "user1@example.com"

}

Add New User
 

POST /users

Request:

{

  "username": "new_user",

  "email": "new_user@example.com"

}

Response:

{

  "message": "User added successfully"

}

Troubleshooting
•     Database Issues: Ensure the database URI is correctly set in the environment variables.

•     Server Errors: Check the application logs for detailed error messages.

•     Testing Failures: Verify that the test fixtures are correctly setting up and tearing down the test environment.

This documentation provides an overview of the application structure, key components, setup instructions, testing procedures, and example requests to help you get started with and understand the project.








# Flask Web Application

This is a robust web application built with Flask, featuring comprehensive testing and secure, performant interactions with third-party APIs.

## Features

- User Management
- Database Integration with SQLAlchemy
- Third-Party API Interaction
- Comprehensive Testing (Unit, Integration, E2E, Security, Performance)

## Setup

1. **Clone the repository:**

    ```bash 
    https://inf-git.fh-rosenheim.de/studsaxesh6537/python-flask-sqs.git
   
    
    ```

2. **Set up a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```



4. **Run the application:**

    ```bash
    flask run
    ```

## Running Tests

- **Unit Tests:**

    ```bash
    pytest tests/
    ```

- **Performance Tests:**

    ```bash
    locust -f locustfile.py
    ```

## Additional Information

For more details on how to use this application and contribute, please refer to the [documentation](docs/).
