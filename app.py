from crypt import methods
import os
from sre_constants import SUCCESS
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
from sqlalchemy import desc
from flask_migrate import Migrate



#importing the models file
from models import setup_db, Question, db





def create_app(test_config=None):
    # create and configure the app
    #this also sets up the models part
    app = Flask(__name__)
    migrate = Migrate(app, db)
    setup_db(app)
    CORS(app, resources={'/': {'origins': '*'}})


    # CORS Headers 
    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type,Authorization,true"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS"
        )
        return response


    @app.route('/')
    def heyyy():
        print('good morning africa')
        return f'hey world'
               

    return app
       

  
