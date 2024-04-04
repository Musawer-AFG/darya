import json


class EmailManager:
    def __init__(self, email, password, receiver_email):
        self.email = email
        self.password = password
        self.receiver_email = receiver_email

    def set_email(self, email):
        self.email = email

    def set_password(self, password):
        self.password = password

    def set_receiver_email(self, receiver_email):
        self.receiver_email = receiver_email

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def get_receiver_email(self):
        return self.receiver_email

    def save_to_json(self, file_path):
        data = {
            "email": self.email,
            "password": self.password,
            "receiver_email": self.receiver_email
        }
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)

    def load_from_json(self, file_path):
        try:
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
                self.email = data.get("email", "")
                self.password = data.get("password", "")
                self.receiver_email = data.get("receiver_email", "")
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file: {file_path}")