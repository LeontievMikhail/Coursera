class User:
    def __init__(self,name,email):
        self.name = name
        self.email=email

    def __str__(self):
        return '{}<{}>'.format(self.name, self.email)

jane= User('Jane Doe', 'janedoe@example.com')

print(jane)

