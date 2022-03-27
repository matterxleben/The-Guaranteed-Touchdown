from flask import (Flask,render_template, request)
from nfl_sports_betting import calculate_winner
 
app = Flask(__name__)
 
@app.route("/")
def index() :
 
    return render_template("matt_test.html")
 
@app.route("/", methods=['GET','POST'])
def post_winner() :
    if request.method == "POST" :
        home = request.form['Hteam']
        away = request.form['Ateam']
        win = calculate_winner(home, away)
    return render_template('matt_test.html', winner=win)
 
    #return render_template("matt_test.html", winner = calculate_winner("Buffalo Bills", "Miami Dolphins"))