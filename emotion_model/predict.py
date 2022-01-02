from utils import parse_config
from extract_feats.librosa import get_data
from sklearn.neural_network import MLPClassifier

def predict(config, audio_path, model):
    feature = get_data(config, audio_path, config.predict_feature_path, train=False)

    y_pred = model.predict(feature)
    print(y_pred)
    # result = model.predict(feature)
    # result_prob = model.predict_proba(feature)
    # print('Recogntion: ', config.observed_emotions[int(result)])
    # print('Probability: ', result_prob)
    # utils.radar(result_prob, config.class_labels)
    
if __name__ == '__main__':
    audio_path = ''

    config = parse_config()
    # model = models.load(config)
    model = MLPClassifier(alpha=1e-2, batch_size=256, epsilon=1e-8, hidden_layer_sizes=(300,), learning_rate='adaptive', max_iter=500)
    predict(config, audio_path, model)