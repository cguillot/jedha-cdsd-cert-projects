import numpy as np
import os
import cv2
import random
from tensorflow.keras import layers, Sequential

panneau_shape=(64, 64)
rep_panneaux="panneaux"
rep_panneaux_diff="panneaux_diff"
rep_non_panneaux="non_panneaux"


def create_model1(p_shape) :
    
    model = Sequential()
    
    model.add(layers.Input(shape = (p_shape[0], p_shape[1], 3), dtype='float32'))
    
    model.add(layers.Conv2D(64, 3, strides=1))
    model.add(layers.BatchNormalization())
    model.add(layers.Activation('relu'))
    model.add(layers.MaxPool2D(pool_size=2, strides=2))
    
    model.add(layers.Conv2D(128, 3, strides=1))
    model.add(layers.BatchNormalization())
    model.add(layers.Activation('relu'))
    model.add(layers.MaxPool2D(pool_size=2, strides=2))
    
    model.add(layers.Flatten())
    model.add(layers.Dense(256, activation='relu'))
    model.add(layers.BatchNormalization())
    model.add(layers.Dense(1, activation='sigmoid'))

    return(model)
    

def create_model2(p_shape, nombre_classes) :
    
    model=Sequential()

    model.add(layers.Input(shape = (p_shape[0], p_shape[1], 3), dtype='float32'))
    
    model.add(layers.Conv2D(128, 3, strides=1))
    model.add(layers.Dropout(0.2))
    model.add(layers.BatchNormalization())
    model.add(layers.Activation('relu'))
    
    model.add(layers.Conv2D(128, 3, strides=1))
    model.add(layers.Dropout(0.2))
    model.add(layers.BatchNormalization())
    model.add(layers.Activation('relu'))
    
    model.add(layers.MaxPool2D(pool_size=2, strides=2))
    
    model.add(layers.Conv2D(256, 3, strides=1))
    model.add(layers.Dropout(0.3))
    model.add(layers.BatchNormalization())
    model.add(layers.Activation('relu'))
    
    model.add(layers.Conv2D(256, 3, strides=1))
    model.add(layers.Dropout(0.4))
    model.add(layers.BatchNormalization())
    model.add(layers.Activation('relu'))
    
    model.add(layers.MaxPool2D(pool_size=2, strides=2))
    
    model.add(layers.Flatten())
    model.add(layers.Dense(512, activation='relu'))
    model.add(layers.Dropout(0.5))
    model.add(layers.BatchNormalization())
    
    model.add(layers.Dense(nombre_classes, activation='softmax'))

    return (model)
    

def get_panneaux (rep_panneaux, redim) :

    list_panneau_files = sorted(os.listdir(rep_panneaux))
    panneaux = list()
    panneaux_images = list()

    for file in list_panneau_files :
        panneaux.append(file.split(".")[0])
        image = cv2.imread(rep_panneaux + "/" + file)
        image = cv2.resize(image, (redim[0], redim[1]))
        panneaux_images.append(image)

        
    return panneaux, np.array(panneaux_images)


def generate_images(image, nombre_images) :

    h, w, c = image.shape
    list_images = list()
    
    for _ in range(nombre_images) :
        list_images.append(generate_modif_image(image))
    
    return list_images

    
def generate_modif_image(image):
    h, w, c = image.shape

    # coleur unie autour du panneau 
    r_color = [np.random.randint(255), np.random.randint(255), np.random.randint(255)]
    image = np.where(image == [142, 142, 142], r_color, image).astype(np.uint8)

    if np.random.randint(3):
        k_max = 3
        kernel_blur = np.random.randint(k_max) * 2 + 1
        image = cv2.GaussianBlur(image, (kernel_blur, kernel_blur), 0)

    M = cv2.getRotationMatrix2D((int(w/2), int(h/2)), random.randint(-10, 10), 1)
    image = cv2.warpAffine(image, M, (w, h))
        
    if np.random.randint(2):
        a = int(max(w, h)/5)+1
        pts1 = np.float32([[0, 0], [w, 0], [0, h], [w, h]])
        pts2 = np.float32([[0+random.randint(-a, a), 0+random.randint(-a, a)], [w-random.randint(-a, a), 0+random.randint(-a, a)], [0+random.randint(-a, a), h-random.randint(-a, a)], [w-random.randint(-a, a), h-random.randint(-a, a)]])        
        M = cv2.getPerspectiveTransform(pts1,pts2)
        image = cv2.warpPerspective(image, M, (w, h))
        
    if np.random.randint(2):
        r = random.randint(0, 5)
        h2 = int(h*0.9)
        w2 = int(w*0.9)
        if r == 0:
            image = image[0:w2, 0:h2]
        elif r == 1:
            image = image[w-w2:w, 0:h2]
        elif r==2:
            image=image[0:w2, h-h2:h]
        elif r==3:
            image=image[w-w2:w, h-h2:h]
        image=cv2.resize(image, (h, w))

    if np.random.randint(2):
        r=random.randint(1, int(max(w, h)*0.15))
        image = image[r:w-r, r:h-r]
        image=cv2.resize(image, (h, w))

    if not np.random.randint(4):
        t = np.empty((h, w, c) , dtype=np.float32)
        for i in range(h):
            for j in range(w):
                for k in range(c):
                    t[i][j][k]=(i/h)
        M = cv2.getRotationMatrix2D((int(w/2), int(h/2)), np.random.randint(4)*90, 1)
        t = cv2.warpAffine(t, M, (w, h))
        image = (cv2.multiply((image/255).astype(np.float32), t)*255).astype(np.uint8)

    # gamma
    image = np.clip(random.uniform(0.6, 1.0) * image - np.random.randint(50), 0, 255).astype(np.uint8)
  
    if not np.random.randint(4):
        p=(15+np.random.randint(10))/100
        image=(image*p+50*(1-p)).astype(np.uint8)+np.random.randint(100)

    # bruit
    n = np.random.randn(h, w, c) * random.randint(5, 30)
    image = np.clip(image + n, 0, 255).astype(np.uint8)
        
    return image

