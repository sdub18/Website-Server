#
#  __init__.py
#  Website Server
#
#  Created by Sam DuBois on 6/25/20.
#

import os

from flask import Flask

def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE = os.path.join(app.instance_path, 'website_server.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when NOT testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test test_config
        app.config.from_mapping(test_config)

    # ensure that the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'Hello, World'

    # Initialize Database
    from . import db
    db.init_app(app)

    # Register Authentication Blueprint
    from . import auth
    app.register_blueprint(auth.bp)

    return app
