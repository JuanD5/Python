class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def login(self) -> str:
        return 'Logged in'
    
    def __repr__(self) -> str:
        return f'<User {self.username}'