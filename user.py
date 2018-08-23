import hashlib


class Users:
    def __init__(self, username, password):
        self.username = username
        self.password = hashlib.sha256(password).hexdigest()

    def getUsername(self):
        return self.username


"""
    def getPassword(self):
        return self.password
"""

user = Users("Bilyan", "password")
print user.getUsername()
print user.getPassword()
