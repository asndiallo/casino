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

        playerId = cursor.lastrowid

        # Commit your changes in the database
        connection.commit()

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

        gameId = cursor.lastrowid

        # Commit your changes in the database
        connection.commit()

        return gameId

    except:
        # Rolling back in case of error
        connection.rollback()

    # Closing the connection
    connection.close()


def addRound(game, level, attempt, gain, win):
    connection = connectToDatabase()
    # Creating a cursor object using the cursor() method
    cursor = connection.cursor()

    # Preparing SQL query to INSERT a record into the database.
    sql = f"""INSERT INTO ROUND(game_id, level, attempt, gain, win)
    VALUES ('{game}, {level}, {attempt}, {gain}, {win}')"""

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
