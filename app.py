from flask import Flask, render_template, request

app = Flask(__name__)

parse = lambda x: x == "Yes" or x == "yes"

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/quiz")
def quiz():
    return render_template("quiz.html")

@app.route("/results", methods=["GET","POST"])
def results():
    if request.method == "POST":
        history = parse(request.form.get("family_history"))
        smoker = parse(request.form.get("smoker"))
        alcohol = parse(request.form.get("drink"))
        diabetes = parse(request.form.get("diabetes"))
        minYears = int(request.form.get("years"))
        #sedated = parse(request.form.get("sedation"))
        diet = parse(request.form.get("fasting"))
        home = parse(request.form.get("home"))

        return other_super_advanced_parser(superadvancedaimodel(history,smoker,alcohol,diabetes,minYears,diet,home))
    return render_template("results.html")


def superadvancedaimodel(history,smoker,alcohol,diabetes,minYears,diet,home):
    if history:
        return "colonoscopy"
    if smoker and alcohol or smoker and diabetes or alcohol and diabetes or alcohol and smoker and diabetes:
        return "colonoscopy"
    if smoker or alcohol or diabetes:
        if diet:
            return "virtualcolonoscopy"
        if minYears == 1:
            return "fecaloccultbloodtest"
        else:
            return "stooldnatest"
    if home:
        return "stooldnatest"
    return "colonoscopy"

def other_super_advanced_parser(string):
    return render_template(string+".html")
