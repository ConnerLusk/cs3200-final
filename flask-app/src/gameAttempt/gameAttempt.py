from flask import Blueprint, request, jsonify, make_response
import json
from src import db
from utils import cursor_to_json


gameAttempt = Blueprint('gameAttempt', __name__)

# Get all the game attempts from the database
@gameAttempt.route('/gameAttempt', methods=['GET'])
def get_gameAttempts():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of game attempts
    cursor.execute('SELECT * FROM GameAttempt')
    
    return cursor_to_json(cursor)

# Get all the game attempts from the database
@gameAttempt.route('/gameAttempt/<playerId>', methods=['GET'])
def get_player_gameAttempts(playerId):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of game attempts of the playerId
    cursor.execute(f'SELECT * FROM GameAttempt WHERE playerId = {playerId}')

    return cursor_to_json(cursor)

@gameAttempt.route('/gameAttempt/<playerId>', methods=['DELETE'])
def delete_player_gameAttempts(playerId):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    cursor.execute(f'DELETE * FROM GameAttempt WHERE playerId = {playerId}')

    return "Deleted"

@gameAttempt.route('/gameAttempt/<playerId>/<gameId>', methods=['GET'])
def get_game_gameAttempts(playerId, gameId):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    cursor.execute(f'SELECT * FROM GameAttempt WHERE playerId = {playerId} and gameId = {gameId}')

    return cursor_to_json(cursor)

@gameAttempt.route('/gameAttempt/<playerId>/<gameId>', methods=['POST'])
def post_game_gameAttempts(playerId, gameId, isInProgress, time_Elapsed, score):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    cursor.execute(f'INSERT INTO GameAttempt VALUES ({gameId}, {playerId}, {isInProgress}, {time_Elapsed}, {score})')

    return "Inserted"

@gameAttempt.route('/gameAttempt/<playerId>/<gameId>', methods=['DELETE'])
def delete_game_gameAttempts(playerId, gameId):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    cursor.execute(f'DELETE * FROM GameAttempt WHERE playerId = {playerId} and gameId = {gameId}')

    return "Deleted"