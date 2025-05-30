import os
import yaml
from pathlib import Path
from roboflow import Roboflow

ROBOFLOW_API_KEY=os.environ.get('ROBOFLOW_API_KEY')

print(os.environ)
print('ROBOFLOW_API_KEY: ', ROBOFLOW_API_KEY)

DATASET_BASE_DIR=os.environ.get("YOLO_DATASET_BASE_DIR", "./data/self-driving-cars")

rf = Roboflow(api_key=ROBOFLOW_API_KEY)

project = rf.workspace("selfdriving-car-qtywx").project("self-driving-cars-lfjou")
version = project.version(6)
dataset = version.download("yolov11", location=DATASET_BASE_DIR, overwrite=False)

# Fix paths, as for some reasons, they are wrong!

def fix_dataset_yaml(dataset_base_dir):
    yaml_path = Path(f"{dataset_base_dir}/data.yaml").resolve()

    with open(yaml_path, "r") as f:
        data_cfg = yaml.safe_load(f)

    data_cfg['train'] = data_cfg.get('train').replace('..', '.')
    data_cfg['val'] = data_cfg.get('val').replace('..', '.')
    data_cfg['test'] = data_cfg.get('test').replace('..', '.')

    with open(yaml_path, "w") as f:
        yaml.dump(data_cfg, f)

fix_dataset_yaml(DATASET_BASE_DIR)
