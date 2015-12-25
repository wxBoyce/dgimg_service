#!/usr/bin/env python
# -*- coding: utf-8 -*-

import flask
import pymongo
import bson.binary
import bson.objectid

app = flask.Flask(__name__)
app.debug = True

db = pymongo.MongoClient('localhost', 27017).test


@app.route('/img/<fid>')
def serve_file(fid):
    f = db.files.find_one(bson.objectid.ObjectId(fid))
    return flask.Response(f['content'], mimetype='image/' + f['mime'])

if __name__ == '__main__':
    app.run(port=10081)
