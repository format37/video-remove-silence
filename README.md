# `video-remove-silence`

Tool for removing silence from video files.

## Remove silence

```
./video-remove-silence some_file.mp4
```

## Extract audio

```
python3 extract_audio.py
```

## Convert audio

```
sh convert_wav.sh output.wav out_con.wav
```

## Transcribe audio
Using [vosk](https://github.com/format37/stt/tree/main/vosk_cpu)
```
python3 transcribe.py out_con.wav
```

## Dependencies

- Python 3.5+
- FFmpeg
