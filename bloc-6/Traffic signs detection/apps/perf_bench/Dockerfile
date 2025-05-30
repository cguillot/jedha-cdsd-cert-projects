FROM continuumio/miniconda3

# Update base image and install some required dependencies
RUN apt-get update && \
    apt-get install curl nano unzip ffmpeg libsm6 libxext6  -y --no-install-recommends && \
    apt-get clean && \
    apt-get autoremove && \
    rm -rf /var/cache/apt/archives/* && \
    rm -rf /var/lib/apt/lists/*

# Create a new user and set up the environment
ARG USERNAME=user
ARG USER_UID=1000
ARG USER_GID=1000

# Create a non-root user and setup permissions
RUN groupadd --gid $USER_GID $USERNAME && \
    useradd --uid $USER_UID --gid $USER_GID -m $USERNAME && \
    mkdir -p /home/$USERNAME && \
    chown -R $USERNAME:$USERNAME /home/$USERNAME

# Switch to the new user
USER $USERNAME

# Prepare python env
WORKDIR /build-env
RUN cat <<EOF > /build-env/docker-environment.yml
name: docker-env
dependencies:
  - python=3.11
  - pip
EOF

# Use Bash shell
SHELL ["/bin/bash", "-c"]

WORKDIR /home/$USERNAME

RUN conda init && \
    /bin/bash -c "source ~/.bashrc && \
    conda env create --file=/build-env/docker-environment.yml -y && \
    echo 'conda activate docker-env' >> ~/.bashrc"

###############################################################################
# Prepare application
#
# Set working directory and permissions
WORKDIR /app
#RUN chown -R $USERNAME:$USERNAME /app

COPY --chown=user requirements.txt /build-env/
RUN conda run -n docker-env pip install --no-cache-dir -r /build-env/requirements.txt
COPY --chown=user . /app
RUN ["chmod", "+x", "/app/run.sh"]

ENV SERVER_PORT=7860

EXPOSE $SERVER_PORT

ENV DSFS_FT_31_MODELS_BASE_DIR="/app/src/model-tester/models"

# tell PyTorch to not use the GPU?
ENV CUDA_VISIBLE_DEVICES=""

#CMD [ "/app/run.sh"]
ENTRYPOINT ["/app/run.sh"]
