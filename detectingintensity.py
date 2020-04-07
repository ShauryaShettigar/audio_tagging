# from os.path import dirname, join as pjoin
# import scipy.io as sio

# data_dir = pjoin(dirname(sio.__file__), 'tests', 'data')
# wav_fname = pjoin(data_dir, 'ANGER 1.wav')
# samplerate, data = sio.wavfile.read(wav_fname)
# print(f"number of channels = {data.shape[1]}")

# length = data.shape[0] / samplerate
# print(f"length = {length}s")

import soundfile as sf
import pyloudnorm as pyln

data, rate = sf.read("ANGER 2.wav")
meter = pyln.Meter(rate) #
loudness = meter.integrated_loudness(data)
print(loudness)