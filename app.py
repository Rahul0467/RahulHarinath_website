from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/experience")
def experience():
    return render_template("experience.html")

if __name__ == "__main__":
    app.run(debug=True)