# FROM continuumio/miniconda3:24.4.0-0
FROM mambaorg/micromamba:1-lunar
WORKDIR /home
SHELL [ "/bin/bash", "-c" ]

COPY ./files/gcloud_cli/google-cloud-cli-481.0.0-linux-x86_64.tar.gz ./gcloud_cli.tar.gz
COPY ./files/auth/gcloud_cli_auth.json ./gcloud_cli_auth.json
COPY ./files/CoastSat-master ./CoastSat-master

# install gclould cli
RUN tar -xf ./gcloud_cli.tar.gz
RUN ./google-cloud-sdk/install.sh -q --path-update true
# using source /root/.bashrc not adding path, dont know why
# this way we set it manually
ENV PATH="/home/google-cloud-sdk/bin:${PATH}"

# authenticate gcloud cli
ENV KEY_FILE="/home/gcloud_cli_auth.json"
# RUN gcloud auth login --cred-file=$KEY_FILE

WORKDIR /home/CoastSat-master
RUN micromamba create -n coastsat
# RUN micromamba shell reinit --bash
RUN micromamba shell reinit
RUN micromamba activate coastsat
RUN micromamba install -c conda-forge geopandas -y
RUN micromamba install -c conda-forge earthengine-api scikit-image matplotlib astropy notebook -y
RUN pip install pyqt5 imageio-ffmpeg