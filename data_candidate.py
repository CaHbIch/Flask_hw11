import json

from candidate import Candidates


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
                skills = candidat["skills"]

                candidats = Candidates(pk, name, picture, position, gender, age, skills)
                candidates.append(candidats)

            return tuple(candidates)

    def get_id(self, pk):
        """ возвращает одного кандидата по его pk"""
        gets_id = self.load_candidate()
        candidates_get_id = []
        for candidate in gets_id:
            if candidate.pk == pk:
                candidates_get_id.append(candidate.position)
                candidates_get_id.append(candidate.picture)
                candidates_get_id.append(candidate.skills)
        return candidates_get_id

    def get_by_name(self, name):
        """возвращает имена кандидатов"""
        candidates = self.load_candidate()
        candidates_match = []
        for candidate in candidates:
            if name.lower() in candidate.name.lower():
                candidates_match.append(candidate)
        return candidates_match

    def get_by_skills(self, skills):
        """возвращает навыки кандидатов"""
        skill = self.load_candidate()
        get_skills = []
        for candidate_skills in skill:
            get_skill = candidate_skills.skills.lower().split(', ')
            if skills in get_skill:
                get_skills.append(candidate_skills)
        return get_skills
