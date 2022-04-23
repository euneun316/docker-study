ARG UBUNTU_VERSION=18.04
FROM ubuntu:${UBUNTU_VERSION}

ARG PYTHON=python3.8
ARG PIP=pip

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install && apt-get install -y --no-install-recommends \
    nodejs \
    git \
    curl \
    vim \
    ssh \
    sudo \
    wget \
    python3.8 \
    python3-pip \
    python3.8-dev \
    npm

RUN rm /usr/bin/python3 && ln -s python3.8 /usr/bin/python3

RUN npm install -g yarn && npm cache clean -f && npm install -g n && n stable

RUN ${PYTHON} -m ${PIP} --no-cache-dir install -q --upgrade pip setuptools wheel

COPY ./news-kids-back/requirements.txt /tmp
WORKDIR /tmp
RUN ${PYTHON} -m ${PIP} install -r /tmp/requirements.txt
    
ENV LANG C.UTF-8

WORKDIR /app 
COPY ../news-kids-back /app/news-kids-back
COPY ../news-kids-front /app/news-kids-front

# React
EXPOSE 3000
WORKDIR /app/news-kids-front
RUN yarn
# RUN yarn start 0.0.0.0:3000

# Django
EXPOSE 8000
WORKDIR /app/news-kids-back
CMD python3 manage.py runserver 0.0.0.0:8000

COPY ./run_django.sh /app
# ENTRYPOINT ["sh","../run_django.sh"]
