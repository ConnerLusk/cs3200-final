from flask import Blueprint, request, current_app, request
from src import db
from utils import submit_query, get_query


gameAttempt = Blueprint('gameAttempt', __name__)

# Get all the game attempts from the database
@gameAttempt.route('/gameAttempt', methods=['GET'])
def get_gameAttempts():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of game attempts
    cursor.execute('SELECT * FROM GameAttempt')
    
    return submit_query(cursor)

# Get all the game attempts from the database
@gameAttempt.route('/gameAttempt/<playerId>', methods=['GET','DELETE'])
def player_id(playerId):
    if request.method == 'GET':
        return get_query(f'SELECT * FROM GameAttempt WHERE playerId = {playerId}')
    elif request.method == 'DELETE':
        return submit_query(f'DELETE FROM GameAttempt WHERE playerId = {playerId}', "Deleted")




@gameAttempt.route('/gameAttempt/<playerId>/<gameId>', methods=['GET','POST','DELETE'])
def get_game_gameAttempts(playerId, gameId):
    if request.method == 'GET':
        return get_query(f'SELECT * FROM GameAttempt WHERE playerId = {playerId} and gameId = {gameId}')
    elif request.method == 'POST':
        the_data = request.json
    
        current_app.logger.info(the_data)

        gameId = the_data["gameId"]
        playerId = the_data["playerID"]
        isInProgress = the_data["isInProgress"]
        time_Elapsed = the_data["timeElapsed"]
        score = the_data["score"]

        query = "INSERT INTO GameAttempt (gameId, playerID, isInProgress, timeElapsed, score) VALUES ("
        query += f"{gameId}, {playerId}, {isInProgress}, {time_Elapsed}, {score})"

        submit_query(query, "Inserted")

    elif request.method == "DELETE":
        return submit_query(f'DELETE * FROM GameAttempt WHERE playerId = {playerId} and gameId = {gameId}', "Deleted")
    