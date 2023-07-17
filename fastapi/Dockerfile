FROM python:3.8

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    curl \
    libturbojpeg0

RUN pip3 install requests \
                 numpy \
                 PyTurboJPEG \
                 line_profiler

# COPY requirement_fastapi.txt requirement_fastapi.txt
# RUN pip3 install -r requirement_fastapi.txt
RUN pip3 install fastapi \
                 uvicorn
COPY . .

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

ENTRYPOINT ["/bin/bash", "-c", "uvicorn fastapi_server:app --reload --host 0.0.0.0 --port ${API_PORT}"]