import numpy as np
from pydub import AudioSegment
import argparse

def shift_pitch_gender(sound, gender):
    if gender == "":
      gender = "male"
    else:
      pitch = sound.dBFS
      gender = "female" if pitch > -20 else "male"
    semitones = 12 if gender == "male" else -12
    shifted_sound = sound._spawn(sound.raw_data, overrides={"frame_rate": int(sound.frame_rate*(2.0**(semitones/12.0)))})
    shifted_sound = shifted_sound.set_frame_rate(44100)
    return shifted_sound

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--voice_path', type=str, default="")
  parser.add_argument('--output_path', type=str, default="shifted.wav")
  parser.add_argument('--gender', type=str, default="")
  args = parser.parse_args()
  sound = AudioSegment.from_file(args.voice_path)
  shifted_sound = shift_pitch_gender(sound, args.gender)
  shifted_sound.export(args.output_path, format="wav")