import sys
import json
import random
import requests
from turbojpeg import TurboJPEG
from line_profiler import LineProfiler 
import numpy as np
# import time

profile = LineProfiler()

# -------- COPY -------- 
class CFG(object):
    def __init__(self,container_name:str ,port:int ):
        self.ip = f'http://{container_name}' # container_name : flask / fastapi
        self.port = port
        self.url = f'{self.ip}:{self.port}/test/'
        self.test_url = f'{self.ip}:{self.port}/test/'

@profile
def encode(img: np.ndarray):
    pass 
def decode(): 
    pass


if __name__ == '__main__':
    # cfg = CFG("flask",8080) # if flask : 2809 , fastapi : 2810
    cfg = CFG("fastapi",8080)
    jpeg = TurboJPEG()
    input_img = 'rabbit.jpeg'
    with open(input_img, 'rb') as infile:
        bgr_array = jpeg.decode(infile.read())


    img_enc = jpeg.encode(bgr_array,quality=20)
    print(type(img_enc))
    print(sys.getsizeof(bgr_array))
    print(sys.getsizeof(img_enc))

    print(cfg.url)
    try:
        response = requests.post(cfg.url,data=img_enc)
        if response.status_code==200:
            print("Success")
        else:
            raise(response.status_code)
    except:
        raise("fail")


    # print('save image: {}'.format(time.time() - start))


    # if img_list is not None:
    #   req_list = [{ 
    #       'type': 'normal',
    #       'request_id': 'asdgasdusydahrf', 
    #       'cam_id': '0',
    #       'images': img_list,
    #       'bbox_confidences': [0.8,0.9,0.9],
    #       'mask_confidences': [0.7,0.6,0.9],
    #       'filter':[], 
    #   }]
    #   req_list = json.dumps(req_list,ensure_ascii=False)


    # print('url: ',cfg.url)
    # # print(tracker_id_list)
    # # req_list = json.dumps(1)
    # # print(type(req_list))
    # second = time.time()
    # print('**************1************')

    # try:
    #   response = requests.post(cfg.url,json=req_list)
    #   if response.status_code==200:
    #       print(time.time()-second)
    # except:
    #   print('API Server is not opening ')
    #   exit(0)




    # print('api time: {}'.format(time.time() - second)