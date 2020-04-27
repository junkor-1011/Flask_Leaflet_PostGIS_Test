# (Args)
# ARG: BASE_IMAGE
# ARG: USER_UID


ARG BASE_IMAGE=python:3.7-slim-buster


FROM ${BASE_IMAGE}

# system update & package install
RUN apt-get clean && \
    apt-get -y update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    libpcre3 libpcre3-dev \
    zlib1g zlib1g-dev \
    openssl libssl-dev \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
# todo: 要不要の選別など

# user        
# ref:
# https://zukucode.com/2019/06/docker-user.html
# https://qiita.com/Riliumph/items/3b09e0804d7a04dff85b
# 一般ユーザーアカウントを追加
ENV USER_NAME=app
ARG USER_UID=1000
ARG PASSWD=password

RUN useradd -m -s /bin/bash -u ${USER_UID} ${USER_NAME} && \
    gpasswd -a ${USER_NAME} sudo && \
    echo "${USER_NAME}:${PASSWD}" | chpasswd && \
    echo "${USER_NAME} ALL=(ALL) ALL" >> /etc/sudoers
# 一般ユーザーにsudo権限を付与
#RUN gpasswd -a ${UID} sudo


# https://medium.com/@rlagowski/create-flask-app-with-uwsgi-nginx-certbot-for-ssl-and-all-this-with-docker-a9f23516618d
COPY ./requirements.txt /tmp/requirements.txt
#COPY ./app /app
RUN mkdir /app
RUN chown -R ${USER_NAME}:${USER_NAME} /app # --chown= では環境変数の代入が効かない

USER ${USER_UID}
WORKDIR /app

# pip
ENV PATH $PATH:/home/${USER_NAME}/.local/bin
RUN python3 -m pip install --user --upgrade pip && \
    python3 -m pip install -r /tmp/requirements.txt --user

CMD ["uwsgi", "--ini", "uwsgi.ini"]

