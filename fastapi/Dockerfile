FROM duruo850/ubuntu18.04-python3.6

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    curl \
    libturbojpeg

RUN pip3 install requests \
                 numpy \
                 PyTurboJPEG \
                 line_profiler

COPY requirement_fastapi.txt requirement_fastapi.txt 
RUN pip3 install -r requirement_fastapi.txt

COPY . .

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# ENTRYPOINT ["uvicorn","fastapi_server:app","--reload","--port","8080"]