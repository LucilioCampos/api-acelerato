from requests.auth import HTTPBasicAuth


class Auth(object):

    def __init__(self, username, token):
        self.username = username
        self.token = token

    def get_token(self):
        return self.token

    def get_username(self):
        return self.username

    def credentials(self):
        return HTTPBasicAuth(self.get_username(), self.get_token())
