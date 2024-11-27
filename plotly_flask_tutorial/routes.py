"""Routes for parent Flask app."""
from flask import current_app as app
from flask import render_template, request, redirect, url_for, session
import psycopg2

app.secret_key = "completelyrandomstring"

@app.route("/")
def home():
    datatext = session["datatext"] if "datatext" in session else "test"
    playername = session["playername"] if "playername" in session else "test2"
    """Home page of Flask Application."""
    return render_template(
        "index.jinja2",
        title="Plotly Dash Flask Tutorial",
        description="Embed Plotly Dash into your Flask applications.",
        template="home-template",
        body="This is a homepage served with Flask.",
        base_url=request.base_url,
        datatext=datatext,
        playername=playername,
    )

@app.route("/data")
def data_func():
    conn = psycopg2.connect("dbname='nfl' user='postgres' host='db' password='example'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM quarterback LIMIT 50;")
    res = cur.fetchone()
    cur.close()
    conn.close()
    session["datatext"] = str(res)
    return redirect(url_for("home"))

@app.route("/playerdata", methods = ['GET', 'POST'])
def player_data():
    session["playername"] = request.form.get("playername")
    return redirect(url_for("home"))
