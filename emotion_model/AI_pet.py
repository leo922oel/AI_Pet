import select_gif as sgif
from predict import predict
from utils.config import parse_config
import models
import os


if __name__ == '__main__':
    config = parse_config()
    model = models.load(config)
    audio = 'input_data/output.wav'
    auto = True
    while auto:
        if int(os.stat(audio).st_mtime) != int(os.stat(audio).st_mtime):
            print("start predict")
            emo = predict(config, audio, model)
            print(emo)
            prev_mood = 'Neutral'
            curr_gif = 0

            print("GIF code: ", sgif.select_gif(emo, prev_mood, curr_gif))
