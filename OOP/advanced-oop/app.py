from admin import Admin
from database import Database

admin = Admin(username="Rolf", password="1234", access=3)

admin.save()

if __name__ == "__main__":
    print(Database.find(lambda x: x["username"] == "Rolf"))