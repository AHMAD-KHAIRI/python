from flask import Flask, render_template
import random, requests
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    year = datetime.now().year
    name = "Ahmad Khairi"
    random_number = random.randint(1, 10)
    return render_template("index.html",num=random_number, year=year, name=name)

@app.route("/guess/<name>")
def guess(name):
    name = name.title()
    genderize_endpoint = "https://api.genderize.io/"
    agify_endpoint = "https://api.agify.io/"
    parameter = {
        "name": name
        }
    genderize_response = requests.get(url=genderize_endpoint, params=parameter)
    gender = genderize_response.json()["gender"]
    agify_response = requests.get(url=agify_endpoint, params=parameter)
    age = agify_response.json()["age"]
    # return f"<h1>Hey {name}!<br><br>I think you are {gender},<br><br>And maybe {age} years old.</h1>"
    return render_template("guess.html", name=name, gender=gender, age=age)

@app.route("/blog/<num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_response = requests.get(url=blog_url)
    blog_posts = blog_response.json()
    return render_template("blog.html", posts=blog_posts)

if __name__ == "__main__":
    app.run(debug=True)