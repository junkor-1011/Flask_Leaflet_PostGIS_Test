#!/usr/bin/env python

import json, io, datetime, codecs, os, random
from uuid import uuid4
from hashlib import md5, sha256

# Flask
from flask import Flask, render_template, request, jsonify, make_response,\
    send_file, session, abort, flash, url_for, redirect, Response
# Flask-SQLAlchemy
#from flask_sqlalchemy import SQLAlchemy
from database import db, init_db
import models
from models import GeoPointTestA, User, Dots, Flights, Iris
# from models import **, **, ...

# logging
# ref: https://qiita.com/amedama/items/b856b2f30c2f38665701
from logging import getLogger, StreamHandler, DEBUG
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

# Mapbox
try:
    #from .mapbox_settings import access_token
    from confs.mapbox_settings import access_token
except Exception as e:
    logger.warning(f"Import Error{str(e)}")
    logger.warning(f"No Mapbox-accessToken")


# create app
def create_app():
    """
    """

    app = Flask(__name__)

    app.secret_key = md5(str(uuid4()).encode()).hexdigest()     # 要らないかも?
    app.config['SECRET_KEY'] = sha256(str(uuid4()).encode()).hexdigest()
    app.config.from_object('confs.config_db.Config')

    init_db(app)
    
    return app

app = create_app()


@app.route('/', methods=['GET'])
def main():
    title = "Main Menu"
    return render_template('main.html', title=title, access_token=access_token)
    

@app.route('/post_test_tmp1', methods=['POST'])
def post_test_tmp1():
    arg1 = request.form['arg1']
    arg2 = request.form['arg2']
    response_object = {
        "message": "Hello, WORLD",
        "get_args":
            {"arg1": arg1, "arg2": arg2},
    }
    return Response(response=json.dumps(response_object), status=200)


@app.route('/models_test/create_user', methods=['POST'])
def models_test_create_user():
    #data = json.loads(request.get_json())  # todo: headerでContent-Typeを確認する方がベターかも
    json_data = json.dumps(request.get_json())  # todo: headerでContent-Typeを確認する方がベターかも
    data = json.loads(json_data)
    print(data)

    user = User.register_user(data)

    return Response(response=json.dumps({'user': user,}), status=200)


@app.route('/models_test/get_users', methods=['GET'])
def models_test_get_users():
    #users = User.get_users()
    results = User.get_users()

    #return Response(response=json.dumps({'users': users}), status=200)
    return Response(response=json.dumps({'results': results}), status=200)


@app.route('/models_test/get_users_with_text', methods=['GET'])
def models_test_get_users_with_text():
    users = User.get_users_with_text()

    return Response(response=json.dumps({'users': users}), status=200)


@app.route('/users/<int:id>', methods=['GET'])
def users_rest_id(id):
    """
    """
    if request.method == "GET":
        user = db.session.query(User).filter(User.id == id).first()
        if user is not None:
            return Response(response=json.dumps(user.to_dict()), status=200)
        else:
            return Response(response=json.dumps({}), status=200)
    else:
        abort(400)
        return


@app.route('/users/utils/columns', methods=['GET'])
def users_get_columns():

    columns = User.__table__.c.keys()

    return Response(response=json.dumps({'columns': columns}), status=200)


if __name__ == '__main__':
    app.debug = True
    app.run(
            #host='0.0.0.0',
            #port=5000,
            #ssl_context=('ssl/server.crt', 'ssl/server.key'),
            #threaded=True,        
    )
