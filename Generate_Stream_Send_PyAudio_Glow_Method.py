import numpy as np
import requests
import io
import pyaudio


# Step 1: Simulate Glow TTS (Generate synthetic audio)
def simulate_glow_tts(text):
    # Replace this with your actual Glow TTS implementation
    # This is a simple example generating a sinusoidal wave for demonstration
    duration = 5  # seconds
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    audio_data = 0.5 * np.sin(2 * np.pi * 440 * t)
    return audio_data, sample_rate


# Step 2: Stream the generated .wav file using PyAudio
def stream_audio(audio_data, sample_rate):
    p = pyaudio.PyAudio()

    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=sample_rate,
                    output=True)

    # Play the audio
    stream.write((audio_data * 32767).astype(np.int16).tobytes())

    # Close the stream and PyAudio
    stream.stop_stream()
    stream.close()
    p.terminate()


# Step 3: Simulate sending audio to Audio2face API
def simulate_audio2face_api(audio_data, sample_rate):
    # Simulated Audio2face API endpoint
    audio2face_api_endpoint = "https://audio2face-simulation.example.com"

    # Prepare headers
    headers = {
        "Content-Type": "audio/wav",
    }

    # Convert audio data to bytes
    audio_bytes = io.BytesIO()
    np.savetxt(audio_bytes, audio_data)

    # Simulate sending audio to Audio2face API
    response = requests.post(audio2face_api_endpoint, headers=headers, data=audio_bytes.getvalue())

    # Process the response (handle errors, extract animation data, etc.)
    if response.status_code == 200:
        animation_data = response.json()
        print("Animation data:", animation_data)
    else:
        print(f"Error: {response.status_code}, {response.text}")


# Step 4: Main script
if __name__ == "__main__":
    # Step 1: Generate synthetic audio using Glow TTS
    text_to_generate = "Hello, this is a test."
    audio_data, sample_rate = simulate_glow_tts(text_to_generate)

    # Step 2: Stream the generated audio using PyAudio
    stream_audio(audio_data, sample_rate)

    # Step 3: Send audio to simulated Audio2face API
    simulate_audio2face_api(audio_data, sample_rate)
