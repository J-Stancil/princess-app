from flask import Flask, render_template
from data import tree

app = Flask(__name__)

@app.route("/")
def start():
    return render_template("index.html")

@app.route("/tree")
def tree_view():
    return render_template("tree.html", tree=tree)

if __name__ == "__main__":
    app.run(debug=True)