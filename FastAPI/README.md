# WebApp with FastAPI framework

![FastAPI](./logo/fastapi-logo.png)

### Steps

Create and activate the dedicated virtual environment
```bash
$ python3 -m venv venv  && . venv/bin/activate

!!!Deactivate the dedicated virtual environment
$ deactivate
``` 

Install [FastAPI](https://fastapi.tiangolo.com/) dependencies
```bash
$ pip install fastapi
$ pip install uvicorn
``` 

Check the app locally 
```bash
$ uvicorn main:app --reload 

OR 

Call directly from main script 
``` 

Freeze all the project dependencies into requirements.txt
```bash
$ pip freeze > requirements.txt
``` 

Build Image
```bash
$ docker build -t python-api .
``` 

Run Container
```bash
$ docker run -p 8000:8000 python-api
where: 
    "-p" flag - mapping forwarding of ports
``` 

