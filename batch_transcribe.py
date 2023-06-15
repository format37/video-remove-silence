import asyncio
import websockets
import wave
import json
import sys


def accept_feature_extractor(phrases, accept):    
    if len(accept)>1 and accept['text'] != '':        
        accept_text = str(accept['text'])                
        accept_start = str(accept['result'][0]['start'])
        accept_end = accept['result'][-1:][0]['end']        
        conf_score = []
        for result_rec in accept['result']:
            # print('#', result_rec['conf'], result_rec['start'], result_rec['end'], result_rec['word'])
            conf_score.append(float(result_rec['conf']))
        conf_mid = str(sum(conf_score)/len(conf_score))
        # print('=== middle confidence:', conf_mid, '\n')
        phrases.append(accept_text)


async def run_test(uri, filename, out_filepath):

    phrases = []

    async with websockets.connect(uri) as websocket:

        wf = wave.open(filename, "rb")        
        await websocket.send('{ "config" : { "sample_rate" : %d } }' % (wf.getframerate()))
        buffer_size = int(wf.getframerate() * 0.2) # 0.2 seconds of audio
        while True:
            data = wf.readframes(buffer_size)

            if len(data) == 0:
                break

            await websocket.send(data)
            accept = json.loads(await websocket.recv())					
            accept_feature_extractor(phrases, accept)

        await websocket.send('{"eof" : 1}')
        accept = json.loads(await websocket.recv())		
        accept_feature_extractor(phrases, accept)

        # print(phrases)
        # Save phrases to text file
        with open(out_filepath, 'w') as f:
            for phrase in phrases:
                f.write("%s\n" % phrase)


def transcribation(filename, out_filepath):
    asyncio.run(run_test('ws://localhost:2800', filename, out_filepath))


def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} input.wav output.txt")
        sys.exit(1)
    filename = sys.argv[1]
    out_filepath = sys.argv[2]
    transcribation(filename, out_filepath)


if __name__ == "__main__":
    main()
