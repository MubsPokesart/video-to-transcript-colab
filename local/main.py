import os
import time
import whisper

dirname = os.path.dirname(__file__)

SOURCE_DIR = os.path.join(dirname, "videos")
OUTPUT_DIR = os.path.join(dirname, "transcripts")
SUPPORTED_EXTENSIONS = ('.mp4', '.mov', '.m4a', '.mp3', '.wav', '.flac') # File extensions to look for

# Which Whisper model to use.
# Options: "tiny", "base", "small", "medium", "large"
# ".en" models (e.g., "base.en") are faster if you know all audio is English.
def load_whisper_model(model_name="base"):
    try:
        print(f"Loading Whisper model '{model_name}'... (This may take a moment)")
        model = whisper.load_model(model_name)
        print("Model loaded successfully.")
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        print("Please ensure you have a GPU runtime (Runtime > Change runtime type > GPU)")
        return None

def run_transcription(model, video_path, output_path):
    try:
        result = model.transcribe(video_path, verbose=True)
        transcript_text = result["text"]
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(transcript_text)

        return True
    
    except Exception as e:
        print(f"ERROR processing '{video_path}': {e}\n")
        return False


def main():
    # 1. Create the output directory if it doesn't exist
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"Transcripts will be saved to: {OUTPUT_DIR}")

    files_skipped = 0
    files_processed = 0

    # 2. Load the Whisper model
    model = load_whisper_model("base")

    if model is None:
        print("Failed to load the Whisper model. Exiting.")
        return
    
    # 3. Process each video file in the source directory
    for root, dirs, files in os.walk(SOURCE_DIR):
        for file in files:
            if file.lower().endswith(SUPPORTED_EXTENSIONS):
                video_path = os.path.join(root, file)
                base_filename = os.path.splitext(file)[0]
                transcript_filename = f"{base_filename}.txt"
                transcript_path = os.path.join(OUTPUT_DIR, transcript_filename)
                if os.path.exists(transcript_path):
                    print(f"--- Skipping '{file}', transcript already exists. ---")
                    files_skipped += 1
                    continue
                print(f"--- Transcribing '{file}'... ---")
                if run_transcription(model, video_path, transcript_path):
                    files_processed += 1
                    print(f"--- Finished '{file}'. Saved to '{transcript_path}' ---")
                else:
                    files_skipped += 1

if __name__ == "__main__":
    main()