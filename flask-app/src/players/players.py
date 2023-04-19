from flask import Blueprint, request, jsonify, make_response
import json
from src import db
from utils import get_query 
from utils import  submit_query


players = Blueprint('players', __name__)

# Get all players from the DB
@players.route('/players', methods=['GET'])
def get_players():
    query = 'SELECT fname, lname FROM Player;'
    return get_query(query)

@players.route('/players', methods=['POST'])
def create_player():

        the_data = request.json

        premium = the_data['isPremium']
        fname = the_data['fName']
        lname = the_data['lName']
        email = the_data['email']
        birthday = the_data['birthday']

        query = 'INSERT into Player (isPremium, fName, lName, email, birthday) VALUES ('
        query += f"{premium}, '{fname}', '{lname}', '{email}', '{birthday}')"

        return submit_query(query, "Inserted")

# Delete, fetch, or update a specific player
@players.route('/players/<playerID>', methods= ['GET','PUT','DELETE'])
def get_player(playerID):

    if request.method == "GET":
        query = 'SELECT * FROM Player where playerID = {0};'.format(playerID)
        return get_query(query)
    
    elif request.method == "PUT":
        the_data = request.json

        premium = the_data['isPremium']
        fname = the_data['fName']
        lname = the_data['lName']
        email = the_data['email']
        birthday = the_data['birthday']

        # generate query
        query = f"UPDATE Player SET isPremium = '{str(premium)}',"
        query += f"fName = '{fname}', lname = '{lname}', email = '{email}', birthday ='{birthday}'"
        query += f"WHERE playerID = {playerID}"
        
        return submit_query(query, "Updated")
  
    elif request.method == "DELETE":

        query = 'Delete FROM Player where playerID = {0};'.format(playerID)
        return submit_query(query, "Deleted")


