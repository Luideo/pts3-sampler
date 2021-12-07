# Fichier : Sound.py
# Classe representant un fichier son

class Sound:

    # path : chemin relatif du fichier son
    def __init__(self, aPath):
        self.path = aPath

    # Recuperer le chemin relatif du son
    # Retourne le chemin relatif du son
    def getPath(self):
        return self.path

    # Modifier le chemin relatif du fichier son
    def setPath(self, path):
        self.path = path





