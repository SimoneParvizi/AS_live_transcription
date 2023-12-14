#%%
import glob
import whisper
import time

#%%
model = whisper.load_model("base")

# Directory where the recordings are stored
recordings_dir = r'C:/users/simon/Desktop/AS_live_transcription/recordings/*.wav'
transcript_file = r'C:/users/simon/Desktop/AS_live_transcription/transcript.txt'

processed_files = set()

while True:
    
    # Retrieve the list of .wav files
    files = glob.glob(recordings_dir)

    # Process files that haven't been processed yet
    for file in files:
        if file not in processed_files:
            
            # Load the audio file
            audio = whisper.load_audio(file)
            audio = whisper.pad_or_trim(audio)
            mel = whisper.log_mel_spectrogram(audio).to(model.device)

            # Options
            options = whisper.DecodingOptions(language='en', fp16=False)

            # Decoding
            result = whisper.decode(model, mel, options)

            # Avoiding interpretation of silence
            if result.no_speech_prob < 0.5:
                print(result.text)

                # Append text to the transcript file
                with open(transcript_file, 'a', encoding='utf-8') as f:
                    f.write(result.text + '\n')

                # Mark file as processed
                processed_files.add(file)

    # Wait for a short period before checking for new files again
    time.sleep(1)

#%%