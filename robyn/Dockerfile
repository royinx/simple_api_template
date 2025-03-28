FROM python:3.11-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    curl \
    libturbojpeg0

COPY requirements.txt requirements.txt
RUN pip3 install uv --no-cache-dir
RUN uv pip install --no-cache-dir -r requirements.txt --system
COPY . .
ENTRYPOINT ["/bin/bash", "-c", "python3 server.py ${API_PORT}"]

# docker build -t roycicd/simple_api_template:robyn .
# docker run --rm -it -e API_PORT=8080 -p 3214:8080 \
#             roycicd/simple_api_template:robyn
