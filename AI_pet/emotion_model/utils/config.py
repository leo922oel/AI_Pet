import argparse
import yaml

class Config:
    def __init__(self, *args, **kwargs):#, params: dict={}):
        # model
        self.model = kwargs.get('model', 'cnn1d')

        # training params
        self.epochs = 1500
        self.batch_size = 32
        self.learning_rate = 0.001

        # model params
        self.n_kernels = 48
        self.kernel_sizes = [5, 5, 5, 5, 5, 5]
        self.dropout = 0.5
        self.hidden_sizes = 256

        # emotion
        self.emotion_labels = {
            '01': 'Neutral',
            '02': 'Calm',
            '03': 'Happy',
            '04': 'Sad',
            '05': 'Angry',
            '06': 'Fearful',
            '07': 'Disgust',
            '08': 'Surprised'
        }
        self.observed_emotions = ['Neutral', 'Calm', 'Happy', 'Sad', 'Angry', 'Fearful', 'Disgust', 'Surprised']

        # path 
        self.data_path =  "emotion_model/training_dataset/Actor_*/*.wav"
        self.feature_path = kwargs.get('feature_path', "features")
        self.train_feature_path = kwargs.get('train_feature_path', 'emotion_model/features/train_feat.p')
        self.predict_feature_path = kwargs.get('predict_feature_path', 'emotion_model/features/test_feat.p')
        self.checkpoint_path = kwargs.get('checkpoint_path', 'emotion_model/checkpoint/')
        self.checkpoint_name = kwargs.get('checkpoint_name', 'best_model_checkpoint')

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