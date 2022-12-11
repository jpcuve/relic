import requests
from flask import Blueprint, jsonify

bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/')
def api_index():
    return jsonify(status='ok')


@bp.route('/drouot')
def api_drouot():
    session = requests.Session()
    session.headers.update({
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9,fr;q=0.8,nl;q=0.7,de;q=0.6,ca;q=0.5',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    })
    res = session.get('https://drouot.com')
    print(res.status_code)
    return jsonify(status='ok')
