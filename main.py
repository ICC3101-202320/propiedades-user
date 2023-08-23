from user import User

usr = User('john_doe', 'password')
print(usr)
# usr._password = 'nueva_contraseña'
print(usr)
# print(usr.get_username())
# print(usr.get_password('john_doe'))
# print(usr.get_password('john_do'))
usr.password = {
        "username": 'john_doe',
        "old_password": 'nueva_contraseña',
        "new_password": 'new_pass'
    }
print(usr.password)
print(usr)
