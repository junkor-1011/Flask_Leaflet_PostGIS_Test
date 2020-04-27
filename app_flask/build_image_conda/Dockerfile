ARG BASE_IMAGE=debian:10-slim
FROM $BASE_IMAGE

USER root

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    wget \
    curl \
    bzip2 \
    ca-certificates \
    sudo \
    unzip \
    fontconfig \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


# add user
ENV USER_NAME=app
ARG USER_UID=1000
ARG PASSWD=password
RUN useradd -m -u ${USER_UID} ${USER_NAME} && \
    gpasswd -a ${USER_NAME} sudo && \
    echo "${USER_NAME}:${PASSWD}" | chpasswd && \
    echo "${USER_NAME} ALL=(ALL) ALL" >> /etc/sudoers

# prepare for conda
ENV CONDA_DIR=/opt/conda \
    HOME=/home/$USER_NAME \
    SHELL=/bin/bash

RUN mkdir -p $CONDA_DIR && \
    chown $USER_NAME:$USER_UID $CONDA_DIR

# ubuntu color-prompt
#RUN sed -i 's/^#force_color_prompt=yes/force_color_prompt=yes/' /etc/skel/.bashrc

# conda package-info
COPY ./packages_dev.yml /tmp/conda_packages.yml


# Flaskアプリ起動用設定
#COPY ./app /app
RUN mkdir /app
RUN chown -R ${USER_NAME}:${USER_NAME} /app


USER $USER_NAME

ENV CONDA_DIR=/opt/conda \
    HOME=/home/$USER_NAME \
    SHELL=/bin/bash

WORKDIR $HOME
ARG PYTHON_VERSION=default

#RUN echo $CONDA_DIR
# ref https://hub.docker.com/r/jupyter/base-notebook/dockerfile
ENV MINICONDA_VERSION=4.8.2 \
    MINICONDA_MD5=87e77f097f6ebb5127c77662dfc3165e \
    CONDA_VERSION=4.8.2 \
    PATH=${CONDA_DIR}/bin:$PATH
# https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
# https://repo.anaconda.com/miniconda/

RUN cd /tmp && \
    wget --quiet https://repo.continuum.io/miniconda/Miniconda3-py37_${MINICONDA_VERSION}-Linux-x86_64.sh && \
    echo "${MINICONDA_MD5} *Miniconda3-py37_${MINICONDA_VERSION}-Linux-x86_64.sh" | md5sum -c - && \
    /bin/bash Miniconda3-py37_${MINICONDA_VERSION}-Linux-x86_64.sh -f -b -p $CONDA_DIR && \
    rm Miniconda3-py37_${MINICONDA_VERSION}-Linux-x86_64.sh && \
    echo "conda ${CONDA_VERSION}" >> $CONDA_DIR/conda-meta/pinned && \
    conda config --system --prepend channels conda-forge && \
    conda config --system --set auto_update_conda false && \
    conda config --system --set show_channel_urls true && \
    conda config --system --set channel_priority strict && \
    if [ ! $PYTHON_VERSION = 'default' ]; then conda install --yes python=$PYTHON_VERSION; fi && \
    conda list python | grep '^python ' | tr -s ' ' | cut -d '.' -f 1,2 | sed 's/$/.*/' >> $CONDA_DIR/conda-meta/pinned && \
    conda install --quiet --yes conda && \
    conda install --quiet --yes pip && \
    conda update --all --quiet --yes && \
    conda clean --all -f -y && \
    rm -rf /home/$NB_USER/.cache/yarn

# install packages
RUN conda env update -n base -f /tmp/conda_packages.yml

# environment
# containerに入って作業するとき用(ubuntuだと確か不要)
RUN echo "export CONDA_DIR=/opt/conda \n" >> /home/${USER_NAME}/.bashrc && \
    echo "export PATH=\$SPARK_HOME/bin:\$CONDA_DIR/bin:\$JAVA_HOME/bin:\$PATH" >> /home/${USER_NAME}/.bashrc

#USER ${USER_UID}
WORKDIR /app

CMD ["uwsgi", "--ini", "uwsgi.ini"]
