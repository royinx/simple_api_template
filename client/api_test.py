import sys
import requests
from turbojpeg import TurboJPEG
from line_profiler import LineProfiler
# import time

profile = LineProfiler()

# -------- COPY --------
class CFG(object):
    def __init__(self,container_name:str ,port:int ):
        self.ip = f'http://{container_name}' # container_name : flask / fastapi
        self.port = port
        self.url = f'{self.ip}:{self.port}/test/'
        self.test_url = f'{self.ip}:{self.port}/healthcheck/'

if __name__ == '__main__':
    jpeg = TurboJPEG()
    input_img = 'rabbit.jpeg'
    with open(input_img, 'rb') as infile:
        bgr_array = jpeg.decode(infile.read())


    img_enc = jpeg.encode(bgr_array,quality=20)
    # print(type(img_enc))
    # print(sys.getsizeof(bgr_array))
    # print(sys.getsizeof(img_enc))

    def send(ip , port , img_enc):
        try:
            # response = requests.get(f"http://{ip}:{port}/healthcheck")
            response = requests.post(f"http://{ip}:{port}/test/",data=img_enc)
            if response.status_code==200:
                print(f"[Success] - http://{ip}:{port}/test/ \t status: {response.status_code} \t {response.json()}")
            else:
                raise(response.status_code)
        except:
            raise("fail")

    import time
    time.sleep(5)
    while 1:
        send("fastapi", 9000, img_enc)
        time.sleep(1)
        send("flask", 9000, img_enc)
        time.sleep(1)
        send("robyn", 9000, img_enc)
        time.sleep(1)
        send("rust_axum", 9000, img_enc)
        time.sleep(1)