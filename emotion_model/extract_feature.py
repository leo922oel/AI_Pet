import librosa
import soundfile
import glob, os
import numpy as np
from sklearn.model_selection import train_test_split

def extract_feature(file_name, mfcc, chroma, mel):
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

def load_data(config, mfcc=True, chroma=True, mel=True, test_size=0.2):
    x, y = [], []
    for file in glob.glob(config.data_path):
        file_name = os.path.basename(file)
        emotion = config.emotion_labels[file_name.split("-")[2]]
        if emotion not in config.observed_emotions:
            continue
        feature = extract_feature(file, mfcc=mfcc, chroma=chroma, mel=mel)
        x.append(feature)
        y.append(emotion)
    
    return train_test_split(np.array(x), y, test_size=test_size, random_state=40)
        