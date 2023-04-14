from flask import Blueprint, request, jsonify, make_response
import json
from src import db
from utils import cursor_to_json


answers = Blueprint('answers', __name__)

# Get all the answers from the database
@answers.route('/answers/<gameId>', methods=['GET'])
def get_all_answers(gameId):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of game attempts
    cursor.execute(f'SELECT * FROM Answers WHERE gameId = {gameId}')
    
    return cursor_to_json(cursor)

# Get all the answers from the database
@answers.route('/answers/<gameId>', methods=['DELETE'])
def delete_game_answers(gameId):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of game attempts
    cursor.execute(f'DELETE * FROM Answers WHERE gameId = {gameId}')
    
    return "Deleted"
    

# Get all the answers from the database
@answers.route('/answers/<gameId>/<ValueRow>/<ValueColumn>', methods=['GET'])
def get_answer(gameId, ValueRow, ValueColumn):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of game attempts
    cursor.execute(f'SELECT * FROM Answers WHERE gameId = {gameId} and ValueRow = {ValueRow} and {ValueColumn}')
    
    return cursor_to_json(cursor)

# Get all the answers from the database
@answers.route('/answers/<gameId>/<ValueRow>/<ValueColumn>', methods=['POST'])
def insert_answer(gameId, gameName, ValueRow, ValueColumn, charValue):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of game attempts
    cursor.execute(f'INSERT INTO GameAttempt VALUES ({gameId}, {gameName}, {ValueRow}, {ValueColumn}, {charValue})')


# Get all the answers from the database
@answers.route('/answers/<gameId>/<ValueRow>/<ValueColumn>', methods=['PUT'])
def update_answer(gameId, gameName, ValueRow, ValueColumn, charValue):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of game attempts
    cursor.execute(f'''
                    UPDATE Answers SET gameId = {gameId} 
                    gameName = {gameName} ValueRow = {ValueRow}
                    ValueColumn = {ValueColumn} charValue = {charValue} 
                    WHERE gameId =  {gameId})
                    ''')
    
@answers.route('/answers/<gameId>/<ValueRow>/<ValueColumn>', methods=['DELETE'])
def delete_answer(gameId, gameName, ValueRow, ValueColumn, charValue):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of game attempts
    cursor.execute(f'DELETE * FROM Answers WHERE gameId = {gameId})')


