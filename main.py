from flask import Flask, render_template, request

from config import path
from data_candidate import DataCandidates

app = Flask(__name__)

data_candidates = DataCandidates(path)


@app.route('/')
def list_():
    return render_template('list.html',
                           data_candidates=data_candidates.load_candidate(),
                           title="Кандидаты",
                           all="Все кандидаты")


@app.route('/candidate/<int:pk>/')
def single(pk):
    return render_template('single.html',
                           candidates=data_candidates.get_id(pk),
                           title="Кандидат",
                           all="Данные о кандидате")


@app.route('/search/')
@app.route('/search/<name>')
def search(name=None):
    if name is None:
        name = request.args.get('query')
    candidates = data_candidates.get_by_name(name)
    return render_template('search.html',
                           title="Найдено кандидатов",
                           candidates=candidates,
                           count_names=len(candidates))


@app.route('/skill/')
@app.route('/skill/<skills>')
def skill_name(skills=None):
    if skills is None:
        skills = request.args.get("skill")
    get_by_skills = data_candidates.get_by_skills(skills)
    return render_template('skill.html',
                           title="Поиск по навыкам",
                           get_by_skills=get_by_skills,
                           count_skills=len(get_by_skills))


@app.route('/index/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
