```
Check docker version 
$ docker -v

List Docker Containers
$ docker ps 
$ docker ps -a # all dockers

Create docker Image 
$ docker build -t <image-name> .
    e.g. docker build -t python-imdb . 

Run Docker Container
$ docker run <image-name> 
    e.g. docker run python-imdb 

Run Docker Container with interactive (-i) and sudo (-t) mode 
$ docker run -t -i <image-name> 
    e.g. docker run -t -i python-imdb     


```
