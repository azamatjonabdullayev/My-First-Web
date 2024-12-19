from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
@app.route("/home")
def main_page():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/support")
def support():
    return render_template("support.html")


if __name__ == "__main__":
    app.run(debug=True)
