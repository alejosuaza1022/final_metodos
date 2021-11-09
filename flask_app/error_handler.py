from flask import json
from werkzeug.exceptions import HTTPException
from flask import jsonify


def set_error_handler(app):
    @app.errorhandler(Exception)
    def handle_exception(e):
        if isinstance(e, HTTPException):
            response = e.get_response()
            response.data = json.dumps({
                "code": e.code,
                "name": e.name,
                "description": e.description,
            })
            response.content_type = "application/json"
            return response
        print(str(e))
        return jsonify(error=str(e), code=500), 500
