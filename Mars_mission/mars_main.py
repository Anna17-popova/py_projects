from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    text = 'Заготовка'
    return render_template('base.html', title=text)


@app.route('/training/<prof>')
def training(prof):
    return render_template('professions.html', prof=prof)


@app.route('/list_prof/<type>')
def list_prof(type):
    if type not in 'olul':
        print('WRONG PARAMS')
        return
    return render_template('list_professions.html', type=type)


@app.route('/answer')
@app.route('/auto_answer')
def auto_answer():
    title, surname, name, education, profession, sex, motivation, ready =\
        'Анкета', 'Popova', 'Anna', '-', '-',\
        'female', 'Всегда мечтал застрять на Марсе!', 'True'
    return render_template('auto_answer.html', title=title, surname = surname, name=name, education=education,
                           profession=profession, sex=sex, motivation=motivation, ready=ready)


if __name__ == '__main__':
    app.run(port=8070, host='127.0.0.1')
