from flask import Flask, render_template
import requests
from datetime import datetime

app = Flask(__name__)

year = datetime.now().year

blog_url = "https://api.npoint.io/3952e1745b93d62ae350"
# blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
blog_response = requests.get(url=blog_url)
all_posts = blog_response.json()

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html", posts=all_posts, year=year)

@app.route("/about")
def about():
    return render_template("about.html", year=year)

@app.route("/post/<int:blog_id>")
def get_post(blog_id):
    blog_date = all_posts[blog_id - 1]["date"]
    blog_title = all_posts[blog_id - 1]["title"]
    blog_subtitle = all_posts[blog_id - 1]["subtitle"]
    blog_body = all_posts[blog_id - 1]["body"]
    blog_image = all_posts[blog_id - 1]["image"]
    return render_template("post.html", date=blog_date, title=blog_title, subtitle=blog_subtitle, body=blog_body, image=blog_image, year=year)

@app.route("/contact")
def contact():
    return render_template("contact.html", year=year)

if __name__ == "__main__":
    app.run(debug=True)