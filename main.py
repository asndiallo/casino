from libs import lib
from libs import databaseLib

pseudo = input('\t- Je suis Python. Quel est votre pseudo ? \n ')

print(f'\t- Hello {pseudo}, vous avez 10 €, Très bien ! Installez vous SVP à la table de pari.\n\t\t\t Je vous expliquerai le principe du jeu : \n')
print('\t- Att : vous avez le droit à trois essais !\n')
print('\t- Si vous devinez mon nombre dès le premier coup, vous gagnez le double de votre mise !\n')
print('\t- Si vous le devinez au 2è coup, vous gagnez exactement votre mise !\n')
print('\t- Si vous le devinez au 3è coup, vous gagnez la moitiè votre mise !\n ')
print('\t- Si vous ne le devinez pas au 3è coup, vous perdez votre mise et')
print('\tvous avez le droit : ')
print('\t\t- de retenter votre chance avec l\'argent qu\'il vous reste pour reconquérir le level perdu.')
print('\t\t- de quitter le jeu.\n')
print('\t- Dès que vous devinez mon nombre : vous avez le droit de quitter le jeu et de partir avec vos gains OU \n\t\tde continuer le jeu en passant au level supérieur.\n  ')


databaseLib.addPlayer(pseudo, 10)
playerId = databaseLib.getPlayerId(pseudo)
databaseLib.addGame(playerId)
gameId = databaseLib.getGameId(playerId)


def game(level, attempts, maxAttempts, start, stop):
    betted = lib.getBetting()
    toGuess = lib.chooseNumber(start, stop)
    print(toGuess)
    print(
        f'\t- Je viens de penser à un nombre entre 1 et {10*level}. Devinez lequel ?\n')
    guessed = lib.getGuessing(maxAttempts, level)
    guess = lib.validateGuessing(toGuess, guessed)
    print(guess)

    attempts = 1
    while attempts < maxAttempts and guess != True:
        guessed = lib.getGuessing(maxAttempts-attempts, level)
        guess = lib.validateGuessing(toGuess, guessed)
        print(guess)
        attempts += 1

    # TODO: calculate the gain properly
    gain = lib.calculateGain(attempts, guess, betted)

    if guess == True:
        databaseLib.addRound(betted, playerId, level, attempts, gain, pseudo)
        print(
            f'\t- Bingo {pseudo}, vous avez gagné en {attempts} coup(s) et vous avez remporté {gain} € !\n')
        nextStep = lib.pursue()
        if (nextStep == 'O'):
            print(
                f'\tvous avez maintenant {lib.getTotalBalance(gain, betted)} € au total')
            level += 1
            maxAttempts += 2
            lib.pursuing(level, maxAttempts)
            game(level, 3, maxAttempts, 1, level*10)
        elif nextStep == 'N':
            print(
                f'\t- Au revoir ! Vous finissez la partie avec un de {gain} € \n\tvous avez maintenant {lib.getTotalBalance(gain, betted)} € au total.\n ')
            databaseLib.showStats(gameId)
    else:
        databaseLib.addRound(betted, playerId, level, attempts, gain, 0)
        print(
            f'\t- Vous avez perdu ! Mon nombre était {toGuess} ! Il vous reste {10-betted} €\n')
        nextStep = lib.pursue()
        if nextStep == 'O':
            level = 1
            maxAttempts = 3
            lib.pursuing(level, maxAttempts)
            game(level, 3, maxAttempts, 1, level*10)
        elif nextStep == 'N':
            print(f'\t- Au revoir ! Vous finissez la partie avec {gain} €.\n ')
            print(
                f'\tvous avez donc {lib.getTotalBalance(gain, betted)} € au total')
            databaseLib.showStats(gameId)


game(1, 3, 3, 1, 10)
