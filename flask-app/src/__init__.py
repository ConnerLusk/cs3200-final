# Some set up for the application 

from flask import Flask
from flaskext.mysql import MySQL

# create a MySQL object that we will use in other parts of the API
db = MySQL()

def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = 'someCrazyS3cR3T!Key.!'
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = open('/secrets/db_password.txt').readline()
    app.config['MYSQL_DATABASE_HOST'] = 'db'
    app.config['MYSQL_DATABASE_PORT'] = 3306
    app.config['MYSQL_DATABASE_DB'] = 'KLMVGames'

    db.init_app(app)

    from src.submission.submission  import submission
    from src.players.players import players
    from src.gameAttempt.gameAttempt  import gameAttempt
    from src.answers.answers import answers
    from src.clues.clues import clues
    from src.gameTypes.gameTypes import gameType
    from src.games.games import games
    from src.guesses.guesses import guesses

    app.register_blueprint(submission,    url_prefix='/s')
    app.register_blueprint(players, url_prefix= '/pl' )
    app.register_blueprint(gameAttempt,    url_prefix='/ga')
    app.register_blueprint(answers,    url_prefix='/a')
    app.register_blueprint(clues,    url_prefix='/cl')
    app.register_blueprint(gameType,    url_prefix='/gt')
    app.register_blueprint(games,    url_prefix='/g')
    app.register_blueprint(guesses,    url_prefix='/gu')


    return app