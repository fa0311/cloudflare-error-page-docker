import json
import os

from cloudflare_error_page import render as render_cf_error_page
from flask import Flask, request


def create_app() -> Flask:
    app = Flask(__name__)

    with open("params.json") as f:
        params = json.load(f)

    def update_params(params: dict):
        if params.get("ray_id") is None:
            if request.headers.get("Cf-Ray"):
                params["ray_id"] = request.headers.get("Cf-Ray")[:16]
        if params.get("client_ip") is None:
            params["client_ip"] = request.headers.get(
                "X-Forwarded-For", request.remote_addr
            )
        if params.get("host_status", {}).get("location") is None:
            params["host_status"]["location"] = request.host
        return render_cf_error_page(params), params.get("error_code", 500)

    @app.route("/")
    def index():
        copy_params = params.copy()
        return update_params(copy_params)

    # 500.html などの 数字.html
    @app.route("/<int:error_code>.html")
    def error_page(error_code: int):
        copy_params = params.copy()
        copy_params["error_code"] = error_code
        return update_params(copy_params)

    @app.route("/health")
    def health():
        return "OK", 200

    return app


if __name__ == "__main__":
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "5000"))
    create_app().run(host=host, port=port)
