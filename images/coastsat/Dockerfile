FROM conda/miniconda3
SHELL [ "/bin/bash", "-c" ]
COPY ./files/gcloud_cli/google-cloud-cli-481.0.0-linux-x86_64.tar.gz /gcloud_cli.tar.gz
COPY ./files/auth/gcloud_cli_auth.json /gcloud_cli_auth.json

# install gclould cli
RUN tar -xf ./gcloud_cli.tar.gz
RUN ./google-cloud-sdk/install.sh -q --path-update true
# RUN nl /root/.bashrc
# RUN source /root/.bashrc
# source using /root/.bashrc not adding path, dont know why
ENV PATH="/google-cloud-sdk/bin:${PATH}"

# authenticate gcloud cli
ENV KEY_FILE="/gcloud_cli_auth.json"
RUN gcloud auth login --cred-file=$KEY_FILE

RUN conda install -c conda-forge geopandas -y
RUN conda install -c conda-forge earthengine-api scikit-image matplotlib astropy notebook -y
RUN pip install pyqt5 imageio-ffmpeg