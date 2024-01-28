from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/A")
def choice_a():
    return render_template("a_index.html")

@app.route("/B")
def choice_b():
    return render_template("b_index.html")

@app.route("/team")
def team():
    return render_template("team.html")

if __name__ == "__main__":
    app.run(debug=True)