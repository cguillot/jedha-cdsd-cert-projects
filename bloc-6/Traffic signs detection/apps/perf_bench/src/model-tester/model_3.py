from ultralytics import YOLO
from PIL import Image
import cv2
import numpy as np
import time

model = None
classNames = ['Green Light', 'Red Light', 'Speed Limit 10', 'Speed Limit 100', 'Speed Limit 110', 'Speed Limit 120', 'Speed Limit 20', 'Speed Limit 30', 'Speed Limit 40', 'Speed Limit 50', 'Speed Limit 60', 'Speed Limit 70', 'Speed Limit 80', 'Speed Limit 90', 'Stop']

import os

def warm():
    global model
    if model is None:

        yolo_base_dir = os.getenv('DSFS_FT_31_MODELS_BASE_DIR', '/app/src/model-tester/models')
        print(f'loading model {yolo_base_dir}...')
        model = YOLO(f'{yolo_base_dir}/yolov11n-best_ncnn_model', task='detect', verbose=True)
        print('model loaded')

def predict(image, to_rgb = True):
    global model

    print('predicting model...')
    if model is None:
        warm()
        
    infer_start_time = time.perf_counter()

    results = model(image, imgsz=480)
    
    infer_end_time = time.perf_counter()

    elapsed_time_ms = (infer_end_time - infer_start_time) * 1000

    print(f"model_3 inferred in: {elapsed_time_ms:.3f} ms")

    res_plotted = results[0].plot()
    
    if type(image) is not np.ndarray:
        img_rgb = cv2.cvtColor(res_plotted, cv2.COLOR_BGR2RGB)
    else:
        img_rgb = res_plotted

    detected = []
    for bbox in results[0].boxes:
        detected.append({'confidence': float(bbox.conf), 'label_name': classNames[int(bbox.cls)]})

    print(detected)
    description = str(results[0].speed) + " " + str(detected)
    
    stats = {
        'time_to_predict_ms': elapsed_time_ms
    }

    return { "image": img_rgb, "description": description, "detections": detected, "stats": stats }
