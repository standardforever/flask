from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

"""Stage 1 Task"""
@app.route('/')
def hello_world():
    return {"slackUsername": "standardforever","backend": True,"age": 21 ,"bio": "I am passionate about tech"}

@app.route('/cal', methods = ['POST'])
def calculation():
    result = 0
    """Possible options"""
    lis = ['+', '-', '*', 'addition', 'subtraction',
         'multiplication', 'add', 'subtract', 'multiply', 'product']

    """Get the json request"""    
    data = request.get_json()
    opera = data.get("operation_type")
    x = data.get("x")
    y = data.get("y")
    """Split the opertion field to check if it is a string"""
    spli = ""
    try:
        spli = opera.split(' ')
    except:
        pass
    if (len(spli) > 1):
        for i in spli:
            if (i in lis):
                opera = i
                break

    """Validate the input and perform action"""
    if (isinstance(y, int) and isinstance(x, int) and opera):
        if (opera == lis[3] or opera == lis[0] or opera == lis[6]):
            result = x + y
        elif (opera == lis[4] or opera == lis[1] or opera == lis[7]):
            result = x - y
        elif (opera == lis[5] or opera == lis[2] or opera == lis[8] or opera == lis[9]):
            result = x * y
        return ({"slackUsername": "standardforever",
                    "operation_type": opera,
                    "result": result
            })
    return ("Wrong format")
            


if __name__ == "__main__":
    app.run(debug=False)
