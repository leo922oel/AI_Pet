from keras.layers import Dense, Dropout, Flatten, Conv1D, Activation,\
    BatchNormalization, MaxPooling1D
from keras.models import Sequential
# from keras.optimizers import Adam
from tensorflow.keras.optimizers import Adam, SGD
import numpy as np
from .dnn import DNN

class CNN1D(DNN):
    def __init__(self, model: Sequential, trained: bool = False) -> None:
        super(CNN1D, self).__init__(model, trained)
    
    @classmethod
    def make(cls,
             input_shape : int,
             n_kernels : int,
             kernel_sizes : int,
             hidden_size : int,
             dropout : float=0.5,
             n_classes : int=3,
             learning_rate : float=0.01):
        model = Sequential()
        # for size in kernel_sizes:
            # model.add(Conv1D(filters=n_kernels, kernel_size=size, padding='same', input_shape=(input_shape, 1)))
            # model.add(BatchNormalization(axis=-1))
            # model.add(Activation('relu'))
            # model.add(Dropout(dropout))
        
        # model.add(Flatten())
        # model.add(Dense(hidden_size))
        # model.add(BatchNormalization(axis=-1))
        # model.add(Activation('relu'))
        # model.add(Dropout(dropout))

        model.add(Conv1D(128, kernel_size=5, padding='same', input_shape=(input_shape, 1)))
        model.add(Activation('relu'))
        model.add(Conv1D(128, kernel_size=5, padding='same',))
        model.add(Activation('relu'))
        model.add(Dropout(0.1))
        model.add(MaxPooling1D(8))
        model.add(Conv1D(128, kernel_size=5, padding='same',))
        model.add(Activation('relu'))
        model.add(Conv1D(128, kernel_size=5, padding='same',))
        model.add(Activation('relu'))
        model.add(Conv1D(128, kernel_size=5, padding='same',))
        model.add(Activation('relu'))
        model.add(Dropout(0.2))
        model.add(Conv1D(128, kernel_size=5, padding='same',))
        model.add(Activation('relu'))
        model.add(Flatten())

        model.add(Dense(n_classes, activation='softmax'))
        optimizer = SGD(learning_rate=learning_rate)
        model.compile(loss='sparse_categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])

        return cls(model)

    def reshape_input(self, data : np.ndarray) -> np.ndarray:
        data = np.reshape(data, (data.shape[0], data.shape[1], 1))
        return data