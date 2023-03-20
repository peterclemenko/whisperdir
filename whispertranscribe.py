import whisper
import os
import sys
import json

def transcribe_all_audio_files_in_directory(directory_path):
    for file_name in os.listdir(directory_path):
        if file_name.endswith(".mp3") or file_name.endswith(".wav") or file_name.endswith(".m4a"):
            file_path = os.path.join(directory_path, file_name)
            print(f"Transcribing {file_path}...")
            
            print(f"load model")
            
            model = whisper.load_model("base")

            print(f"Transcribe")
            print(file_name)

            result = model.transcribe(file_path)

            output_file_name = os.path.splitext(file_name)[0] + "_output.txt"
    
            with open(output_file_name, 'w') as f:
                
                # convert dictionary into string
                # using json.dumps()
                result2 = json.dumps(result)

                f.write(result2)

            print()

if len(sys.argv) < 2:
    print("Usage: python whispertranscribe.py <input_directory>")
    sys.exit(1)

input_directory = sys.argv[1]

# Example usage
transcribe_all_audio_files_in_directory(input_directory)