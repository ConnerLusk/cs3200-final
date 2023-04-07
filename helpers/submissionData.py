MAX_NUMBER_ATTEMPTS = 15
NUMBER_USERS = 10
import random
import math

puzzles = [
    ["*stem","*trip","dough","inch","meet"],
    ["*frog","*rice","model","idea","corn"],
    ["**boo","*rich","conch","vogue","story"],
    ["*dark","melee","icing","cake","slew"]
]
num_puzzles = len(puzzles)
querys = []
querys.append("USE KLMVGames;\n")
gameAttempts = []
for i in range(1,NUMBER_USERS+1):
    for j in range(1,random.randint(1,MAX_NUMBER_ATTEMPTS)):
        gameId = random.randint(1,4)
        timeTaken = random.randint(7,200)
        score = random.randint(1,100)
        querys.append(f"INSERT INTO GameAttempt (gameId, playerID, isInProgress, timeElapsed, score) VALUES ({gameId}, {i}, true, {timeTaken}, {score});\n")
        gameAttempts.append((gameId,i,True,timeTaken,score))

submissions = []
for i, attempt in enumerate(gameAttempts):
    attemptId = i + 1
    k = random.randint(1,3)
    for j in range(1,k+1):
        if j == k:
            querys.append(f"INSERT INTO Submission (submissionNumber, attemptId, numIncorrect) VALUES ({j}, {attemptId}, 0);\n")
            submissions.append((j,attemptId,0))
        else:
            numWrong = math.floor(random.randint(1,10))
            if numWrong % 2 == 1:
                numWrong -= 1
            querys.append(f"INSERT INTO Submission (submissionNumber, attemptId, numIncorrect) VALUES ({j}, {attemptId}, {numWrong});\n")
            submissions.append((j,attemptId,numWrong))

for i, submission in enumerate(submissions):
    submission_number = submission[0]
    attempt_id = submission[1]
    number_incorrect = submission[2]
    attempt = gameAttempts[attempt_id-1]
    puzzle = puzzles[attempt[0]-1]
    if number_incorrect == 0:
        for i, row in enumerate(puzzle):
            for j, char in enumerate(row):
                if char != '*':
                    querys.append(f"INSERT INTO Guesses (submissionNumber, attemptId, valueRow, valueColumn, charValue) VALUES ({submission_number}, {attempt_id}, {i}, {j}, '{char}');\n")
    else:
        correct = 10 - number_incorrect
        s = ""
        for i, row in enumerate(puzzle):
            for j, char in enumerate(row):
                if char == '*':
                    continue
                if correct <= 0 and i == 0 and j == 4:
                    querys.append(f"INSERT INTO Guesses (submissionNumber, attemptId, valueRow, valueColumn, charValue) VALUES ({submission_number}, {attempt_id}, {i}, {j}, 'x');\n")
                elif correct <= 2 and i == 1 and j == 3:
                    querys.append(f"INSERT INTO Guesses (submissionNumber, attemptId, valueRow, valueColumn, charValue) VALUES ({submission_number}, {attempt_id}, {i}, {j}, 'x');\n")
                elif correct <= 4 and i == 4 and j == 2:
                    querys.append(f"INSERT INTO Guesses (submissionNumber, attemptId, valueRow, valueColumn, charValue) VALUES ({submission_number}, {attempt_id}, {i}, {j}, 'x');\n")
                elif correct <= 6 and i == 3 and j == 1:
                    querys.append(f"INSERT INTO Guesses (submissionNumber, attemptId, valueRow, valueColumn, charValue) VALUES ({submission_number}, {attempt_id}, {i}, {j}, 'x');\n")
                elif correct <= 8 and i == 2 and j == 0:
                    querys.append(f"INSERT INTO Guesses (submissionNumber, attemptId, valueRow, valueColumn, charValue) VALUES ({submission_number}, {attempt_id}, {i}, {j}, 'x');\n")
                else:
                    querys.append(f"INSERT INTO Guesses (submissionNumber, attemptId, valueRow, valueColumn, charValue) VALUES ({submission_number}, {attempt_id}, {i}, {j}, '{char}');\n")

joiner = ""
output = joiner.join(querys)

with open('../db/04_KLMVGame_Submissions.sql', 'w') as file:
  file.write(output)
