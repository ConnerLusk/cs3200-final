from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db
from utils import cursor_to_json


answers = Blueprint('answers', __name__)


@answers.route('/answers/<gameId>', methods=['GET'])
def get_all_answers(gameId):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to get all answers from the database
    cursor.execute(f'SELECT * FROM Answers WHERE gameId = {gameId}')
    
    return cursor_to_json(cursor)


@answers.route('/answers/<gameId>', methods=['DELETE'])
def delete_game_answers(gameId):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to delete all game answers
    cursor.execute(f'DELETE * FROM Answers WHERE gameId = {gameId}')
    
    return "Deleted"
    


@answers.route('/answers/<gameId>/<ValueRow>/<ValueColumn>', methods=['GET'])
def get_answer(gameId, ValueRow, ValueColumn):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for an answer
    cursor.execute(f'SELECT * FROM Answers WHERE gameId = {gameId} and ValueRow = {ValueRow} and {ValueColumn}')
    
    return cursor_to_json(cursor)


@answers.route('/answers/<gameId>/<ValueRow>/<ValueColumn>', methods=['POST'])
def insert_answer(gameId, ValueRow, ValueColumn):

    the_data = request.json
    
    current_app.logger.info(the_data)

    gameId = the_data["gameId"]
    gameName = the_data["gameName"]
    ValueRow = the_data["valueRow"]
    ValueColumn = the_data["valueColumn"]
    charValue = the_data["charValue"]

    query = "INSERT INTO Answers (gameId, gameName, ValueRow, ValueColumn, charValue) VALUES ("
    query += f"{gameId}, '{gameName}', {ValueRow}, {ValueColumn}, '{charValue}')"
    
    # get a cursor object from the database
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return "Inserted"

@answers.route('/answers/<gameId>/<ValueRow>/<ValueColumn>', methods=['PUT'])
def update_answer(gameId, ValueRow, ValueColumn):
    the_data = request.json
    
    current_app.logger.info(the_data)

    gameId = the_data["gameId"]
    gameName = the_data["gameName"]
    ValueRow = the_data["valueRow"]
    ValueColumn = the_data["valueColumn"]
    charValue = the_data["charValue"]


    # use cursor to update answers
    query = f"UPDATE Answers SET gameName = '{gameName}'"
    query += f", charValue = '{charValue}'"
    query += f"WHERE gameId = {gameId} and valueRow = {ValueRow} and valueColumn = {ValueColumn}"

    
    # get a cursor object from the database
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return "Updated"
    
@answers.route('/answers/<gameId>/<ValueRow>/<ValueColumn>', methods=['DELETE'])
def delete_answer(gameId, gameName, ValueRow, ValueColumn, charValue):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to delete an answer
    cursor.execute(f'DELETE * FROM Answers WHERE gameId = {gameId})')

    return "Deleted"
