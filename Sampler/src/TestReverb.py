from pysndfx import AudioEffectsChain
from pygame import mixer
mixer.init(buffer=16)
mixer.set_num_channels(49)

fx = (
    AudioEffectsChain()
    .reverb()
)

infile = 'reverb.wav'
outfile = 'processed-output.ogg'

fx(infile, outfile)

mixer.music.load(outfile)

mixer.music.set_volume(50)

mixer.music.play()

while 1:
    print("oui")