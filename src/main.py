"""Simple Flask web application."""

from __future__ import annotations

import os

from flask import Flask


def create_app() -> Flask:
    """Create and configure the Flask application."""
    app = Flask(__name__)

    @app.route("/")
    def hello() -> str:
        """Return a friendly greeting."""
        return "Hello, world!"

    return app


def main() -> None:
    """Run the Flask development server."""
    port = int(os.environ.get("PORT", 5000))
    create_app().run(host="0.0.0.0", port=port)


if __name__ == "__main__":
    main()
