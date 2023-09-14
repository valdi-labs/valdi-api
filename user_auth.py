from api_utils import account_login


class UserAuth:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.access_token = None
        self.refresh_token = None

    def login(self):
        login_info = account_login(self.email, self.password)
        if login_info:
            self.refresh_token = login_info['refresh_token']
            self.access_token = login_info['access_token']
        else:
            raise ValueError('Unexpected response from login API')
