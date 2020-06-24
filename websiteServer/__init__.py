##
##  application.py
##  Website-Server
##
##  Created by Sam DuBois on 6/23/20.
##  Copyright © 2020 Samuel DuBois. All rights reserved.
##

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# MARK: Instantiate Our Server and Database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.app = app

# MARK: Import Other Routes
import websiteServer.models
import websiteServer.articleRoutes

# MARK: Initial Internal Route
@app.route('/', methods=['GET'])
def welcomeClient():
    return jsonify({'message': 'Welcome to my Website Backend'})

db.create_all()

# MARK: Run Server
if __name__ == '__main__':
    app.run()
