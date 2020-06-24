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
    firstArticle = Article.query.first()
    print(firstArticle)
    return jsonify({'test': 'This did work!'})

@app.route('/articles', methods=['POST'])
def postArticle():
    data = request.get_json()
    article = Article(title='dad', subtitle='icecream')
    db.session.add(article)
    db.session.commit()
    return "Success", 200
