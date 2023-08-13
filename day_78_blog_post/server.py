from flask import Flask, render_template
from datetime import datetime
import requests


app = Flask(__name__)

year = datetime.now().year
name = "Ahmad Khairi"

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
blog_response = requests.get(url=blog_url)
all_posts = blog_response.json()

@app.route('/')
def home():
    return render_template("index.html", posts=all_posts, name=name, year=year)

@app.route("/post/<int:blog_id>")
def get_post(blog_id):
    blog_title = all_posts[blog_id - 1]["title"]
    blog_body = all_posts[blog_id - 1]["body"]
    return render_template("post.html", title=blog_title, body=blog_body, name=name, year=year)

if __name__ == "__main__":
    app.run(debug=True)
