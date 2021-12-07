# Fichier : Program.py
# Classe representant un programme de l'appareil MIDI

from Bank import Bank

class Program:

    # number : numero du programme
    # banks : liste de banques qu'un programme peut contenir
    def __init__(self, number):
        self.number = number
        self.banks = list()

    # Ajouter une banque au programme
    # bank : banque a ajouter
    def addBank(self, bank):
        self.banks.append(bank)

    # Supprimer une banque du programme
    # bank : banque a supprimer
    def removeBank(self, bank):
        self.banks.remove(bank)

    # Recuperer une banque precise du programme
    # id : identifiant de la banque a recuperer
    # Retourne la banque demandee
    def getBank(self, id):
        for bank in self.banks:
            if bank.getId() == id:
                return bank

    # Recuperer le numero du programme
    # Retourne le numero du programme
    def getNumber(self):
        return self.number

    # Modifier le numero du programme
    # number : nouveau numero du programme
    def setNumber(self, number):
        self.number = number












