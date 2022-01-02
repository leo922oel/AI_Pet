from extract_feats.librosa import load_feature
# from keras.utils import np_utils
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

from utils.config import parse_config

def train(config):
    x_train, x_test, y_train, y_test = load_feature(config, config.train_feature_path, train=True)
    print(f'feature extracted: {x_train.shape[1]}')

    model = MLPClassifier(alpha=1e-2, batch_size=256, epsilon=1e-8, hidden_layer_sizes=(300,), learning_rate='adaptive', max_iter=500)
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)
    acc = accuracy_score(y_test, y_pred)
    print("acc: ", {acc})
    print(y_pred)

    # if config.model == 'cnn1d':
        # y_train, y_test = np.utils.to_categorical(y_train), np.utils.to_categorical(y_test)
        # model.train(x_train, y_train, x_test, y_test,
                        # batch_size=config.batch_size,
                        # n_epochs=config.epochs)
    # else:
        # model.train(x_train, y_train)
    
    # model.evaluate(x_test, y_test)
    # model.save(config.checkpoint_path, config.checkpoint_name)

if __name__ == '__main__':
    config = parse_config()
    train(config)