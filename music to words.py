import whisper
from whisper.utils import get_writer
import os

# 1. Configuration
# "small" is fast. "medium" is very accurate. "large" is best but slow.
MODEL_SIZE = "medium" 
AUDIO_FILE = r"C:\Users\romaj\Робочий стіл\music.mp3"

print(f"--- Loading Whisper Model: {MODEL_SIZE} ---")
# This will download the model the first time you run it (approx 1.5GB for medium)
model = whisper.load_model(MODEL_SIZE)

print(f"--- Transcribing {AUDIO_FILE}... ---")
# 'word_timestamps=True' is the magic setting. 
# It ensures the AI aligns text to the exact moment words are spoken, not just general vibes.
result = model.transcribe(AUDIO_FILE, word_timestamps=True)

# 2. Output Directory
output_dir = "."

# 3. Generate All Formats
# This automatically creates .srt, .vtt, .txt, .json, and .tsv
print("--- Saving Files ---")

# SRT (Subtitles)
srt_writer = get_writer("srt", output_dir)
srt_writer(result, AUDIO_FILE)

# VTT (Web Video)
vtt_writer = get_writer("vtt", output_dir)
vtt_writer(result, AUDIO_FILE)

# JSON (Raw Data with word-level timestamps)
json_writer = get_writer("json", output_dir)
json_writer(result, AUDIO_FILE)

print(f"Success! Files saved in: {os.getcwd()}")
print("Check specifically for .srt and .json for the timestamps.")