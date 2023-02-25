# Pitch Shifting for Voice Gender Conversion
This Python code provides a simple way to shift the pitch of an audio file to make it sound like a different gender. It uses the Python library pydub to process the audio file and shift the pitch up or down by one octave depending on the specified gender or the dBFS level of the audio file.

## Installation
Before using the code, you must install the following dependencies:
```
python
numpy
pydub
```
You can install the dependencies using the following command:
```
pip install -r requirements.txt
```
## Usage
The code is designed to be run from the command line using the python command. Here is an example command that converts an audio file to a female voice:

```
python Gender_Changer.py --voice_path input.wav --output_path output.wav --gender female
```
The command specifies the path to the input audio file (`input.wav`), the path to the output audio file (`output.wav`), and the desired gender (`female`).

If the gender parameter is not provided, the code will attempt to automatically determine the gender based on the dBFS level of the audio file. If the dBFS level is greater than -20, the code will assume the gender is female. Otherwise, it will assume the gender is male.

```
python Gender_Changer.py --voice_path input.wav --output_path output.wav
```
## How it works
The code defines a function called `shift_pitch_gender` that takes two arguments: `sound` and `gender`. The `sound` argument is an instance of the `AudioSegment` class that represents the input audio file. The `gender` argument is a string that specifies the desired gender of the output audio file. If no gender is specified, the code attempts to automatically determine the gender based on the dBFS level of the input audio file.

The code first checks if the `gender` parameter is empty, and if so, sets it to "male". Otherwise, it computes the dBFS level of the input audio file and sets the gender to "female" if the dBFS level is greater than -20, and "male" otherwise.

The code then calculates the number of semitones to shift the pitch based on the specified or automatically determined gender, and uses the `_spawn` method of the `AudioSegment` class to create a new instance of the `AudioSegment` class with the pitch shifted accordingly. The code also sets the frame rate of the shifted audio to 44100 Hz to ensure compatibility with most audio playback software.

Finally, the code exports the shifted audio to a WAV file using the `export` method of the `AudioSegment` class, with the file name and format specified by the `output_path` and `format` parameters, respectively.


## Limitations
While this code provides a simple way to shift the pitch of an audio file to make it sound like a different gender, it has some limitations:

+ The code relies on the `pydub` library, which may not be compatible with all audio file formats.
+ The code uses a simple heuristic to determine the gender of the input audio file based on its dBFS level, which may not always be accurate.
+ The code shifts the pitch of the entire audio file, which may not always produce the desired effect. For example, the pitch of background music or noise may also be shifted.
+  The code only supports shifting the pitch up or down by one octave, which may not be sufficient for some use cases.
+ The input audio file must be in WAV format. Other audio formats are not currently supported.
+ The code assumes that the input audio file has a single channel. If the audio file has multiple channels, only the first channel will be used.
