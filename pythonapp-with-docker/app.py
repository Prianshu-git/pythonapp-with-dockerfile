from flask import Flask, render_template, request
import random

app = Flask(__name__)

first_syllables = ["An", "El", "Jo", "Lu", "Ma", "Sa", "Na", "Da"]
second_syllables = ["na", "ra", "la", "vi", "el", "ah", "ie", "on"]
last_syllables = ["son", "man", "ley", "ton", "berg", "field", "wood", "ford"]

def generate_name():
    first = random.choice(first_syllables) + random.choice(second_syllables)
    last = random.choice(first_syllables) + random.choice(last_syllables)
    return f"{first} {last}"

@app.route("/", methods=["GET", "POST"])
def index():
    names = []
    count = 5  # default
    if request.method == "POST":
        count = int(request.form.get("count", 5))
        names = [generate_name() for _ in range(count)]
    return render_template("index.html", names=names, selected_count=count)

if __name__ == "__main__":
    app.run(debug=True)
