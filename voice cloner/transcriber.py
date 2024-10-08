import os
import torch
import torchaudio
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

# Define the path where the .m4a files are located
wav_directory = ""  # Add your wav dir

# Define the output file name
output_file = os.path.join(wav_directory, "list.txt")

# Define the range of .m4a files (1 to 20)
wav_files_range = range(1, 21)

# Initialize the list to store file paths and transcripts
file_and_transcripts = []

# Initialize the wav2vec model and processor
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-large-960h")
processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-large-960h")

# Iterate through the .m4a files
for i in wav_files_range:
    wav_file = os.path.join(wav_directory, f"{i} wav.m4a")

    # Check if the .m4a file exists
    if os.path.exists(wav_file):
        # Recognize the speech in the .m4a file
        try:
            waveform, sample_rate = torchaudio.load(wav_file)
            waveform = waveform.squeeze()  # Squeeze the batch dimension
            resampler = torchaudio.transforms.Resample(
                orig_freq=sample_rate, new_freq=16000)
            waveform = resampler(waveform)
            input_values = processor(
                waveform, return_tensors="pt", sampling_rate=16000).input_values
            logits = model(input_values).logits
            predicted_ids = torch.argmax(logits, dim=-1)
            transcript = processor.decode(predicted_ids[0])
        except FileNotFoundError:
            print(f"File not found: {wav_file}")
            continue

        # Append the desired path format and transcript to the list
        file_and_transcripts.append(
            f"/content/TTS-TT2/wavs/{i} wav.m4a|{transcript}")
    else:
        print(f"File not found: {wav_file}")

# Write the file paths and transcripts to the output file
with open(output_file, "w") as f:
    for line in file_and_transcripts:
        f.write(f"{line}\n")

print(f"File '{output_file}' created successfully.")
