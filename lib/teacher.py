from user import User

import random

class Teacher(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = ["Teaching Methodology"]

    def teach(self):
        # Return the first item from knowledge for testing purposes
        return self.knowledge[0]
