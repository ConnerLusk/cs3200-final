from flask import Blueprint, request, jsonify, make_response
import json
from src import db

submission = Blueprint('submission', __name__)

# Get all the submissions by a player
@submission.route('/submission/<playerId>', methods=['GET'])
def get_player_submission(playerId):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    query = f'''
    SELECT GA.attemptId, Submission.submissionNumber, Submission.numIncorrect
    FROM Submission JOIN GameAttempt GA on Submission.attemptId = GA.attemptId
    WHERE playerId = {playerId};
    '''

    # use cursor to query the database for a list of products
    cursor.execute(query)

    #column headers data
    column_headers = [x[0] for x in cursor.description]

    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

# Get all the submissions by a player for a specific game
@submission.route('/submission/<playerId>/<gameId>', methods=['GET'])
def get_player_game_submission(playerId, gameId):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    query = f'''
    SELECT GA.attemptId, Submission.submissionNumber, numIncorrect
    FROM Submission JOIN GameAttempt GA on Submission.attemptId = GA.attemptId
    where playerId = {playerId} AND gameId = {gameId};
    '''

    # use cursor to query the database for a list of products
    cursor.execute(query)

    #column headers data
    column_headers = [x[0] for x in cursor.description]

    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

# # Return a specific submission given a submission number 
@submission.route('/submission/<playerId>/<gameId>/<submissionNumber>', methods=['GET'])
def get_player_game_submission_num(playerId, gameId, submissionNumber):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    query = f'''
    SELECT GA.attemptId, Submission.submissionNumber, numIncorrect
    FROM Submission JOIN GameAttempt GA on Submission.attemptId = GA.attemptId
    WHERE playerId = {playerId} AND gameId = {gameId} AND submissionNumber = {submissionNumber};
    '''
    cursor.execute(query)

    #column headers data
    column_headers = [x[0] for x in cursor.description]


    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

