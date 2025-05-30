import numpy as np
import os
import cv2
import random
from tensorflow.keras import layers, Sequential

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

panneau_shape=(64, 64)

models_base_dir = os.getenv('DSFS_FT_31_MODELS_BASE_DIR').strip('"')

# check for existence of models weights
MODEL1_PATH = f'{models_base_dir}/custom_models/model1.h5'
MODEL2_PATH = f'{models_base_dir}/custom_models/model2.h5'

panneau_classes = ['30', '50', '70', '90', '110', '130']

if os.path.isfile(MODEL1_PATH) and os.path.isfile(MODEL2_PATH):
    model1 = create_model1(panneau_shape)
    model1.load_weights(f'{models_base_dir}/custom_models/model1.h5')

    model2 = create_model2(panneau_shape, len(panneau_classes))
    model2.load_weights(f'{models_base_dir}/custom_models/model2.h5')
else:
    model1 = None
    model2 = None
