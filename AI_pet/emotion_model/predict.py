from emotion_model.utils.config import parse_config
from emotion_model.extract_feats.librosa import get_data
import emotion_model.models as models
import glob
import os

def predict(config, audio_path, model):
    feature = get_data(config, audio_path, config.predict_feature_path, train=False)
    result = model.predict(feature)
    print(result)
    emotion = config.observed_emotions[int(result)]
    # print('Recogntion: ', config.observed_emotions[int(result)])
    return emotion
    
if __name__ == '__main__':
    print("start")
    audio_path = 'input_data/*.wav'
    config = parse_config()
    model = models.load(config)
    # for file in glob.glob(audio_path):
        # file_name = os.path.basename(file)

    emo = predict(config, audio_path, model)
    print(emo)