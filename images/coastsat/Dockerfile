FROM condaforge/mambaforge:24.3.0-0

SHELL [ "/bin/bash", "-c" ]
WORKDIR /home
COPY ./files/gcloud_cli/google-cloud-cli-481.0.0-linux-x86_64.tar.gz /home/gcloud_cli.tar.gz
COPY ./files/auth/gcloud_cli_auth.json /home/gcloud_cli_auth.json
COPY ./CoastSat /home/CoastSat

# install gclould cli
RUN tar -xf /home/gcloud_cli.tar.gz
RUN /home/google-cloud-sdk/install.sh -q --path-update true

# using source /root/.bashrc does not add to path, dont know why
# this way we set it manually
ENV PATH="/home/google-cloud-sdk/bin:${PATH}"

# authenticate gcloud cli
ENV KEY_FILE="/home/gcloud_cli_auth.json"
RUN gcloud auth login --cred-file=$KEY_FILE

WORKDIR /home/CoastSat
RUN cp coastSatRunner.py coastSatRunner
RUN chmod +x coastSatRunner
ENV PATH="/home/CoastSat:${PATH}"
RUN yes | mamba env create -f /home/CoastSat/environment.yml && \
    mamba clean --all --yes && \
    rm -rf /opt/conda/pkgs

# Change the default shell to use mamba run in the coastsat environment
SHELL ["mamba", "run", "-n", "coastsat", "/bin/bash", "-c"]

# RUN pip install pyqt5 imageio-ffmpeg 

# running application
# CMD ["mamba", "run", "-n", "coastsat", "python", "your_script.py"]
# CMD ["mamba", "run", "-n", "coastsat", "jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]

ENTRYPOINT [ "mamba", "run", "-n", "coastsat", "coastSatRunner"]
