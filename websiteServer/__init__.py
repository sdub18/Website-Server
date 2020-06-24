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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/data.db'
db = SQLAlchemy(app)

# MARK: Initial Internal Route
@app.route('/', methods=['GET'])
def welcomeClient():
    return jsonify({'message': 'Welcome to my Website Backend'})

# MARK: Import Other Routes
import websiteServer.articleRoutes

# MARK: Run Server
if __name__ == '__main__':
    db.create_all()
    app.run()
