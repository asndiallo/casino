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


def getGuessing(remainingAttempts, level):
    try:
        guessing = int(input(
            f'\t- Je viens de penser à un nombre entre 1 et 10. Devinez lequel ?\n\t Il vous reste {remainingAttempts} essai(s) !\n'))
        if guessing not in range(1, (10*level + 1)):
            guessing = int(
                input(f'\t- Je ne comprends pas ! Entrer SVP un nombre entre 1 et {10*level} :  ?\n'))
            getGuessing()
        return guessing
    except ValueError:
        print(
            (f'\t- Je ne comprends pas ! Entrer SVP un nombre entre 1 et {10*level} :  ?\n'))
        getGuessing()


def validateGuessing(toGuess, guessed):
    if guessed > toGuess:
        return '\t- Votre nombre est trop grand !\n'
    elif guessed < toGuess:
        return '\t- Votre nbre est trop petit !\n'
    else:
        return guessed == toGuess


def pursue():
    return input('\t- Souhaitez-vous continuer la partie (O/N) ?\n').upper()
