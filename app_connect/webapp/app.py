from flask import Flask

def create_app() -> Flask:
    app = Flask(
        __name__,
        static_folder="static",
        static_url_path="/static"
    )

    from webapp.api.routes import bp
    app.register_blueprint(bp)

    @app.get("/")
    def index():
        return app.send_static_file("index.html")

    return app


app = create_app()