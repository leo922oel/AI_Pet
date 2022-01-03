import joblib
import librosa
import soundfile
import glob, os
import numpy as np
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split

# from extract_feats.librosa import get_data_path

def features(file_name, mfcc=True, chroma=True, mel=True):
    with soundfile.SoundFile(file_name) as sound_file:
        x = sound_file.read(dtype="float32")
        sample_rate = sound_file.samplerate

        result = np.array([])
        if mfcc:
            sample_mfcc = np.mean(librosa.feature.mfcc(y=x, sr=sample_rate, n_mfcc=40).T, axis=0)
            result = np.hstack((result, sample_mfcc))
        if chroma:
            stft = np.abs(librosa.stft(x))
            sample_chroma = np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T, axis=0)
            result=np.hstack((result, sample_chroma))
        if mel:
            sample_mel = np.mean(librosa.feature.melspectrogram(x, sr=sample_rate).T, axis=0)
            result = np.hstack((result, sample_mel))
    return result

def get_max_min(files):
    min, max = 100, 0

    for file in files:
        sound_file, samplerate = librosa.load(file, sr=None)
        t = sound_file.shape[0] / samplerate
        if t < min: min = t
        if t > max: max = t
    
    return max, min

def load_feature(config, feature_path, train : bool):
    features = pd.DataFrame(data=joblib.load(feature_path), columns=['file_name', 'features', 'emotion'])

    X = list(features['features'])

    if train:
        Y = list(features['emotion'])

        return train_test_split(np.array(X), np.array(Y), test_size=.1, random_state=40)
    else:
        return np.array(X)

def get_data(config, data_path, feature_path, train : bool):
    if train:
        # max, min = get_max_min(files)
        data = []
        # for file in files:
        for file in glob.glob(config.data_path):
            file_name = os.path.basename(file)
            # label = config.emotion_labels[file_name.split("-")[2]]
            label = file_name.split("-")[2]
            # if label not in config.observed_emotions:
                # continue
            feature = features(file)
            data.append([file, feature, int(label)-1])
    else:
        for file in glob.glob(config.data_path):
            feature = features(file)
            data = [[file, feature, -1]]
    
    cols = ['file_name', 'features', 'emotion']
    data_pd = pd.DataFrame(data, columns=cols)
    pickle.dump(data, open(feature_path, 'wb'))

    return load_feature(config, feature_path, train=train)

        