from flask import (Flask,render_template, request)
from nfl_sports_betting import calculate_winner

app = Flask(__name__)

@app.route("/")
def index() :

    return render_template("matt_test.html")

@app.route("/", methods=['GET','POST'])
def post_winner() :
#    if request.method == "POST" :
#        home = ** get dropdown home team 1 from html input **
#        away = ** get dropdown away 1 from html input **
#	    winner = calculate_winner(home, away)
#    return render_template(‘matt_test.html', winner=winner)

    return render_template("matt_test.html", winner = calculate_winner("Buffalo Bills", "Miami Dolphins"))