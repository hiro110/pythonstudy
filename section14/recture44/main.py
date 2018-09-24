# class

class Student:
    def __init__(self, name):
        self.name = name
        self.score = {}

    def add_score(self, subject_name, point):
        self.score[subject_name]=point

    def get_score(self, subject_name):
        return self.score.get(subject_name, 'その教科はまだ')


hiroaki = Student('hiroaki')
hiroaki.add_score('math', 50)
print(hiroaki.score)

ito = Student('ito')
ito.add_score('math', 100)
print(ito.score)