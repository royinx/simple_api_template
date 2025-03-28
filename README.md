# Simple Flask Template

## Quick Start
```bash
# docker-compose build
docker-compose up
```

<details>
<summary>prompt</summary>

i am writing a rust axum api server
i want to implement 2 endpoint
1. healthcheck
>  get method , will return the json below
```python
@app.get("/healthcheck/")
async def check_health():
    return {"Status": 1}
```
2. test
> post method, will recieve a JPG file , and use `zune-jpeg` library  to decode image and return the shape in json format
```python
@app.post("/test/")
async def inference(req: Request):
    data = await req.body()
    img = jpeg.decode(data)
    # print(sys.getsizeof(data))
    # print(sys.getsizeof(img))
    # print(img.shape)
    return JSONResponse(content=json.dumps({"shape": img.shape}))
```

</details>




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

`zune-jpeg`(Rust) is on par with `libjpeg-turbo` (C).
