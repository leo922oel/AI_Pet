# ML_final_project
ML team19 final project : AI pet

# **Emotion model**
#### Structure
```
├── models/                
│   ├── base.py          // base of all model
│   ├── dnn                // nn model
│   │   ├── dnn.py         // base of nn
│   │   ├── cnn.py         // CNN
│   │   └── lstm.py        // LSTM
│   └── ml.py              // SVM & MLP
│
├── extract_feats/         // extract features
│   └── librosa.py         // extract features by librosa
├── utils/
│   └── config.py          // call parameters by config
├── features/              // save the setting feature file
├── checkpoint/            // save the check point of trained model
├── train.py               // train model
├── predict.py             // prediction
└── preprocess.py          // preprocess the original datak
```

#### Preprocess
New training dataset should preprocess first to set the feature file.

```python
python preprocess.py
```
#### quick train
Use training data to build the model. The name of files follows the format :
```
{*}-{*}-{the emotion label}-{...}.wav
```
```python
python train.py
```
#### quick test
- Currently, The model is the building cnn.
- The path way of the test file can modify in the predict.py : audio_path = "{file path}" 
- each time predicts a data only.
```python
python predict.py
```

# **Dataset**
- [Common Voice](https://commonvoice.mozilla.org/zh-CN/datasets)

- [Surrey Audio-Visual Expressed Emotion (SAVEE)](http://personal.ee.surrey.ac.uk/Personal/P.Jackson/SAVEE/Download.html)

- [MEGA EmoV-DB](https://mega.nz/folder/KBp32apT#gLIgyWf9iQ-yqnWFUFuUHg)


# **Voice Model**
- <https://github.com/Renovamen/Speech-Emotion-Recognition>


# **Output .Gif file**
- <https://www.jianshu.com/p/bd99496598e1>
- <https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/367149/>

- 另種方法
    1. 把gif切成很多張PNG :
    <https://www.cleverpdf.com/zh-tw/gif-to-png>
    2. 把多張PNG拼成gif :
    <https://paste.ofcode.org/8FDwbCPWGG7n23xR32mm8g>
    
        (fps愈大，每張PNG間隔愈短)

# **mood tag**
    Happy
    Sad
    Angry
    Neutral
    Calm
    Fearful
    Disgust
    Surprised