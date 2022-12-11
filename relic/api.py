import requests
from flask import Blueprint, jsonify

bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/')
def api_index():
    return jsonify(status='ok')


@bp.route('/drouot')
def api_drouot():
    session = requests.Session()
    res = session.get('https://drouot.com')
    print(res.status_code)
    return jsonify(status='ok')
