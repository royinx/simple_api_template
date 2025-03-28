# Simple Flask Template

## Quick Start
```bash
# docker-compose build
docker-compose up
```

<details>
<summary>Developments</summary>

## Build
```bash
cd <dir: fastapi_dir / flask_dir >
```
## Flask API
```
docker build -f dockerfile_flask -t flask .
docker run --name=flask \
           --rm \
           -it \
           -p 2809:8080 \
           --ip="flask" \
           -v ${PWD}:/py \
           -w /py \
           flask
```

## FastAPI
```
docker build -f dockerfile_fastapi -t fastapi .
docker run --name=fastapi \
           --rm \
           -it \
           -p 2810:8080 \
           --ip="fastapi" \
           -v ${PWD}:/py \
           -w /py \
           fastapi
```

## Robyn
```
docker build -f dockerfile_fastapi -t fastapi .
docker run --name=fastapi \
           --rm \
           -it \
           -p 2810:8080 \
           --ip="fastapi" \
           -v ${PWD}:/py \
           -w /py \
           fastapi
```


## client
```
docker build -f dockerfile_client -t client .
docker run --rm -it --name client -v $PWD:/py -w /py client bash
python3 api_test.py
```

</details>


---
`TurboJPEG` is a fast library for imencode and decode while i wanna put benchmarking there instead of open a new repo.<br/>
check out `jpg.py`
