# Fichier : Pad.py
# Classe representant un pad de l'appareil MIDI

# Import et chargement des modules requis
import pygame
from pygame import mixer
import soundfile as sf
from pysndfx import AudioEffectsChain
class Pad:

    # number : numero du pad
    # sound : son a associer au pad
    def __init__(self, number, sound, isLoop, channel):
        mixer.init(buffer=16)
        mixer.set_num_channels(49)
        self.number = number
        self.sound = sound
        self.isLoop = isLoop
        self.channel = channel

    def makeReverb(self, velocite):

        DelayReverb = velocite / 127

        fx = (
            AudioEffectsChain()
            .reverb()
        )

        infile = self.sound.getPath()
        NewPath = './processed-output.ogg'

        fx(infile, NewPath)

        # Write the audio back as a wav file:

        return NewPath

    # Jouer un son associe au pad
    def play(self, velocite, reverb, velociteReverb):

        if reverb == True:
            Path = self.makeReverb(velociteReverb)

            mixer.music.load(Path)

            volume = round(float(velocite * 100 / 127) / 100, 2)

            mixer.Channel(self.channel).set_volume(volume)

            mixer.Channel(self.channel).play(mixer.music(Path))

        else:
            mixer.music.load(self.sound.getPath())
        
            volume = round(float(velocite*100/127)/100, 2)
        
            mixer.Channel(self.channel).set_volume(volume)

            mixer.Channel(self.channel).play(self.sound.getPath())

    # Arreter un son se jouant en boucle
    def stopLoop(self):
        if self.isLoop == True:
            mixer.Channel(self.channel).stop()

    # Arreter un son en boucle lance
    def isReading(self):
        return mixer.Channel(self.channel).get_busy()

    # Modifier le numero du pad
    # number : nouveau numero a associer
    def setNumber(self, number):
        self.number = number

    # Recuperer le numero du pad
    # Retourne le numero du pad
    def getNumber(self):
        return self.number

    # Modifier le son associe au pad
    # sound : nouveau son a associer
    def setSound(self, sound):
        self.sound = sound

    # Recuperer le son associe au pad
    # Retourne le son associe au pad
    def getSound(self):
        return self.sound
    # Ajoute un son dans une queue





        
         


