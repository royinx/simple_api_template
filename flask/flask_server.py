#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 09:01:21 2019

@author: Roy
"""
import sys
from flask import Flask, jsonify, request
# from gevent import monkey, pywsgi
from flask_cors import CORS
from turbojpeg import TurboJPEG

# monkey.patch_all()
app = Flask(__name__)
CORS(app,support_credentials=True)
jpeg = TurboJPEG()

@app.route('/test',methods=["POST"])
def test():
    data = request.data
    img = jpeg.decode(data)
    # print(sys.getsizeof(data))
    # print(sys.getsizeof(img))
    # print(img.shape)
    return jsonify(shape=img.shape)


@app.route('/healthcheck',methods=["GET"])
def test_api():
    return jsonify(Status=1)

if __name__ == '__main__':
    port = int(sys.argv[1])
    # server = pywsgi.WSGIServer(('0.0.0.0',cfg.port),app)

    print("Flask server configuration is done!")
    print('API is running!')
    print('LocalIP: {} , Port: {}'.format("localhost",port))
    # print('HostName: {} , LocalIP: {} , Port: {}'.format(,cfg.port))

    print()
    app.run(host='0.0.0.0', port=port)
    # server.serve_forever()
