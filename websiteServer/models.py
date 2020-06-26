##
##  article.py
##  Website-Server
##
##  Created by Sam DuBois on 6/23/20.
##  Copyright © 2020 Samuel DuBois. All rights reserved.
##

from flask_sqlalchemy import SQLAlchemy
from websiteServer import db
from marshmallow import Schema, fields

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1000), unique=False, nullable=False)
    subtitle = db.Column(db.String(2000), unique=False, nullable=False)

class ArticleSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    subtitle = fields.Str()
