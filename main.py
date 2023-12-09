from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("register.html")

app.run('0.0.0.0', 80, debug=True)