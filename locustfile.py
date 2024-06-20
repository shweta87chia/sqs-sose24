from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    host = "http://localhost:5000"
    wait_time = between(1, 5)

    @task
    def load_home(self):
        self.client.get('/')

    @task
    def get_all_users(self):
        self.client.get('/users')

    @task
    def get_user(self):
        # Fetch all users first to ensure there's at least one user to get
        response = self.client.get('/users')
        if response.status_code == 200 and response.json()['users']:
            user_id = response.json()['users'][0]['id']
            self.client.get(f'/users/{user_id}')
        else:
            print('No users found to fetch.')

    @task
    def add_user(self):
        user_data = {
            "username": "testuser",
            "email": "testuser@example.com"
        }
        self.client.post('/users', json=user_data)

    @task
    def apitester(self):
        self.client.get('/get')
