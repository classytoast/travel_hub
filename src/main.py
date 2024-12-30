from flask import Flask, render_template

from config import DEBUG

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def main_view():
    """Главная страница сайта"""
    return render_template(
        'index.html',
        title='Travel hub'
    )


if __name__ == '__main__':
    app.run(debug=DEBUG)
