import argparse
import yaml

class Config:
    def __init__(self, *args, **kwargs):#, params: dict={}):
        # for key, val in params.items():
            # if key != 'params' and isinstance(val, dict):
                # self.__dict__[key] = Config(val)
            # else:
                # self.__dict__[key] = val
        self.model = kwargs.get('model', 'cnn1d')
        self.emotion_labels = {
            '01': 'neutral',
            '02': 'calm',
            '03': 'happy',
            '04': 'sad',
            '05': 'angry',
            '06': 'fearful',
            '07': 'disgust',
            '08': 'surprised'
        }
        self.observed_emotions = ['calm', 'happy', 'fearful', 'disgust']
        self.data_path =  "D:\\LeoData\\11010\\machine_learning\\ML_final_project\\AudioEmotion\\Actor_*\\*.wav"

def load_config(file_path : str):
    file = open(file_path, 'r', encoding='utf-8')
    config = yaml.load(file.read(), Loader=yaml.FullLoader)

    return config

def parse_config():
    # parser = argparse.ArgumentParser()
    # parser.add_argument(
        # '--config',
        # type=str,
        # default='configs/config.yaml',
    # )
    # args = parser.parse_args()
    # config_dict = load_config(args.config)
    config = Config()
    return config