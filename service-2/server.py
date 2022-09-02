from flask import Flask
import pathlib

app = Flask(__name__)

@app.route('/service2')
def index():
    return "Web App with Python Flask in servise-2\n"

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0')