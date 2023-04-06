NUMBER_SUBMISSIONS = 40
import random
import math

final_string = ""
puzzles = [
    ["*stem","*trip","dough","inch","meet"],
    ["*frog","*rice","model","idea","corn"],
    ["**boo","*rich","conch","vogue","story"],
    ["*dark","melee","icing","cake","slew"]
]
gamesAttempts = [(1, 1, False, 100, 19),
       (1, 2, False, 200, 22),
       (1, 3, False, 233, 12),
       (1, 4, False, 219, 32),
       (1, 5, True, 270, 42),
       (1, 6, False, 300, 29),
       (1, 7, True, 101, 34),
       (1, 8, False, 90, 12),
       (1, 9, True, 73, 13),
       (1, 10, False, 10, 23),
       (2, 1, False, 40, 12),
       (2, 2, False, 43, 12),
       (2, 3, True, 100, 43),
       (2, 4, False, 219, 23),
       (2, 5, False, 301, 63),
       (2, 6, True, 20, 22),
       (2, 7, False, 28, 4),
       (2, 8, False, 31, 21),
       (2, 9, False, 39, 13),
       (2, 10, False, 15, 3),
       (3, 1, True, 14, 3),
       (3, 2, False, 58, 10),
       (3, 3, False, 90, 23),
       (3, 4, False, 36, 1),
       (3, 5, False, 42, 11),
       (3, 6, False, 59, 12),
       (3, 7, False, 22, 23),
       (3, 8, True, 67, 12),
       (3, 9, False, 93, 1),
       (3, 10, False, 13, 4),
       (4, 1, False, 42, 23),
       (4, 2, True, 104, 13),
       (4, 3, False, 255, 45),
       (4, 4, False, 30, 13),
       (4, 5, True, 58, 11),
       (4, 6, False, 27, 22),
       (4, 7, False, 40, 24),
       (4, 8, True, 42, 32),
       (4, 9, False, 12, 6),
       (4, 10, False, 9, 8)]

submissions = []

for i in range(1,NUMBER_SUBMISSIONS + 1):
    for j in range(1,3):
        if j == 1:
            numWrong = math.floor(random.randint(0,20)/2)
            s = f"(1,{i},{numWrong}),"
            submissions.append((2,i,numWrong))
            final_string += s
        else:
            s = f"(2,{i},0),"
            final_string += s
            submissions.append((1,i,0))
print(final_string)
print("s")
print("s")
print("s")
print("s")
guesses = []
s = ""
test = {}
for sub in submissions:
    subNum = sub[0]
    attempt = sub[1]
    wrong = sub[2]
    game = gamesAttempts[attempt - 1][0]
    puzzle = puzzles[game - 1]
    if wrong == 0:
        for i, row in enumerate(puzzle):
            for j, char in enumerate(row):
                if char != '*':
                    s += (f"({subNum},{attempt},{i},{j},'{char}'),")
    else:
        correct = 10 - wrong
        for i, row in enumerate(puzzle):
            for j, char in enumerate(row):
                if char == '*':
                    continue
                if correct <= 0:
                    if i == 0 and j == 3:
                        s += (f"({subNum},{attempt},{i},{j},'x'),")
                if correct <= 2:
                    if i == 1 and j == 3:
                        s += (f"({subNum},{attempt},{i},{j},'x'),")
                if correct <= 4:
                    if i == 4 and j == 0:
                        s += (f"({subNum},{attempt},{i},{j},'x'),")
                if correct <= 6:
                    if i == 3 and j == 0:
                        s += (f"({subNum},{attempt},{i},{j},'x'),")
                if correct <= 8:
                    if i == 2 and j == 0:
                        s += (f"({subNum},{attempt},{i},{j},'x'),")
                else:
                     s += (f"({subNum},{attempt},{i},{j},'{char}'),")

print(s)





