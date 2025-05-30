from ultralytics import YOLO
from PIL import Image
import cv2
import numpy as np

model = None
classNames = ['Green Light', 'Red Light', 'Speed Limit 10', 'Speed Limit 100', 'Speed Limit 110', 'Speed Limit 120', 'Speed Limit 20', 'Speed Limit 30', 'Speed Limit 40', 'Speed Limit 50', 'Speed Limit 60', 'Speed Limit 70', 'Speed Limit 80', 'Speed Limit 90', 'Stop']

import os

def warm():
    global model
    if model is None:
        # export DSFS_FT_31_MODELS_BASE_DIR=$(pwd)/src/model-tester
#        yolo_base_dir = os.getenv('DSFS_FT_31_MODELS_BASE_DIR', '/app/src/model-tester')

#        print(f'loading model {yolo_base_dir}...')
#        model = YOLO(f'{yolo_base_dir}/yolov11n-best_ncnn_model', task='detect')
        model = YOLO('./yolo11n-home-trained-30-epochs_ncnn_model', task='detect')
        print('model loaded')

def predict(image, to_rgb = True):
    global model

    print('predicting model...')
    if model is None:
        warm()
        
    results = model(image, imgsz=480)

    res_plotted = results[0].plot()
    
    if type(image) is not np.ndarray:
        img_rgb = cv2.cvtColor(res_plotted, cv2.COLOR_BGR2RGB)
    else:
        img_rgb = res_plotted

    # View results
    # for r in results:
    #     print(r.summary)  # print the Probs object containing the detected class probabilities

    detected = []
    for bbox in results[0].boxes:
        detected.append({'conf': f'{float(bbox.conf):.2f}', 'cls' : int(bbox.cls), 'label': classNames[int(bbox.cls)]})
        

    print(detected)
    description = str(results[0].speed) + " " + str(detected)

    return { "image": img_rgb, "description": description, "detected": detected}
