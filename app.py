from flask import Flask, render_template, request, url_for, redirect, flash
from game_of_life import GameOfLife

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sdfiygfyasdbsahdbyuasf'

@app.route('/index', methods=['POST', 'GET'])
def index():

    if request.method == "POST":
        if request.form['height'] and request.form['weight']:
            height = request.form['height']
            weight = request.form['weight']
            GameOfLife(int(height), int(weight))
            return redirect(url_for('live'))
        else:
            GameOfLife(25, 25)
            return redirect(url_for('live'))

    return render_template('index.html')


@app.route('/live')
def live():
    game = GameOfLife()
    if game.generation_count > 0:
        game.form_new_generation()
    game.generation_count += 1
    return render_template('live.html', game=game, counter=game.generation_count)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
