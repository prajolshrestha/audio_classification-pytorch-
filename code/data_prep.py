import torchaudio
from plot_audio import plot_specgram
import os # for operating system related functionality.
import random # for generating random numbers.

wav_path = 'data/set_a' #path to the directory containing the audio files.
wav_filenames = os.listdir(wav_path) #Creates a list of filenames of all files in the directory
random.shuffle(wav_filenames) #Randomly shuffles the order of the filenames in the above list

ALLOWED_CLASSES = ['normal', 'murmur', 'extrahls', 'artifact'] # list
for f in wav_filenames:#Iterates over each filename
    class_type = f.split('_')[0] #Extracts the class type from the filename 
    #by splitting the filename at the underscore character and taking the first element.
    f_index = wav_filenames.index(f) #Gets the index of the current filename
    # if file position is 0-139 then train folder, else test
    target_path = 'train' if f_index < 140 else 'test'
    class_path = f"{target_path}/{class_type}"#path to the directory where the current file will be stored.
    file_path = f"{wav_path}/{f}"# path to the current audio file.
    f_basename = os.path.basename(f)#Gets the base name of the current filename (without the path).
    f_basename_wo_ext = os.path.splitext(f_basename)[0]#Gets the base name of the current filename without the file extension.
    target_file_path = f"{class_path}/{f_basename_wo_ext}.png"#path to the file where the spectrogram of the current audio file will be saved as a png file.
    if (class_type in ALLOWED_CLASSES):
        # create folder if necessary
        if not os.path.exists(class_path):
            os.makedirs(class_path)
        #extract class type from file    
        data_waveform, sr = torchaudio.load(file_path)#Loads the current audio file into 
        #a tensor called "data_waveform" and the sampling rate into a variable called "sr"
        plot_specgram(waveform=data_waveform, sample_rate = sr, file_path=target_file_path)#create spectogram