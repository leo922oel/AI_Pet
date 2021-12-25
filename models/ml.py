import os
import pickle
from abc import ABC
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.base import BaseEstimator
from sklearn.externals import joblib
from .base import BaseModel

class ML(BaseModel, ABC):
    def __init__(self, model : BaseEstimator, trained : bool=False) -> None:
        super(ML, self).__init__(model, trained)
    
    def save(self, path: str, name: str) -> None:
        save_path = os.path.abspath(os.path.join(path, name + '.m'))
        pickle.dump(self.model, open(save_path, "wb"))
    
    @classmethod
    def load(cls, path : str, name : str):
        model_path = os.path.abspath(os.path.join(path, name + '.m'))
        model = joblib.load(model_path)

        return cls(model, True)
    
    def train(self, x_train : np.ndarray, y_train : np.ndarray) -> None:
        self.model.fit(x_train, y_train)
        self.trained = True
    
    def predict(self, samples: np.ndarray) -> np.ndarray:
        if not self.trained: raise RuntimeError("Trained model unexist.")
        return self.model.predict(samples)
    
class SVM(ML):
    def __init__(self, model: BaseEstimator, trianed: bool = False) -> None:
        super(SVM, self).__init__(model, trianed)
    
    @classmethod
    def make(cls, params):
        model = SVC(**params)
        return cls(model)

class MLP(ML):
    def __init__(self, model: BaseEstimator, trained: bool = False) -> None:
        super(MLP, self).__init__(model, trained)
    
    @classmethod
    def make(cls, params):
        model = MLPClassifier(**params)
        return cls(model)