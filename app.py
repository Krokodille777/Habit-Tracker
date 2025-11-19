import flask
from flask import Flask, jsonify, request, render_template


app = Flask(__name__)
# Simple endpoint that returns a greeting message
@app.route('/hello', methods=['GET'])
def hello_world():
    return jsonify(message="Hello, World!")
# New endpoint that echoes back JSON data sent in the POST request
@app.route('/echo', methods=['POST'])
def echo():
    data = request.json
    return jsonify(data)  
# Endpoint to render a simple HTML page
@app.route('/page', methods=['GET'])
def render_page():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)