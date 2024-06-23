FROM continuumio/miniconda3:24.4.0-0
SHELL [ "/bin/bash", "-c" ]
WORKDIR /home
COPY ./files/gcloud_cli/google-cloud-cli-481.0.0-linux-x86_64.tar.gz /home/gcloud_cli.tar.gz
COPY ./files/auth/gcloud_cli_auth.json /home/gcloud_cli_auth.json
COPY ./files/CoastSat-master /home/CoastSat-master

# install gclould cli
RUN tar -xf /home/gcloud_cli.tar.gz
RUN /home/google-cloud-sdk/install.sh -q --path-update true
# using source /root/.bashrc not adding path, dont know why
# this way we set it manually
ENV PATH="/home/google-cloud-sdk/bin:${PATH}"

# authenticate gcloud cli
ENV KEY_FILE="/home/gcloud_cli_auth.json"
RUN gcloud auth login --cred-file=$KEY_FILE
