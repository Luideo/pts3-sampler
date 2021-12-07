# Fichier : Pad.py
# Classe representant un pad de l'appareil MIDI

# Import et chargement des modules requis
import pygame
from pygame import mixer

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

    # Jouer un son associe au pad
    def play(self, velocite):
        mixer.music.load(self.sound.getPath())
        
        volume = round(float(velocite*100/127)/100, 2)
        
        mixer.Channel(self.channel).set_volume(volume)
        
        if self.isLoop == True:
            mixer.Channel(self.channel).play(mixer.Sound(self.sound.getPath()), loops=-1)
        else:
            mixer.Channel(self.channel).play(mixer.Sound(self.sound.getPath()))

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
    def playQueue(self, velocite):
        if self.isLoop == True:
            mixer.Channel(self.channel).queue(mixer.Sound(self.sound.getPath()), loops=-1)
        else:
            mixer.Channel(self.channel).queue(mixer.Sound(self.sound.getPath()))






        
         


