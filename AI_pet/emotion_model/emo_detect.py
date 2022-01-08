import emotion_model.select_gif as sgif
from emotion_model.predict import predict
from emotion_model.utils.config import parse_config
import emotion_model.models as models
import os


def detect(prev_mood, curr_gif):
    config = parse_config()
    model = models.load(config)
    audio = 'emotion_model/input_data/audio_recording.wav'

    emo = predict(config, audio, model)
    print(emo)

    return emo, sgif.select_gif(emo, prev_mood, curr_gif)
