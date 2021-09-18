from flask import Flask
from flask import request
import markdown
from flask import Flask
import markdown.extensions.fenced_code
import os.path
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from model.score  import init, run

app = Flask(__name__)

init()

@app.route("/")
def intro():
    readme_file = open("INTRO.md", "r")
    md_template_string = markdown.markdown(
        readme_file.read(), extensions=["fenced_code"]
    )
    return md_template_string

@app.route("/api/classify", methods=['POST'])
def classify():
    classify_response = run(request.get_data())
    return (classify_response)

if __name__ == 'main':
    app.run(debug = True, host='0.0.0.0', port=8000)