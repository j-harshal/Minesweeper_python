class User:
    def __init__(this, username, password):
        this.username1 = username
        this.password1 = password

    def login(this, username, password):
        if this.username1 == username and this.password1 == password:
            print("Logged in successfully")
        else:
            print("Invalid credentials")


print("Create user")
username = input("Enter the username: ")
password = input("Enter the Password: ")
print("Account created successfully. Login now")

user = User(username, password)

user_input_username = input("Username: ")
user_input_password = input("Password: ")

user.login(user_input_username, user_input_password)
