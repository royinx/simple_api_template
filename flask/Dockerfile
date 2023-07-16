FROM duruo850/ubuntu18.04-python3.6

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    curl \
    libturbojpeg

RUN pip3 install requests \
                 numpy \
                 PyTurboJPEG \
                 line_profiler

COPY requirement_flask.txt requirement_flask.txt
RUN pip3 install -r requirement_flask.txt

COPY . .

ENTRYPOINT ["/bin/bash", "-c", "gunicorn --bind 0.0.0.0:${API_PORT} flask_server:app"]