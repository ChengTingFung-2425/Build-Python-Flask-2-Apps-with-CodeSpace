from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Miguel"}
    posts = [
        {
            "author": {"username": "John"},
            "body": "Beautiful day in Portland!",
        },
        {
            "author": {"username": "Susan"},
            "body": "The Avengers movie was so cool!"
        }, # Extendable
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)


if name == "__main__":
    app.run(debug=True)
