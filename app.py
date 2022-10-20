from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
import data

app = Flask(__name__)
Bootstrap(app)


@app.route("/")
def index():
    profile = data.profile_exp
    tech_exp = data.technical_exp
    prof_exp = data.prof_exp
    return render_template("index.html", profile_exp=profile,
                           tech_exp=tech_exp, prof_exp=prof_exp)


if __name__ == "__main__":
    app.run(debug=True)
