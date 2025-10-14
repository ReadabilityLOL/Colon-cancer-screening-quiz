from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/quiz")
def quiz():
    return render_template("quiz.html")

@app.route("/results")
def results():
    return render_template("results.html")
