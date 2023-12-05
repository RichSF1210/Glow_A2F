import sounddevice as sd
import time
# NOTE THIS IS USING SOUNDDEVICE

def play_audio(file_path):
    # Read the audio file
    audio_data, sample_rate = sd.read(file_path, dtype='int16')

    # Play the audio
    sd.play(audio_data, sample_rate)
    sd.wait()

# Stream the generated audio
play_audio(audio_file_path)