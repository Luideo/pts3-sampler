# Fichier : Pad.py
# Classe representant un pad de l'appareil MIDI

# Import et chargement des modules requis
import pygame
from pygame import mixer
import soundfile as sf
from pedalboard import Pedalboard, Chorus, Reverb, Delay
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
        audio, sample_rate = sf.read(self.sound.getPath())

        # Make a Pedalboard object, containing multiple plugins:
        board = Pedalboard([Chorus(), Reverb(room_size=DelayReverb)])

        # Run the audio through this pedalboard!
        effected = board(audio, sample_rate)

        NewPath = './processed-output.wav'
        # Write the audio back as a wav file:
        sf.write(NewPath, effected, sample_rate)

        return NewPath

    # Jouer un son associe au pad
    def play(self, velocite, reverb, velociteReverb):

        Path = self.sound.getPath()

        if reverb == True:
            Path = self.makeReverb(velociteReverb)

        mixer.music.load(Path)
        
        volume = round(float(velocite*100/127)/100, 2)
        
        mixer.Channel(self.channel).set_volume(volume)

        mixer.Channel(self.channel).play(Path)

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





        
         


