#!/usr/bin/env python

from user import User

import random

class Teacher(User):
    def __init__(self, first_name, last_name):
        super(Teacher, self).__init__(first_name, last_name)
        self.knowledge = ["Subject1", "Subject2"]

    def teach(self):
        return random.choice(self.knowledge)
