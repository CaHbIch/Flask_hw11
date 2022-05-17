class Candidates:

    def __init__(self, pk, name, picture, position, gender, age, skills):
        self.pk = pk
        self.name = name
        self.picture = picture
        self.position = position
        self.gender = gender
        self.age = age
        self.skills = skills

    def __repr__(self):
        return f"{self.pk},{self.name}, {self.picture}, {self.position}, {self.gender}, {self.age}, {self.skills}"
