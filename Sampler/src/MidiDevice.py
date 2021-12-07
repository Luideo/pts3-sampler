# Fichier : MidiDevice.py

from abc import abstractmethod
import rtmidi_python as rtmidi

# Classe abstraite representant un appareil MIDI

class MidiDevice:

    # model : Modele de l'appareil MIDI connecte
    # programs : liste de programmes qu'un appareil MIDI possede
    def __init__(self, model):
        self.midi_in = rtmidi.MidiIn()
        self.midi_in.open_port(0)  # ouverture du port MIDI.
        self.model = model
        self.programs = list()

    # Ajouter un programme a l'appareil MIDI
    # program : programme a ajouter
    def addProgram(self, program):
        self.programs.append(program)

    # Supprimer un programme de l'appareil MIDI
    # program : programme a supprimer
    def removeProgram(self, program):
        self.programs.remove(program)

    # Recuperer le modele de l'appareil MIDI
    # Retourne le modele de l'appareil MIDI
    def getModel(self):
        return self.model

    # Modifier le modele de l'appareil MIDI
    # model :  nouveau modele de l'appareil MIDI
    def setModel(self, model):
        self.model = model

    # Recuperer un programme precis du peripherique MIDI
    # number : numero du programme a recuperer
    # Retourne un programme precis du peripherique MIDI
    def getProgram(self, number):
        for program in self.programs:
            if program.getNumber() == number:
                return program

    # Peupler un appareil midi des ses programmes, banques, pads et sons.
    @abstractmethod
    def populate(self):
        pass

    # Mettre en route l'appareil MIDI pour l'utiliser
    @abstractmethod
    def start(self):
        pass