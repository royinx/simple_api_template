# pylint: disable=import-error,unexpected-keyword-arg
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Roy
"""
# Python standard libararies
import sys

# 3rd party libararies
from turbojpeg import TurboJPEG
from robyn import Robyn, jsonify

app = Robyn(__file__)

jpeg = TurboJPEG()

@app.post("/test/")
async def inference(req):
    data = req.body # list
    data = bytes(data) # bytes
    img = jpeg.decode(data)
    # print(sys.getsizeof(data))
    # print(sys.getsizeof(img))
    # print(img.shape)
    return jsonify({"shape": img.shape})

@app.get("/healthcheck/")
async def check_health():
    return {"Status": 1}

if __name__ == '__main__':  # local dev
    port = int(sys.argv[1])

    print("Robyn server configuration is done!")
    print('API is running!')
    print('LocalIP: {} , Port: {}'.format("localhost",port))

    print()
    app.start(host="0.0.0.0", port=port)