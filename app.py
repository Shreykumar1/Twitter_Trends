from flask import Flask, jsonify, render_template
from src.twitter_selenium import run_script

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/execute-script')
def run():
    document = run_script()
    if "error" in document:
        return jsonify({"error": document["error"]}), 500 
    return jsonify(document)

if __name__ == '__main__':
    app.run(debug=True)
