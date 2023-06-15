import os
from batch_silence_remover import remove_silences
from extract_audio import extract_audio
from batch_convert_audio import convert_audio
from batch_transcribe import transcribation
from summarization import summarize
import time
import datetime


def main():
    time_start = time.time()
    # Iterate files in path 'in'
    for filename in os.listdir('in'):
        if filename.endswith('.md'):
            continue
        
        # Remove silences
        print('#', filename, 'remove_silences')
        remove_silences('in/' + filename, 'out/' + filename)
        
        # Extract audio
        print('#', filename, 'extract_audio')
        extract_audio('out/' + filename, 'out/' + filename + '.wav')
        
        # Convert audio
        print('#', filename, 'convert_audio')
        convert_audio('out/' + filename + '.wav', 'out/' + filename + 'converted.wav')
        
        # Transcribe
        print('#', filename, 'transcribation')
        transcribation('out/' + filename + 'converted.wav', 'out/' + filename + '.txt')
        
        # Summarize
        print('#', filename, 'summarize')
        # Read text from file
        txt_filename = 'out/' + filename + '.txt'
        with open(txt_filename, 'r') as f:
            text = f.read()
        text += '\n\nПожалуйста, подведите итоги встречи.'
        summary = summarize(text)
        # Save summary to file
        summary_filename = 'out/' + filename + '_summary.txt'
        with open(summary_filename, 'w') as f:
            f.write(summary)
    
    time_end = time.time()
    time_passed_formatted = str(datetime.timedelta(seconds=time_end - time_start))
    print('#', 'Done in', time_passed_formatted)


if __name__ == "__main__":
    main()
