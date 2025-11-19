import flask
from flask import Flask, jsonify, request, render_template


app = Flask(__name__)

HABITS_LIST = []

@app.route('/', methods=['GET'])
def index():
    return render_template('homepage.html')
@app.route('/habitpage', methods=['GET'])
def habitpage():
    return render_template('habitpage.html')
if __name__ == '__main__':
    app.run(debug = True)