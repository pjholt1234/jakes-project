class User():
    def __init__(self, id = None, username = None, password = None):
        self.id       = id
        self.username = username
        self.password = password

    def isLoggedIn(self):
        if(self.id is not None):
            print('Logged In')
            return True
        else:
            print('Not logged in.')
            return False
    
    
    def hydrate(self, id, username, password):
        print('Hydrate user model', id, username, password)
        self.id       = id
        self.username = username
        self.password = password

        self.isLoggedIn

