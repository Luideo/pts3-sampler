# Fichier : Main.py
# Fichier d'execution principale

from AkaiMPD218 import AkaiMPD218

def main():

    akai = AkaiMPD218(model="MPD218")
    akai.populate()
    akai.start()


if __name__ == '__main__':
    main()
