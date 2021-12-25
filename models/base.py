from abc import ABC, abstractmethod
from typing import Union
import numpy as np
from keras.models import Sequential
from sklearn.metrics import accuracy_score
from sklearn.base import BaseEstimator

class BaseModel(ABC):
    def __init__(self,
                 model : Union[Sequential, BaseEstimator],
                 trained : bool=False
    ) -> None:
        self.model = model
        self.trained = trained

    @abstractmethod
    def train(self) -> None:
        pass

    @abstractmethod
    def predict(self, samples : np.ndarray) -> np.ndarray:
        pass

    @abstractmethod
    def predict_proba(self, samples : np.ndarray) -> np.ndarray:
        if not self.trained:
            raise RuntimeError('Trianed model unexist.')
        if hasattr(self, 'reshape_input'):
            samples = self.reshape_input(samples)

        return self.model.predict_proba(samples)[0]

    @abstractmethod
    def save(self, path : str, name : str) -> None:
        pass

    @classmethod
    @abstractmethod
    def load(cls, path : str, name : str):
        pass

    @classmethod
    @abstractmethod
    def make(cls):
        pass

    @classmethod
    @abstractmethod
    def evaluate(self, x_test : np.ndarray, y_test : np.ndarray) -> float:
        predictions = self.predict(x_test)
        accuracy = accuracy_score(y_pred=predictions, y_true=y_test)

        # print('Accuracy: %.3f\n' %accuracy)

        return accuracy
