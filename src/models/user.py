from copy import deepcopy

class User:

    def __init__(self):
        self.name = ""
        self.username = ""
        self.address = ""
        self.email = ""
        self.role = ""


class UserBuilder:

    def __init__(self):
        self.user = User()

    def get(self):
        return deepcopy(self.user)

    def name(self, *args):
        self.user.name = ' '.join(args)
        return self

    def username(self, username):
        self.user.username = username 
        return self

    def email(self, email):
        self.user.email = email
        return self

    def role(self, role):
        self.user.role = role 
        return self