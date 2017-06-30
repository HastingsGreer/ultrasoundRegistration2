from flask import Flask, request
app = Flask(__name__)

import pickle, time
@app.route('/upload', methods=["POST"])
def upload():
    print(request.get_json())
    pickle.dump(request.get_json(), open(str(time.time()), "wb"))
    return ""

app.run(host='0.0.0.0', port=80)