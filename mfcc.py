import librosa
y, sr = librosa.load('ANGER 1.wav')
mfcc = librosa.feature.mfcc(y,sr)