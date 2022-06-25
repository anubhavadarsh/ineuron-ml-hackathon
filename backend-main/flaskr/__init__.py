from flask import Flask, request


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # a simple page that says hello
    @app.route("/hello", methods=["POST"])
    def hello():
        return str(request.json)

    return app
