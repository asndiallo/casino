import pymysql.cursors
import pymysql


def connectToDatabase():
    # Connect to the database
    connection = pymysql.connect(host='mysql-casino-assane.alwaysdata.net',
                                 user='288328',
                                 password='casino-assane-bouna',
                                 db='casino-assane_ipssi')
    return connection


def addPlayer(user_pseudo, Balance):
    connection = connectToDatabase()
    # Creating a cursor object using the cursor() method
    cursor = connection.cursor()

    # Preparing SQL query to INSERT a record into the database.
    sql = f"""INSERT INTO PLAYERS(
    Pseudo, Balance)
    VALUES ('{user_pseudo}', {Balance})"""

    try:
        # Executing the SQL command
        cursor.execute(sql)

        # Commit your changes in the database
        connection.commit()

    except:
        # Rolling back in case of error
        connection.rollback()

    # Closing the connection
    connection.close()


def getPlayerId(user_pseudo):
    connection = connectToDatabase()
    try:
        # Creating a cursor object using the cursor() method
        cursor = connection.cursor()

        query = """SELECT Id FROM PLAYERS WHERE Pseudo=(%s)"""

        cursor.execute(query, user_pseudo)

        playerId = cursor.fetchone()[0]

        return playerId

    except:
        # Rolling back in case of error
        connection.rollback()

    # Closing the connection
    connection.close()


def addGame(playerId):
    connection = connectToDatabase()
    # Creating a cursor object using the cursor() method
    cursor = connection.cursor()

    # Preparing SQL query to INSERT a record into the database.
    sql = f"""INSERT INTO GAME(id_user)
    VALUES ('{playerId}')"""

    try:
        # Executing the SQL command
        cursor.execute(sql)

        # Commit your changes in the database
        connection.commit()

    except:
        # Rolling back in case of error
        connection.rollback()

    # Closing the connection
    connection.close()


def getGameId(user_id):
    connection = connectToDatabase()
    try:
        # Creating a cursor object using the cursor() method
        cursor = connection.cursor()

        query = """SELECT Id FROM GAME WHERE id_user=(%s)"""

        cursor.execute(query, user_id)

        gameId = cursor.fetchone()[0]

        return gameId

    except:
        # Rolling back in case of error
        connection.rollback()

    # Closing the connection
    connection.close()


def addRound(bet, playerId, level, attempt, gain, win):
    connection = connectToDatabase()
    # Creating a cursor object using the cursor() method
    cursor = connection.cursor()

    gameId = getGameId(playerId)
    # Preparing SQL query to INSERT a record into the database.
    sql = """INSERT INTO ROUND(game_id, level, attempt, bet, gain, win)
    VALUES (%s, %s, %s, %s, %s, %s)"""
    value = (gameId, level, attempt, bet, gain, win)
    try:
        # Executing the SQL command
        cursor.execute(sql, value)
        # Commit your changes in the database
        connection.commit()
    except:
        # Rolling back in case of error
        connection.rollback()
    # Closing the connection
    connection.close()


def showStats(gameId):
    connection = connectToDatabase()
    # Creating a cursor object using the cursor() method
    cursor = connection.cursor()

    sql = """SELECT
            MAX(bet) AS MaxBet,     
            MIN(bet) AS MinBet,
            AVG(bet) AS AvgBet,
            MAX(gain) AS MaxGain,
            MIN(gain) AS MinGain,
            AVG(gain) AS AvgGain,
            MAX(attempt) AS MaxAttempt,
            MIN(attempt) AS MinAttempt,
            AVG(attempt) AS AvgAttempt
            FROM ROUND WHERE game_id=(%s)            
    """
    cursor.execute(sql, gameId)

    records = cursor.fetchall()

    # Commit your changes in the database
    connection.commit()
    try:
        # Executing the SQL command
        cursor.execute(sql, gameId)

        records = cursor.fetchall()
        print("\tCi-dessous vos Statisques : \n")
        for row in records:
            print("\tMaxBet", row[0], " €")
            print("\tMinBet", row[1], " €")
            print("\tAvgBet", row[2], " €")
            print("\tMaxGain", row[3], " €")
            print("\tMinGain", row[4], " €")
            print("\tAvgGain", row[5], " €")
            print("\tMaxAttempt", row[6])
            print("\tMinAttempt", row[7])
            print("\tAvgAttempt", row[8])
            print("\n")

    except:
        # Rolling back in case of error
        connection.rollback()
    # Closing the connection
    connection.close()
