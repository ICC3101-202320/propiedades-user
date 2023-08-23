class User:
    def __init__(self, username, password):
        self._username = username
        self._password = password

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self):
        pass
    
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, value):
        if self._username == value['username'] and self._password == value['old_password']:
            self._password = value['new_password']


    def __repr__(self):
        return f'{self._username}: {self._password}'
