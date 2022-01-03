import sounddevice as sd
from scipy.io.wavfile import write
import shutil

fs = 44100 # Sample rate
seconds = 3 # Duration of recording
myrecording = sd.rec(int(seconds * fs),samplerate=fs,channels=2)
sd.wait() # Wait until recording is finished
write('Neutral_1-28_0001.wav',fs,myrecording) # Save as WAV file

source = r'D:\04\4\output.wav'
destination = r'D:\04\ML_final_project\emotion_model\input_data'
shutil.copy(source, destination)