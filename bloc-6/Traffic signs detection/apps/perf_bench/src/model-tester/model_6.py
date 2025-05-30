import time
import logging
from ultralytics import YOLO
from PIL import Image
import cv2
import numpy as np
from models.custom_models.models import model1, model2, panneau_classes

import os

c = 0

def predict(image):
    #global model
    global c

    print('prediction model_6...')
    
    print(panneau_classes)

    panneau_shape = (64, 64)

    image_h = 480
    image_w = 640

    minR = 10
    # minR = round(image_w/65)
    maxR = 70
    # maxR = round(image_w/11)
    minDis = 20
    # minDis = round(image_w/7)

    th1 = 23
    th2 = 72

    th1 = 30
    th2 = 90

    seuil_model1 = .2
    seuil_model2 = .33

    r_min = 10
    rbords = .15

    r_speed = 1

    # PIL Image
    # Resize the image to 640x480
    print('image: ', image.size)
    if type(image) is np.ndarray:
        image_array = image.reshape(480, 640, 3)
    else:
        print('image type: ', type(image))
        image_resized = image.resize((640, 480))
        print('image_resized: ', image_resized.size)
        # Convert the image to a NumPy array
        image_array = np.array(image_resized)


    if model1 is None or model2 is None:
        print('model_6 base models not loader!')
        
        stats = {
            'time_to_predict_ms': 0
        }
       
        return { "image": image_array, "description": "Models not loaded", "detections": [], "stats": stats }

    # Ensure the shape is (640, 480, 3)
    print(image_array.shape)

    frame = cv2.cvtColor(image_array, cv2.COLOR_BGR2RGB)

    frame_o = frame.copy()

    infer_start_time = time.perf_counter()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.1, minDis, param1=th1, param2=th2, minRadius=minR, maxRadius=maxR)

    id_panneau = -1
    c += 1

    detections = []

    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")

        print("circles: ", circles) #len(circles[0,:]))
        for (x, y, r) in circles:
            c += 1

            if r > 10 :
                y1 = max(0, int((y-r)-(r*rbords)))
                y2 = min(image_h, int((y+r)+(r*rbords)))
                x1 = max(0, int((x-r)-(r*rbords)))
                x2 = min(image_w, int((x+r)+(r*rbords)))

                panneau_s = cv2.resize(frame[y1:y2, x1:x2], panneau_shape)
                panneau = panneau_s / 255

                print (c)

                cv2.circle(frame_o, (x, y), r, (0, 255, 0), 2)
                cv2.rectangle(frame_o, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

                prediction = model1(np.array([panneau]), training = False)
                print('model1 preds: ', prediction)
                if prediction[0][0]> seuil_model1 :
                    print('over treshold')
                    prediction = model2(np.array([panneau]), training = False)
                    id_panneau_max = np.argmax(prediction[0])

                    if (prediction[0][id_panneau_max] > seuil_model2) :
                        id_panneau = id_panneau_max
                        print("panneau", prediction[0][id_panneau], id_panneau, panneau_classes[id_panneau])

                        detected = {
                            'xmin': x1,
                            'ymin': y1,
                            'xmax': x2,
                            'ymax': y2,
                            'label_id': id_panneau,
                            'label_name': panneau_classes[id_panneau],
                            'confidence': prediction[0][id_panneau]
                        }

                        detections.append(detected)

    infer_end_time = time.perf_counter()
    
    description = 'Nothing'

    if id_panneau != -1:
        description = 'panneau: ' + panneau_classes[id_panneau]

    for detected in detections:
        x1, y1, x2, y2 = detected['xmin'], detected['ymin'], detected['xmax'], detected['ymax']
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to int values

        cv2.rectangle(image_array, (x1, y1), (x2, y2), (255, 0, 255), 3)

    elapsed_time_ms = (infer_end_time - infer_start_time) * 1000

    print(f"model_6 inferred in: {elapsed_time_ms:.3f} ms")
    print('model_6 predicted: ', description)

    stats = {
        'time_to_predict_ms': elapsed_time_ms
    }
    
    return { "image": image_array, "description": description, "detections": detections, "stats": stats }
