from flask import Flask
from flask import jsonify


app = Flask(__name__)

@app.route('/')
def hello_world():
    return '({"SlackUsername": "","Backend": True,"Age": 21,"Bio": "I am passionate about tech"})'

if __name__ == "__main__":
    app.run(debug=False)
