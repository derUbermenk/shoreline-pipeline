FROM continuumio/miniconda3

COPY ./files/gcloud_cli/google-cloud-cli-481.0.0-linux-x86_64.tar.gz /gcloud_cli.tar.gz
COPY ./files/auth/gcloud_cli_auth.json /gcloud_cli_auth.json

# install gclould cli
RUN tar -xf /gcloud_cli.tar.gz
RUN ./google-cloud-sdk/install.sh -q --path-update true
RUN source /root/.bashrc

# authenticate gcloud cli
ENV KEY_FILE = "/gcloud_cli_auth.json"
RUN gcloud auth login --cred-file=$KEY_FILE