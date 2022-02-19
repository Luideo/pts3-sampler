from pysndfx import AudioEffectsChain

fx = (
    AudioEffectsChain()
    .reverb()
)

infile = 'reverb.wav'
outfile = 'processed-output.ogg'

fx(infile, outfile)
