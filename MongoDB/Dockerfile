FROM ubuntu:latest

USER docker

WORKDIR /mongodb-deployment

COPY ./entry_point.sh ./entry_point.sh

CMD ["bash", "entry_point.sh"]
