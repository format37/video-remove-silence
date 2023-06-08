#!/bin/bash

# Check if correct number of arguments are passed
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 input.wav output.wav"
    exit 1
fi

input=$1
output=$2

# Convert the audio file
ffmpeg -i "$input" -ac 1 -ar 16000 -ab 256k "$output"
