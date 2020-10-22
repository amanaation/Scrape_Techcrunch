from flask import Flask, render_template
from scrape_techcrunch import Articles

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def home():
    art = Articles()
    art.get_new_articles()
    return "<h1> Completed Extraction </h1>"


if __name__ == "__main__":
    app.run(debug=True)
