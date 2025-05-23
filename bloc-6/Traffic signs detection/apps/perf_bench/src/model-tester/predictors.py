from model_1 import predict as predict_model_1
from model_2 import predict as predict_model_2
from model_3 import predict as predict_model_3
from model_4 import predict as predict_model_4
from model_5 import predict as predict_model_5
from model_6 import predict as predict_model_6

class PredictiveModel():

    def __init__(self, id, name, predict):
        self._name = name
        self._id = id
        self._predict = predict

    def get_name(self):
        return self._name

    def get_id(self):
        return self._id

    def predict(self, image):
        return self._predict(image)


_predictive_models = []

def available_models():
    # global _predictive_models
    return _predictive_models

_predictive_models = [
    PredictiveModel(1, 'yolov8n-001',  predict_model_1),
    PredictiveModel(4, 'yolov8n-best_ncnn_model-001', predict_model_4),
    PredictiveModel(2, 'yolov11n-001', predict_model_2),
    PredictiveModel(3, 'yolov11n-best_ncnn_model-001', predict_model_3),
    PredictiveModel(5, 'yolov11n-retrained-001', predict_model_5),
    PredictiveModel(6, 'home-made-001', predict_model_6),

]
