import os

from relic import create_app

if __name__ == '__main__':
    app = create_app()
    os.environ['FLASK_DEBUG'] = '1'
    app.run(port=5000, debug=True)
