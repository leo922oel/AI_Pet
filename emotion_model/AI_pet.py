import select_gif as sgif
from predict import predict
from utils.config import parse_config
import models


if __name__ == '__main__':
    audio = 'input_data/*.wav'
    config = parse_config()
    model = models.load(config)
    emo = predict(config, audio, model)
    prev_mood = 'Neutral'
    curr_gif = 0

    print("GIF code: ", sgif.select_gif(emo, prev_mood, curr_gif))
