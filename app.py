from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/id/<int:id>', methods=['GET'])
def get(id):
    if id >= 5000:
        return 'true'
    else:
        return 'false'

@app.route('/id', methods=['POST'])
def post():
    data={'name': '야호', 'value': '52'}
    return data['name']

@app.errorhandler(405)
def method_not_allowed(e):
    data={'name': '야호','value': '52'}
    return data['name']

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)