class Student:
    def __init__(self, first, last, fee):
        self.first = first
        self.last = last
        self.fee = fee

    def email(self):
        return '{}.{}@gmail.com'.format(self.first, self.last)

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def __repr__(self):
        return "Student('{}','{}',{})".format(self.first, self.last, self.fee)
