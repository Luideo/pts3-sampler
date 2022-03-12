#!/bin/bash

###############################################
#               PTS3 - Sampleur
#  Script de configuration de l'environnement
#           Mise à jour : 06/04/2021
###############################################

samplerLocation=$(pwd)

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

echo $'#Demarrage de la redirection de canaux du pilote audio + demarrage script Python sampleur\ncd' $samplerLocation$'/conf\n'$samplerLocation$'/conf/startQJackCtl.sh' >> /home/pi/.bashrc

# ------ Modification du mode HDMI dans le fichier de configuration de démarrage ------#
echo "---------------------------------------------"
echo "Modification du mode HDMI au démarrage de Raspbian "
echo "---------------------------------------------"

echo $'#Passage en mode composite du HDMI au demarrage de Raspbian pour garder les memes id de peripheriques audio - AKAI MPD218\nhdmi_ignore_hotplug=1' >> /boot/config.txt

echo "---------------------------------------------"
echo "Installation terminée "
echo "Redémarrage nécessaire. Le systeme devrait redémarrer dans 5 secondes. "
echo "Si le système ne redémarre pas, redémarrez-le manuellement. "
echo "---------------------------------------------"

# ------ Redémarrage final ------#
sleep 5;
reboot;
