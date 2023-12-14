import sounddevice as sd
import wavio as wv
import datetime

freq = 44100
duration = 5

print("Recording...")

while True:
    ts = datetime.datetime.now()
    filename = ts.strftime("%Y-%m-%d_%H-%M-%S")

    recording = sd.rec(int(duration * freq), samplerate=freq, channels=1)

    # Record audio for the specified number of seconds
    sd.wait()

    wv.write(f"./recordings/{filename}.wav", recording, freq, sampwidth=2)
