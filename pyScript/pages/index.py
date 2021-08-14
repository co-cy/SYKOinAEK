from flask import Blueprint, jsonify

blueprint = Blueprint("index", __name__)


@blueprint.route('/')
def index():
    return jsonify({"status": "OK"})
