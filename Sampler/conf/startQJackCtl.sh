#!/bin/bash

###################################################
#               PTS3 - Sampleur
#  Script de connexion et lancement du programme
#           Mise à jour : 19/03/2021
###################################################

# Connexion de l'appareil MIDI (port de sortie) au client d'écriture (port d'entrée) Midi Through

aconnect 24:MPD218 14:MIDI Through 

# Lancement du programme python 
cd /home/pi/Desktop/2020-2021-INFO2-PTS3-Sampler/src/

python Main.py
