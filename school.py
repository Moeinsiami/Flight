class School():
    def __init__(self, chairs):
        self.chairs = chairs
        self.student = []

    def add_student(self, name):
        if not self.open_chairs():
            return False
        self.student.append(name)
        return True

    def open_chairs(self):
        return self.chairs - len(self.student)
        

clas = School(3)
people = ['amir', 'zahra', 'ahmad', 'hamid', 'ali']

for anyone in people:
    if clas.add_student(anyone):
        print(anyone, 'has been added to the school')
    else:
        print(anyone, 'has not been added to the school')