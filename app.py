from flask import Flask, jsonify, request, render_template


app = Flask(__name__, template_folder='templates')

@app.route("/home")
def index():
    return render_template('index.html')

@app.route("/upload/", methods=["POST"])
def uploadFiles():
    return "in file upload page"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)