class User :
    def __init__(self,username,password) -> None:
        self.username = username
        self.password = password

users = [
    {
        'username':'rolf', 'password':'123'
    },
    {
        'username':'yo', 'password': '456'
    }
]        

user_objects = [User(**data) for data in users] # así se hace cuando hacemos el unpacking de diccionarios 

print(user_objects)

users = [
    ('rolf','123'),
    ('yo','456')
]

user_objects_2 = [User(*data) for data in users]
print(user_objects_2[0].username)