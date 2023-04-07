USE KLMVGames;

# CROSSWORD 1
INSERT INTO Clues (gameId, valueRow, valueColumn, clue, isDown)
VALUES
    (1,0,1,'Acronym for non-humanities fields', false),
    (1,1,1,'Fall over ones feet', false),
    (1,2,0,'The tonight _____ (Ben and Jerry’s flavor)', false),
    (1,3,0,'2.54 centimenters', false),
    (1,4,0,'Swim competition', false),
    (1,2,0,'Faintly shining', true),
    (1,0,1,'Word after stepping or rolling', true),
    (1,0,2,'Can we agree to stop fighting', true),
    (1,0,3,'Number of bits in a byte', true),
    (1,0,4,'Speedometer units', true);

INSERT INTO Answers (gameId, gameName, valueRow, valueColumn, charValue)
VALUES
    (1, 'Crossword',0,1,'s'),
    (1, 'Crossword',0,2,'t'),
    (1, 'Crossword',0,3,'e'),
    (1, 'Crossword',0,4,'m'),
    (1, 'Crossword',1,1,'t'),
    (1, 'Crossword',1,2,'r'),
    (1, 'Crossword',1,3,'i'),
    (1, 'Crossword',1,4,'p'),
    (1, 'Crossword',2,0,'d'),
    (1, 'Crossword',2,1,'o'),
    (1, 'Crossword',2,2,'u'),
    (1, 'Crossword',2,3,'g'),
    (1, 'Crossword',2,4,'h'),
    (1, 'Crossword',3,0,'i'),
    (1, 'Crossword',3,1,'n'),
    (1, 'Crossword',3,2,'c'),
    (1, 'Crossword',3,3,'h'),
    (1, 'Crossword',4,0,'m'),
    (1, 'Crossword',4,1,'e'),
    (1, 'Crossword',4,2,'e'),
    (1, 'Crossword',4,3,'t');


# CROSSWORD 2
INSERT INTO Clues (gameId, valueRow, valueColumn, clue, isDown)
VALUES
    (2,0,1,'Animal with a long, sticky tongue', false),
    (2,1,1,'Most produced crop in China', false),
    (2,2,0,'You can make one for an airplane, or find one on the runway', false),
    (2,3,0,'Result of brainstorming', false),
    (2,4,0,'Most produced crop in the United States', false),
    (2,2,0,'Open ___ night', true),
    (2,0,1,'Fictional character who travels to Mordor', true),
    (2,0,2,'Motorcycle user', true),
    (2,0,3,'It covers about 71% of the worlds surface', true),
    (2,0,4,'Hairstyling group', true);

INSERT INTO Answers (gameId, gameName, valueRow, valueColumn, charValue)
VALUES
    (2, 'Crossword',0,1,'f'),
    (2, 'Crossword',0,2,'r'),
    (2, 'Crossword',0,3,'o'),
    (2, 'Crossword',0,4,'g'),
    (2, 'Crossword',1,1,'r'),
    (2, 'Crossword',1,2,'i'),
    (2, 'Crossword',1,3,'c'),
    (2, 'Crossword',1,4,'e'),
    (2, 'Crossword',2,0,'m'),
    (2, 'Crossword',2,1,'o'),
    (2, 'Crossword',2,2,'d'),
    (2, 'Crossword',2,3,'e'),
    (2, 'Crossword',2,4,'l'),
    (2, 'Crossword',3,0,'i'),
    (2, 'Crossword',3,1,'d'),
    (2, 'Crossword',3,2,'e'),
    (2, 'Crossword',3,3,'a'),
    (2, 'Crossword',4,0,'c'),
    (2, 'Crossword',4,1,'o'),
    (2, 'Crossword',4,2,'r'),
    (2, 'Crossword',4,3,'n');


# CROSSWORD 3
INSERT INTO Clues (gameId, valueRow, valueColumn, clue, isDown)
VALUES
    (3,0,2,'Bad sound from a fan', false),
    (3,1,1,'Well-off', false),
    (3,2,0,'Mollusk with pink shell', false),
    (3,3,0,'Fashion magazine headed by Anna Wintour', false),
    (3,4,0,'Journalists piece', false),
    (3,2,0,'Major pharmacy chain', true),
    (3,0,1,'Most-used part of a ginger plant', true),
    (3,0,2,'The name-o of a nursery rhyme dog', true),
    (3,0,3,'Happen', true),
    (3,0,4,'Funny seeing you here', true);

INSERT INTO Answers (gameId, gameName, valueRow, valueColumn, charValue)
VALUES
    (3, 'Crossword',0,2,'b'),
    (3, 'Crossword',0,3,'o'),
    (3, 'Crossword',0,4,'o'),
    (3, 'Crossword',1,1,'r'),
    (3, 'Crossword',1,2,'i'),
    (3, 'Crossword',1,3,'c'),
    (3, 'Crossword',1,4,'h'),
    (3, 'Crossword',2,0,'c'),
    (3, 'Crossword',2,1,'o'),
    (3, 'Crossword',2,2,'n'),
    (3, 'Crossword',2,3,'c'),
    (3, 'Crossword',2,4,'h'),
    (3, 'Crossword',3,0,'v'),
    (3, 'Crossword',3,1,'o'),
    (3, 'Crossword',3,2,'g'),
    (3, 'Crossword',3,3,'u'),
    (3, 'Crossword',3,4,'e'),
    (3, 'Crossword',4,0,'s'),
    (3, 'Crossword',4,1,'t'),
    (3, 'Crossword',4,2,'o'),
    (3, 'Crossword',4,3,'r'),
    (3, 'Crossword',4,4,'y');

# CROSSWORD 4
INSERT INTO Clues (gameId, valueRow, valueColumn, clue, isDown)
VALUES
    (4,0,1,'Word before money, meat, or matter', false),
    (4,1,0,'All-out brawl', false),
    (4,2,0,'Appropriate answer to be found on top of 7-across', false),
    (4,3,0,'Birthday dessert', false),
    (4,4,0,'Whole bunch', false),
    (4,1,0,'Podcasters needs', true),
    (4,0,1,'Back windshield stick-on', true),
    (4,0,2,'Similar', true),
    (4,0,3,'Not let a subscription lapse', true),
    (4,0,4,'Beer barrel', true);

INSERT INTO Answers (gameId, gameName, valueRow, valueColumn, charValue)
VALUES
    (4, 'Crossword',0,1,'d'),
    (4, 'Crossword',0,2,'a'),
    (4, 'Crossword',0,3,'r'),
    (4, 'Crossword',0,4,'k'),
    (4, 'Crossword',1,0,'m'),
    (4, 'Crossword',1,1,'e'),
    (4, 'Crossword',1,2,'l'),
    (4, 'Crossword',1,3,'e'),
    (4, 'Crossword',1,4,'e'),
    (4, 'Crossword',2,0,'i'),
    (4, 'Crossword',2,1,'c'),
    (4, 'Crossword',2,2,'i'),
    (4, 'Crossword',2,3,'n'),
    (4, 'Crossword',2,4,'g'),
    (4, 'Crossword',3,0,'c'),
    (4, 'Crossword',3,1,'a'),
    (4, 'Crossword',3,2,'k'),
    (4, 'Crossword',3,3,'e'),
    (4, 'Crossword',4,0,'s'),
    (4, 'Crossword',4,1,'l'),
    (4, 'Crossword',4,2,'e'),
    (4, 'Crossword',4,3,'w');