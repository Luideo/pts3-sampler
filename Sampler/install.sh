#!/bin/bash

###############################################
#               PTS3 - Sampleur
#  Script de configuration de l'environnement
#           Mise à jour : 06/04/2021
###############################################

echo "-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/"
echo "     Préparation de l'environnement     "
echo "-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/"

# -------------- build-essential --------------#
echo "----------------------------------------"
echo " Installation du paquet build-essential "
echo "----------------------------------------"

sudo apt-get install -y build-essential

# -------------- python-dev --------------#
echo "----------------------------------------"
echo "   Installation du paquet python-dev    "
echo "----------------------------------------"

sudo apt-get install -y python-dev

# -------------- libasound2 --------------#
echo "----------------------------------------"
echo "   Installation du paquet libasound2    "
echo "----------------------------------------"

sudo apt-get install -y libasound2-dev 

# -------------- libjack-jackd2-dev --------------#
echo "------------------------------------------"
echo "Installation du paquet libjack-jackd2-dev "
echo "------------------------------------------"

sudo apt-get install -y libjack-jackd2-dev

# -------------- QJackCtl --------------#
echo "------------------------------------------"
echo "Installation du paquet QJackCtl "
echo "------------------------------------------"

sudo apt-get install -y qjackctl

# -------------- Dépendances python --------------#
echo "---------------------------------------------"
echo "Installation des dépendances python requises "
echo "1- rtmidi-python"
echo "2- pygame"
echo "---------------------------------------------"

pip install -r requirements.txt

# ------ Automatiser la connexion de l'appareil midi ainsi que le programme ------#
echo "---------------------------------------------"
echo "Automatiser le la connexion de l'appareil MIDI "
echo "Automatiser le lancement du programme "
echo "---------------------------------------------"

sudo su
echo "@lxterminal --command=\"\`home/pi/Desktop/2020-2021-INFO2-PTS3-Sampler/conf/startQJackCtl.sh\`\"" >> /etc/xdg/lxsession/LXDE-pi/autostart

echo "---------------------------------------------"
echo "Installation terminée "
echo "---------------------------------------------"
