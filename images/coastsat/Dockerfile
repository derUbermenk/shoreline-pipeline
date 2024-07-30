FROM condaforge/mambaforge:24.3.0-0

ARG COASTSAT_BRANCH=master
ENV REPO_ZIP=https://github.com/derUbermenk/CoastSat/archive/refs/heads/${COASTSAT_BRANCH}

RUN apt-get update \
    && apt-get install -y unzip \
    && rm -rf /var/lib/apt/lists/*

SHELL [ "/bin/bash", "-c" ]
COPY ./files/gcloud_cli/google-cloud-cli-481.0.0-linux-x86_64.tar.gz /gcloud_cli.tar.gz
COPY ./files/auth/gcloud_cli_auth.json /gcloud_cli_auth.json
COPY ./environment.yml /environment.yml
COPY ./cs_runner_initializer.sh /usr/local/bin/cs_runner_initializer

RUN chmod +x /usr/local/bin/cs_runner_initializer
ENV PATH="/usr/local/bin:${PATH}"


# install gclould cli
RUN tar -xf /gcloud_cli.tar.gz
RUN /google-cloud-sdk/install.sh -q --path-update true

# using source /root/.bashrc does not add to path, dont know why
# this way we set it manually
ENV PATH="/google-cloud-sdk/bin:${PATH}"

# authenticate gcloud cli
ENV KEY_FILE="/gcloud_cli_auth.json"
RUN gcloud auth login --cred-file=$KEY_FILE

RUN yes | mamba env create -f /environment.yml && \
    mamba clean --all --yes && \
    rm -rf /opt/conda/pkgs

# Change the default shell to use mamba run in the coastsat environment
# SHELL ["mamba", "run", "-n", "coastsat", "/bin/bash", "-c"]

ENTRYPOINT [ "mamba", "run", "-n", "coastsat", "cs_runner_initializer"]
