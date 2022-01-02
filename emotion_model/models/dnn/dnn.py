import os
from typing import Optional
from abc import ABC, abstractmethod
import numpy as np
from keras.models import Sequential, model_from_json
from ..base import BaseModel
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
        model.load_weights(model_path)

        return cls(model, True)
    
    def train(self, x_train : np.ndarray, y_train, x_val : Optional[np.ndarray] = None, y_val = None, batch_size : int=10, n_epochs : int=10) -> None:
        if x_val is None or y_val is None:
            x_val, y_val = x_train, y_train

        x_train, x_val = self.reshape_input(x_train), self.reshape_input(x_val)
        history = self.model.fit(x_train, y_train, batch_size=batch_size, epochs=n_epochs, shuffle=True, validation_data=(x_val, y_val))

        # acc = history.history['accuracy']
        # loss = history.history['loss']

        # val_acc = history.history['val_accuracy']
        # val_loss = history.history['val_loss']
        
        # print('Accuracy: %.3f, Loss: %.3f' % (acc, loss))
        # print('Val Accuracy: %.3f, Val Loss: %.3f' % (val_acc, val_loss))
        self.trained=True
    
    def predict(self, samples : np.ndarray) -> np.ndarray:
        if not self.trained: raise RuntimeError('Trained model unexist.')

        samples = self.reshape_input(samples)
        return np.argmax(self.model.predict(samples), axis=1)
    
    @abstractmethod
    def reshape_input(self):
        pass