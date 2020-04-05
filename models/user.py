from random import random, choice
import string


class User:

    def __init__(self, user_id, fname, lname, email):
        self.id = user_id
        self.first_name = fname
        self.last_name = lname
        self.email = email
        self.generate_password()

    def generate_password(self, length=5):
        """Generate a random string of fixed length """
        letters = string.ascii_lowercase
        random_pass = ''.join(choice(letters) for i in range(length))

        self.password = '{}{}{}'.format(
            self.first_name[0:2], random_pass, self.last_name[-2:])

    def __str__(self):
        return '\n*-------*\nUser Details: \nID: {}\nFirst Name: {}\nLast Name: {}\nEmail: {}\nPassword: {}'.format(
            self.id, self.first_name, self.last_name, self.email, self.password)
