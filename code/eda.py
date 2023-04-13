import torchaudio
from plot_audio import plot_specgram, plot_waveform
import seaborn as sns
import matplotlib.pyplot as plt

torchaudio.info

#data
wav_file = 'data/set_a/extrahls__201101070953.wav'
data_waveform, sr = torchaudio.load(wav_file)
data_waveform.size()

# plot waveform
plot_waveform(data_waveform, sample_rate = sr)

# calculate spectrogram
spectogram = torchaudio.transforms.Spectrogram()(data_waveform)
spectogram.size()

#plot spectogram
plot_specgram(waveform = data_waveform,sample_rate= sr)