from flask import Flask, jsonify, request, make_response, url_for, redirect, render_template, session, Session

app = Flask(__name__, static_url_path = "")
app.config['SECRET_KEY'] = '123456'

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/option")
def option():
    return render_template("option.html")

@app.route("/mycourse")
def mycourse():
    return render_template("mycourse.html")

@app.route("/query")
def query():
    return render_template("query.html")





if __name__ == '__main__':   
    app.run(debug = True, host= '0.0.0.0')
