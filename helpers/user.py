class User():
    def __init__(self, id = None, username = None, password = None):
        self.id       = id
        self.username = username
        self.password = password
        self.loggedIn = False

    def hydrate(self, id, username, password):
        print('Hydrate user model', id, username, password)
        self.id       = id
        self.username = username
        self.password = password
        self.loggedIn = True

