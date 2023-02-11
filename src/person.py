import uuid


class Person:

    def __init__(self, name, task, status):
        self.id = uuid.uuid4().hex
        self.firstname = name
        self.lastname = task
        self.department = status

    def __str__(self):
        return f'id:{self.id} ' \
               f'firstname: {self.name}; ' \
               f'Lastname: {self.task}; ' \
               f'Department: {self.status}'

