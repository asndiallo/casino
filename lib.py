import random


def getBetting():
    try:
        betting = int(input('\t- Le jeu commence, entrez votre mise : ?\n'))

        while betting not in range(1, 11):
            betting = int(input(
                '\t- Le montant saisi n\'est pas valide. Entrer SVP un montant entre 1 et 10 € :  ?\n '))
        return betting
    except ValueError:
        print('\nCe n\'était pas un nombre valide. Veillez recommencer \n')
        getBetting()


def chooseNumber(start, stop):
    return random.randint(start, stop)


def getGuessing():
    try:
        guessing = int(input(
            '\t- Je viens de penser à un nombre entre 1 et 10. Devinez lequel ?\n\t- Alors mon nombre est : ?\n'))
        if guessing not in range(1, 11):
            guessing = int(
                input('\t- Je ne comprends pas ! Entrer SVP un nombre entre 1 et 10 :  ?\n'))
            getGuessing()
        return guessing
    except ValueError:
        print(('\t- Je ne comprends pas ! Entrer SVP un nombre entre 1 et 10 :  ?\n'))
        getGuessing()


def validateGuessing(toGuess, guessed):
    return toGuess == guessed
