import os
from typing import Optional
from abc import ABC, abstractmethod
import numpy as np
from keras.models import Sequential, model_from_json
from .base import BaseModel
# from utils import curve

class DNN(BaseModel, ABC):
    def __init__(self, model: Sequential, trained: bool = False) -> None:
        super().__init__(model, trained)
        # print(self.model.summary())
    
    def save(self, path : str, name : str) -> None:
        save_path = os.path.join(path, name + '.h5')
        self.model.save_weights(save_path)

        save_path_json = os.path.join(path, name + '.json')
        with open(save_path_json, "w") as json_file:
            json_file.write(self.model.to_json())
    
    @classmethod
    def load(cls, path : str, name : str):
        model_path_json = os.path.abspath(os.path.join(path, name + '.json'))
        json_file = open(model_path_json, 'r')
        load_model = json_file.read()
        json_file.close()
        model = model_from_json(load_model)

        model_path = os.path.abspath(os.path.join(path, name + '.h5'))
        model.load_weight(model_path)

        return cls(model, True)
    
    def train(self, x_train : np.ndarray, y_train : np.adarray, batch_size : int=10, n_epochs : int=10) -> None:
        x_train = self.reshape_input(x_train)
        history = self.model.fit(x_train, y_train, batch_size=batch_size, epochs=n_epochs, shuffle=True, )

        acc = history.history['acc']
        loss = history.history['loss']
        
        print('Accuracy: %.3f, Loss: %.3f' % (acc, loss))
        self.trained=True