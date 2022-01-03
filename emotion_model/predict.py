from utils.config import parse_config
from extract_feats.librosa import get_data
import models

def predict(config, audio_path, model):
    feature = get_data(config, audio_path, config.predict_feature_path, train=False)
    result = model.predict(feature)
    emotion = config.observed_emotions[int(result)]
    # print('Recogntion: ', config.observed_emotions[int(result)])
    return emotion
    
if __name__ == '__main__':
    audio_path = 'input_data/*.wav'

    config = parse_config()
    model = models.load(config)
    emo = predict(config, audio_path, model)
    print(emo)