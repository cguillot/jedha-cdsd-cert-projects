# Usage:
#
# - build:
#     dotenv -e .env docker build --build-arg ROBOFLOW_API_KEY -t yolo-train .
#
# - run:
#     docker run --gpus all -it --rm -v ${pwd}/work:/model yolo-train
#
FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 \
    libglib2.0-0

WORKDIR /build-env

# Prepare python env
RUN cat <<EOF > /build-env/requirements.txt
pandas
python-dotenv
pyaml
roboflow
ultralytics
EOF

RUN pip install -r /build-env/requirements.txt

# docker build --build-arg ROBOFLOW_API_KEY
ARG ROBOFLOW_API_KEY

ENV ROBOFLOW_API_KEY=$ROBOFLOW_API_KEY
ENV YOLO_DATASET_BASE_DIR="/yolo-data/self-driving-cars"

COPY ./prepare_dataset.py /build-env/prepare_dataset.py

RUN python /build-env/prepare_dataset.py

VOLUME /model

ENV YOLO_PROJECT_DIR=/model

COPY ./train_yolo.py /build-env/train_yolo.py

CMD [ "python", "/build-env/train_yolo.py"]
