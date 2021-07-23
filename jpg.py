import base64
import cv2
import numpy as np 
from turbojpeg import TurboJPEG

import sys

from line_profiler import LineProfiler

profile = LineProfiler()

@profile 
def compress_encode_image(image: np.ndarray, quality: int = 30) -> str:
    """ Compress numpy array image and encode the compressed numpy array into byte string """
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY),
                    quality]
    ret, jpg = cv2.imencode(
        ".jpg", image, encode_param)
    if ret:
        return base64.b64encode(jpg).decode("ascii")
    raise Exception("Failed to compress image")

@profile 
def decode_decompress_image(image: str) -> np.ndarray:
    """ decode a byte string into numpy array and decompress it into an image """
    compressed = np.frombuffer(base64.b64decode(image), dtype=np.uint8)
    return cv2.imdecode(compressed, 1)

@profile 
def main():
    input_img = "rabbit.jpeg"
    output_name = 'output.jpg'
    jpeg = TurboJPEG()

    # print("=============Read Image=============")
    img = cv2.imread(input_img)

    with open(input_img, 'rb') as infile:
        img = jpeg.decode(infile.read())


    # print("=============Write Image=============")
    
    cv2.imwrite(output_name,img)

    with open(output_name, 'wb') as outfile:
        outfile.write(jpeg.encode(img,quality=30))
    base1 = jpeg.encode(img,quality=30)
    base64.b64encode(base1).decode("ascii")
    # print("=============Python Utils=============")

    base2 = compress_encode_image(img)
    decode_decompress_image(base2)

    # print(sys.getsizeof(base1))
    # print(sys.getsizeof(base2))
    
if __name__ == "__main__":
    for i in range(100):
        main()

    profile.print_stats()


# apt-get install -y libturbojpeg0
# pip3 install numpy opencv-python PyTurboJPEG line_profiler