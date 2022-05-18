from flask import Flask, render_template

from candidate import Candidates
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


@app.route('/search/<candidate_name>')
def search():
    return render_template('search.html', candidate_name = data_candidates.get_name())
#
#
# @app.route('/search/<skill_name>')
# def skill_name():
#     return render_template('skill.html')


@app.route('/index/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
