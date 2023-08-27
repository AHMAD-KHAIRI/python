from flask import Flask, render_template, request
import requests, smtplib, os
from datetime import datetime
from dotenv import load_dotenv

app = Flask(__name__)

# load python environment variable
load_dotenv()

my_email = os.environ.get("MY_EMAIL")
my_app_password = os.environ.get("MY_PASSWORD")

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

@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        sender_email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_app_password)
            connection.sendmail(
                from_addr= my_email, 
                to_addrs=my_email, 
                msg=f"Subject: AK's BLOG WEBSITE - You Got a New Message!\n\nName: {name}\nEmail: {sender_email}\nPhone: {phone}\nMessage:{message}"
                )

    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)