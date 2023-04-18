from flask import Blueprint, request, request
from utils import get_query, submit_query

submission = Blueprint('submission', __name__)

# Get all the submissions by a player


@submission.route('/submission/<playerId>', methods=['GET'])
def get_player_submission(playerId):
    query = f'''
    SELECT GA.attemptId, Submission.submissionNumber, Submission.numIncorrect
    FROM Submission JOIN GameAttempt GA on Submission.attemptId = GA.attemptId
    WHERE playerId = {playerId};
    '''
    return get_query(query)

# Get all the submissions by a player for a specific game


@submission.route('/submission/<playerId>/<gameId>', methods=['GET'])
def get_player_game_submission(playerId, gameId):
    query = f'''
    SELECT GA.attemptId, Submission.submissionNumber, numIncorrect
    FROM Submission JOIN GameAttempt GA on Submission.attemptId = GA.attemptId
    where playerId = {playerId} AND gameId = {gameId};
    '''
    return get_query(query)

# # Return a specific submission given a submission number


@submission.route('/submission/<playerId>/<gameId>/<submissionNumber>', methods=['GET'])
def get_player_game_submission_num(playerId, gameId, submissionNumber):
    query = f'''
    SELECT GA.attemptId, Submission.submissionNumber, numIncorrect
    FROM Submission JOIN GameAttempt GA on Submission.attemptId = GA.attemptId
    WHERE playerId = {playerId} AND gameId = {gameId} AND submissionNumber = {submissionNumber};
    '''
    return get_query(query)


@submission.route('/submission/<submissionNumber>/<attemptId>', methods=['PUT'])
def put_player_game_submission_num(submissionNumber, attemptId):
    the_data = request.json
    submissionNumber = the_data["submissonNumber"]
    attemptId = the_data["attemptId"]
    numIncorrect = 3

    query = f"UPDATE Submission SET numIncorrect = '{numIncorrect}' WHERE attemptId = {attemptId} and\
            submissionNumber = {submissionNumber};"

    return submit_query(query, "Updated")
