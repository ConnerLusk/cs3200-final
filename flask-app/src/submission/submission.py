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

# adding calculator for this 
#testing  commits
def calc_num_incorrect(attemptId, submissionNumber):
    count = 0
    rows = [1,2,3,4,5]
    cols = [1,2,3,4,5]
    for x in rows:
        for y in cols:
            try:
                guessVal = get_query(f'Select Guesses.charValue FROM Guesses WHERE submissionNumber = {submissionNumber} AND attemptId = {attemptId} AND valueColumn = {y} and valueRow = {x};')
                ansVal = get_query(f'Select Answers.charValue FROM Answers WHERE submissionNumber = {submissionNumber} AND attemptId = {attemptId} AND valueColumn = {y} and valueRow = {x};')
                if guessVal == ansVal: 
                    count += 1
            except:
                print("bang")
    return 25 - count


@submission.route('/submission/<submissionNumber>/<attemptId>', methods=['PUT'])
def put_player_game_submission_num(submissionNumber, attemptId):
    numIncorrect = calc_num_incorrect(attemptId, submissionNumber)

    query = f"UPDATE Submission SET numIncorrect = '{numIncorrect}' WHERE attemptId = {attemptId} and\
            submissionNumber = {submissionNumber};"

    return submit_query(query, "Updated")


@submission.route('/submission/<submissionNumber>/', methods=['DELETE'])
def delete_game_submission(submissionNumber):

    query = f"DELETE FROM Submission WHERE submissionNumber = {submissionNumber};"
    
    return submit_query(query, "Deleted")