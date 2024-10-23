"""Routes for parent Flask app."""
from flask import current_app as app
from flask import render_template, request
import psycopg2

@app.route("/")
def home():
    """Home page of Flask Application."""
    return render_template(
        "index.jinja2",
        title="Plotly Dash Flask Tutorial",
        description="Embed Plotly Dash into your Flask applications.",
        template="home-template",
        body="This is a homepage served with Flask.",
        base_url=request.base_url,
    )

@app.route("/data")
def data_func():
    conn = psycopg2.connect("dbname='nfl' user='postgres' host='db' password='example'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM quarterback LIMIT 50;")
    res = cur.fetchone()
    cur.close()
    conn.close()
    return (str(res))
