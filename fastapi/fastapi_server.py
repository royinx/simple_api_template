# pylint: disable=import-error,unexpected-keyword-arg
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Roy
"""
# Python standard libararies
import os
from pathlib import Path
import sys
import json

# 3rd party libararies
import requests
import numpy as np 
from turbojpeg import TurboJPEG
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()
jpeg = TurboJPEG()

@app.post("/test/")
async def inference(req: Request):
    data = await req.body()
    img = jpeg.decode(data)
    print(sys.getsizeof(data))
    print(sys.getsizeof(img))
    print(img.shape)
    return JSONResponse(content=json.dumps(1))

@app.get("/test_api/")
async def check_health():
    return {"Status": 1}


if __name__ == '__main__':  # local dev
    port = 8080
    print("FastAPI server configuration is done!")
    print('API is running!')
    print('LocalIP: {} , Port: {}'.format("localhost",port))
    # print('HostName: {} , LocalIP: {} , Port: {}'.format(,cfg.port))

    print()
    uvicorn.run(app, host="0.0.0.0", port=8080)

# uvicorn application:app --reload --port 8000
# curl localhost:8000/health