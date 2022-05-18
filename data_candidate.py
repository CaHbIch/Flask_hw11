import json

from candidate import Candidates
from config import path
from pprint import pprint as pp


class DataCandidates:

    def __init__(self, path):
        self.path = path

    def load_candidate(self):
        '''возвращает список всех кандидатов'''
        with open(self.path, "r", encoding="utf-8") as file:
            file = json.load(file)
            candidates = []
            for candidat in file:
                pk = candidat["id"]
                name = candidat["name"]
                picture = candidat["picture"]
                position = candidat["position"]
                gender = candidat["gender"]
                age = candidat["age"]
                skills = candidat["skills"].lower().strip().split(", ")

                candidats = Candidates(pk, name, position, picture, gender, age, skills)
                candidates.append(candidats)

            return tuple(candidates)

    def get_id(self, pk):
        """ возвращает одного кандидата по его pk"""
        gets_id = self.load_candidate()
        for candidate_id in gets_id:
            if candidate_id.pk == pk:
                return candidate_id

    def get_name(self):
        """возвращает имена кандидатов"""
        gets_name = self.load_candidate()
        names = []
        for candidate_name in gets_name:
            names.append(candidate_name.name)
        return names

    def get_skills(self, skills):
        """возвращает навыки кандидатов"""
        gets_skills = self.load_candidate()
        for candidate_skils in gets_skills:
            if candidate_skils.skills == skills:
                return candidate_skils


data = DataCandidates(path)
print(data.get_name())