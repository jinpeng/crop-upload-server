## crop-upload-server
Server side code of [crop-upload](https://github.com/jinpeng/crop-upload), a small tool for cropping and uploading image to Qiniu cloud.  

### Features
- Generate upload token for Qiniu cloud

### For Developers

#### Techniques:
- Python 3
- Falcon 1.3
- Qiniu
- Gunicorn

#### Run:
Python 3.6 installed, virtual env and wrapper installed.
Download source code and run:

```
$ git clone https://github.com/jinpeng/crop-upload-server.git
$ cd crop-upload-server
$ mkvirtualenv ~/envs/qiniu
$ workon qiniu
$ (qiniu) pip install -r requirements.txt
$ gunicorn app
```
Test it with httpie:

```
$ brew install httpie
$ http localhost:8000/uptoken
HTTP/1.1 200 OK
Connection: close
Date: Fri, 29 Dec 2017 06:52:02 GMT
Server: gunicorn/19.7.1
access-control-allow-origin: *
content-length: 135
content-type: application/json; charset=UTF-8

{
    "token": "LOU-8mkMgbXPU1x8emTOmy6nQ7UE5ZzA_H_xpgjH:fWc6BmvdJUdQbFndm_515P5C3Xg=:eyJzY29wZSI6ImppdHU6IiwiZGVhZGxpbmUiOjE1MTQ1MzM5MjJ9"
}
```

