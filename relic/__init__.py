import logging
import os

from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

CONFIGURATION_LOCATION = 'FLASK_CONFIG'

sql_alchemy = SQLAlchemy()


def create_app() -> Flask:
    app = Flask(__name__, static_folder='../app/build', static_url_path='/')
    app.config.from_object('config')
    if CONFIGURATION_LOCATION in os.environ.keys():  # if FLASK_CONFIG defined in environment
        app.config.from_envvar(CONFIGURATION_LOCATION)  # then overwrite flask.config from that file
    print(f'!!!: {app.debug}')
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',
                        level=logging.DEBUG if app.debug else logging.INFO)
    # from here on log using app.logger (or 'current_app.logger' in the context of a http request)
    app.logger.info(f"Debug? {app.debug}")
    if app.debug:
        CORS(app)
    app.logger.info(f"Should we use the cloud? {app.config['CLOUD']}")

    # db initilization (this is going to use the SQL_ALCHEMY_... variables from the configuration)
    # in production you use some other config.py file pointed to by the FLASK_CONFIG env variable
    sql_alchemy.init_app(app)
    from relic.database import db
    db.init_app(app)

    # blueprint initializations (API endpoints, one file per version)
    from relic import api
    app.register_blueprint(api.bp)

    # the following setup code is when we are in development mode only, with an in memory database
    # in that case, create tables and fill them with test data
    if app.debug:
        db.create_all()
        with db.engine.connect() as connection:
            res = next(connection.execute('select count(*) from users'))
            if res[0] == 0:
                with app.open_resource('data.sql', 'rb') as resource:
                    sql = str(resource.read(), 'utf8')
                    for statement in sql.split(';'):
                        with connection.begin() as transaction:
                            try:
                                connection.execute(statement)
                                transaction.commit()
                            except Exception as e:
                                app.logger.error(e)
                                transaction.rollback()

    @app.errorhandler(Exception)
    def handle_error(ex):
        return jsonify(error=str(ex)), 500

    @app.errorhandler(404)
    def not_found(e):
        return app.send_static_file('index.html')

    @app.route('/')
    def index():
        return app.send_static_file('index.html')

    return app