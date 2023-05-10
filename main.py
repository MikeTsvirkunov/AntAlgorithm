from flask import Flask, render_template, url_for, make_response

app = Flask(__name__)

@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)