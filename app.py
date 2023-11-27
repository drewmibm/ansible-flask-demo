from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return """<h1>Howdy</h1>
<p>This site was configured with Ansible</p>
"""