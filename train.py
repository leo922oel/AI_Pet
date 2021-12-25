import os
import numpy as np
from keras.utils import np_utils
import models
import extract_feats.opensmile as of
import extract_feats.librosa as lf
from utils import parse_opt

def train(config) -> None:
    # load preprocessing data
    if(config.feature_method == 'o'):
        x_train, x_test, y_train, y_test = of.load_feature(config, config.train_feature_path_opensmile, train=True)

    elif(config.feature_method == 'l'):
        x_train, x_test, y_train, y_test = lf.load_feature(config, config.train_feature_path_librosa, train=True)

    # x_train, x_test (n_samples, n_feats)
    # y_train, y_test (n_samples)

    model = models.make(config=config, n_feats=x_train.shape[1])

    print('----- start training', config.model, '-----')
    if config.model in ['lstm', 'cnn1d', 'cnn2d']:
        y_train, y_val = np_utils.to_categorical(y_train), np_utils.to_categorical(y_test)
        model.train(
            x_train, y_train,
            x_test, y_val,
            batch_size = config.batch_size,
            n_epochs = config.epochs
        )
    else:
        model.train(x_train, y_train)
    print('----- end training ', config.model, ' -----')

    model.evaluate(x_test, y_test)
    model.save(config.checkpoint_path, config.checkpoint_name)


if __name__ == '__main__':
    config = parse_opt()
    train(config)
