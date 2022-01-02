import extract_feats.librosa as lb
from utils.config import parse_config

if __name__ == '__main__':
    config = parse_config()
    lb.get_data(config, config.data_path, config.train_feature_path, train=True)