# Fichier : Bank.py
# Classe representant une banque de sons de l'appareil MIDI

class Bank:

    # id : identifiant de la banque
    # pads : liste de pads qu'une banque possede
    def __init__(self, id):
        self.id = id
        self.pads = list()

    # Ajouer un pad a la banque
    # pad : pad a ajouter
    def addPad(self, pad):
        self.pads.append(pad)

    # Supprimer un pad de la banque
    # pad : pad a supprimer
    def removePad(self, pad):
        self.pads.remove(pad)

    # Recuperer un pad precis dans la banque
    # number : numero du pad a recuperer
    # Retourne un pad precis dans la banque
    def getPad(self, number):
        for pad in self.pads:
            if pad.getNumber() == number:
                return pad

    # Recuperer l'identifiant de la banque
    # Retourne l'identifiant de la banque
    def getId(self):
        return self.id

    # Modofier l'identifiant de la banque
    # id : nouvel l'identifiant de la banque
    def setId(self, id):
        self.id = id











