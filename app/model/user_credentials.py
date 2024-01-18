# user_credentials.py in the model directory

class UserCredentials:
    # TODO Complete functions
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def set_password(self, new_password):
        # Logic to hash and set the new password
        pass

    def check_password(self, password):
        # Logic to check the password against the hashed version
        pass
