FROM python:3.7

RUN apt-get update && apt-get install -y libturbojpeg0 && \
    pip3 install -U git+git://github.com/lilohuang/PyTurboJPEG.git && \
    pip3 install requests line_profiler numpy