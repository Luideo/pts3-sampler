#!/usr/bin/python3.4

# Fichier : AkaiMPD218.py

# Import et chargement des modules requis
from MidiDevice import MidiDevice
from Sound import Sound
from Pad import Pad
from Program import Program
from Bank import Bank

# Classe representant un appreil MIDI de marque Akai
# Classe derivee de MidiDevice
class AkaiMPD218(MidiDevice):

    # Peupler l'appareil AKAI de ses programmes, banques, pads et sons.
    def populate(self):
        if(self.model == "MPD218"):

            for i in range(16):
                program = Program(i)
                self.addProgram(program)
                for j in range(3):
                    bank = Bank(chr(65+j))
                    program.addBank(bank)

            for j in range(16):
                for i in range(48):
                    if i <= 15:
                        sound = Sound("./sounds/Program" + str(j) + "/BankA/pad" + str(i) + ".wav")
                        pad = Pad(i, sound, False, i+1)
                        if i>= 8 and i<= 15:
                            pad.isLoop = True
                            pad.channel = 0;
                        self.getProgram(j).getBank('A').addPad(pad)
                    elif i > 15 and i <= 31:
                        sound = Sound("./sounds/Program" + str(j) + "/BankB/pad" + str(i) + ".wav")
                        pad = Pad(i, sound, False, i+1)
                        if i>= 24 and i<= 31:
                            pad.isLoop = True
                            pad.channel = 0;
                        self.getProgram(j).getBank('B').addPad(pad)
                    elif i > 31 and i <= 47:
                        sound = Sound("./sounds/Program" + str(j) + "/BankC/pad" + str(i) + ".wav")
                        pad = Pad(i, sound, False, i+1)
                        self.getProgram(j).getBank('C').addPad(pad)




    # Mettre en route l'appareil AKAI MPD218 : messages MIDI, MIDI Channel, velocite, sons, boucles
    def start(self):

        while True:
            message, delta_time = self.midi_in.get_message()

            if message:
                canal = message[0]
                padTouch = message[1]
                velocite = message[2]
                print("canal {} - pad {} - velocite {}".format(canal, padTouch, velocite))
                # 128 a 144 respectivement 1 a 16 MIDI Channel
                for i in range(144, 160):
                    if canal == i:
                        program = self.getProgram(i - 143)
                        if padTouch <= 15:
                            if program.getBank('A').getPad(padTouch).isLoop == True and program.getBank('A').getPad(padTouch).isReading() == True:
                                print("Le pad : {} est lancé alors qu'il y'a un son",padTouch)
                                # program.getBank('A').getPad(padTouch).playQueue(velocite)
                            else:
                                program.getBank('A').getPad(padTouch).play(velocite)
                                print(program.getBank('A').getPad(padTouch).channel)
                        elif padTouch > 15 and padTouch <= 31:
                            if program.getBank('B').getPad(padTouch).isLoop == True and program.getBank('B').getPad(padTouch).isReading() == True:
                                program.getBank('B').getPad(padTouch).playQueue(velocite)
                            else:
                                program.getBank('B').getPad(padTouch).play(velocite)
                                print(program.getBank('B').getPad(padTouch).channel)
                        elif padTouch > 31 and padTouch <= 47:
                            if program.getBank('C').getPad(padTouch).isLoop == True and program.getBank('C').getPad(padTouch).isReading() == True:
                                program.getBank('C').getPad(padTouch).playQueue(velocite)
                            else:
                                program.getBank('C').getPad(padTouch).play(velocite)
                                print(program.getBank('C').getPad(padTouch).channel)




