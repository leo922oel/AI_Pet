from keras.layers import LSTM as KERAS_LSTM
from keras.layers import Dense, Dropout
from keras.models import Sequential
# from keras.optimizers import Adam
from tensorflow.keras.optimizers import Adam
import numpy as np
from .dnn import DNN

class LSTM(DNN):
    def __init__(self, model: Sequential, trained: bool = False) -> None:
        super(LSTM, self).__init__(model, trained)
    
    @classmethod
    def make(cls,
             input_shape : int,
             rnn_size : int,
             hidden_size : int,
             dropout : float=0.5,
             n_classes : int=3,
             learning_rate : float=0.01):
        model = Sequential()

        model.add(KERAS_LSTM(rnn_size, input_shape=(1, input_shape))) # (time_steps = 1, n_feats)
        model.add(Dropout(dropout))
        model.add(Dense(hidden_size, activation='relu'))

        model.add(Dense(n_classes, activation='softmax'))
        optimzer = Adam(learning_rate=learning_rate)
        model.compile(loss='categorical_crossentropy', optimzer=optimzer, metrics=['accuracy'])

        return cls(model)
    
    def reshape_input(self, data : np.ndarray) -> np.ndarray:
        data = np.reshape(data, (data.shape[0], 1, data.shape[1]))
        return data