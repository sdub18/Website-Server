##
##  article-routes.py
##  Website-Server
##
##  Created by Sam DuBois on 6/23/20.
##  Copyright © 2020 Samuel DuBois. All rights reserved.
##

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from websiteServer import app, db
from websiteServer.models import Article

# MARK: POST Article to database
@app.route('/articles', methods=['GET'])
def getArticles():
    return jsonify({'test': 'This did work!'})
