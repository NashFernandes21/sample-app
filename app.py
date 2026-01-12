from flask import Flask, render_template, abort

app = Flask(__name__)

LESSON_PACKAGES = [
    {"id": 1, "type": "Manual", "instructor": "Mr Rahman", "price": "£30 per class", "tag": "Beginner friendly"},
    {"id": 2, "type": "Manual", "instructor": "Mr Robert", "price": "£30 per class", "tag": "Refresher course"},
    {"id": 3, "type": "Manual", "instructor": "Mr Tom", "price": "£30 per class", "tag": "Test preparation"},
    {"id": 4, "type": "Automatic", "instructor": "Mr Ryan", "price": "£35 per class", "tag": "City driving"},
    {"id": 5, "type": "Automatic", "instructor": "Mr Troy", "price": "£35 per class", "tag": "Evening lessons"},
    {"id": 6, "type": "Automatic + Theory", "instructor": "Mr Ahmed", "price": "£45 per class", "tag": "Full package"},
]

BLOG_POSTS = [
    {"id": 1, "title": "Top 5 Tips to Pass Your Driving Test First Time", "author": "AutoCar Instructors",
     "date": "03 Nov 2025","category": "Test Tips","excerpt": "Nailing your first test is all about preparation..."},
    {"id": 2, "title": "Manual vs Automatic: Which Should You Choose?", "author": "AutoCar Team",
     "date": "27 Oct 2025","category": "Lesson Advice","excerpt": "Unsure whether to book manual or automatic lessons?"},
    {"id": 3, "title": "What to Expect on Your First Driving Lesson", "author": "Instructor Ahmed",
     "date": "15 Oct 2025","category": "Beginner Guide","excerpt": "Here’s how your first lesson will run..."},
]


@app.route("/")
def index():
    return render_template("index.html", lesson_packages=LESSON_PACKAGES, posts=BLOG_POSTS)


@app.route("/post/<int:post_id>")
def post_detail(post_id):
    post = next((p for p in BLOG_POSTS if p["id"] == post_id), None)
    if not post:
        abort(404)
    return render_template("post_detail.html", post=post)

@app.route("/test")
def test():
    return "Flask is working!"


if __name__ == "__main__":
    app.run(debug=True)
