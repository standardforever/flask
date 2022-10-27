from flask import Flask
from flask import jsonify


app = Flask(__name__)

@app.route('/')
def hello_world():
    return {"slackUsername": "standardforever","backend": True,"age": 21 ,"bio": "I am passionate about tech"}

if __name__ == "__main__":
    app.run(debug=False)
