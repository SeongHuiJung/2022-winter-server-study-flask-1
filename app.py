from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/id/<int:id>', methods=['GET'])
def get(id):
    data={}
    if id >= 5000:
        data={'result': True }
    else:
        data={'result': False }
    return data

@app.route('/id', methods=['POST'])
def post():
    data=request.get_json()
    return jsonify({ "name": data['name'] })

@app.errorhandler(405)
def method_not_allowed(e):
    data=request.get_json()
    return jsonify({ "name": data['name'] })

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)