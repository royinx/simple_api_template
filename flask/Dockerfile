FROM python:3.8

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    curl \
    libturbojpeg0

RUN pip3 install requests \
                 numpy \
                 PyTurboJPEG \
                 line_profiler

# COPY requirement_flask.txt requirement_flask.txt
# RUN pip3 install -r requirement_flask.txt
RUN pip3 install flask \
                 flask_cors \
                 gunicorn

COPY . .

ENTRYPOINT ["/bin/bash", "-c", "gunicorn --bind 0.0.0.0:${API_PORT} flask_server:app"]