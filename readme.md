# Audio Recording and Transcription in real-time

This repository contains two Python scripts that work together to record audio and then transcribe it using the Whisper model. 
The system is designed for continuous recording and transcription, and is robust for pauses that might occur like in any doctor-patient conversation

## Components

The system comprises two main scripts:

1. **recorder.py**: Handles the audio recording. Records audio in 5-second chunks and saves each chunk as a WAV file with a timestamp.
2. **transcriber.py**: Processes the recorded audio files for transcription. Uses the Whisper model to transcribe the audio to text, which is then saved to a text file.

## Prerequisites

Before running these scripts, ensure you have the following dependencies installed:

- Python 3
- sounddevice (`pip install sounddevice`)
- wavio (`pip install wavio`)
- whisper (`pip install whisper`)
- glob

## Usage

### Audio Recording

To start recording, run the `recorder.py` script. This script will continuously record audio in 5-second segments. Each segment is saved in the `./recordings` directory with a filename based on the timestamp of the recording.

### Audio Transcription

To transcribe the recorded audio, run the transcriber.py script. This script checks for new recordings in the ./recordings directory, transcribes them using the Whisper model, and appends the transcribed text to a file located at C:/users/simon/Desktop/AS_live_transcription/transcript.txt.

### NOTES

The original idea was to use Faster Whisper, since it's as fast but more precise, and performs better ad Diarization. However, as I have already told Daniel earlier on, Colab kept on crushing when uploading (and sometimes when reading) the .wav files. That's why I chose to use as a solution Whisper since it's usable on CPU without the need of quantization.
