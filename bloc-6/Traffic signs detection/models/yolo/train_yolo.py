import os
from pathlib import Path
import torch
from ultralytics import settings, YOLO

# You can try with more workers.
# In case of `ERROR: Unexpected bus error encountered in worker. This might be caused by insufficient shared memory (shm).` stick to 1.
YOLO_WORKERS=os.environ.get("YOLO_WORKERS", 1)

YOLO_BATCH_SIZE=os.environ.get("YOLO_BATCH_SIZE", 10)
YOLO_NB_EPOCHS=os.environ.get("YOLO_NB_EPOCHS", 5)


# Define dataset base folder
DATASET_BASE_DIR = os.environ.get(
    "YOLO_DATASET_BASE_DIR", "./data/self-driving-cars")

# Define YOLO project outpu
YOLO_PROJECT_DIR = os.environ.get("YOLO_PROJECT_DIR", "./model")

# names: ['green_traffic_light', 'red_traffic_light', 'speed_limit_10', 'speed_limit_100', 'speed_limit_110', 'speed_limit_120', 'speed_limit_20', 'speed_limit_30', 'speed_limit_40', 'speed_limit_50', 'speed_limit_60', 'speed_limit_70', 'speed_limit_80', 'speed_limit_90', 'Stop']
LEARN_CLASSES = [0, 1, 4, 6, 7, 9, 11, 12, 13, 14]


def train(model, dataset_base_dir, project_dir="./model", learn_classes=LEARN_CLASSES, batch_size=10, nb_epochs=30, device='cpu'):
    data_path = Path(f"{dataset_base_dir}/data.yaml").resolve()

    print("Training on dataset located at: ", data_path)

    model.train(
        data=data_path,  # path to dataset YAML
        project=project_dir,
        # batch=-1,   # auto mode for 60% GPU memory utilization
        batch=batch_size,
        epochs=nb_epochs,  # number of training epochs
        workers=YOLO_WORKERS,
        imgsz=480,  # training image size
        fliplr=0,
        device=device,  # device to run on, i.e. device=0 or device=0,1,2,3 or device=cpu
        classes=learn_classes,
        patience=5,  # Number of epochs to wait without improvement in validation metrics before early stopping the training. Helps prevent overfitting
    )

device = "cpu"

if torch.cuda.is_available():
    device = 0

model = YOLO(f"${YOLO_PROJECT_DIR}/yolo11n.pt")

train(
    model,
    DATASET_BASE_DIR,
    project_dir=YOLO_PROJECT_DIR,
    batch_size=YOLO_BATCH_SIZE,
    nb_epochs=YOLO_NB_EPOCHS,
    device=device
)

print("Exporting best model to Tencent NCNN format...")
model.export(format='ncnn', imgsz=480)

print("\n\nDone ###############################################")
