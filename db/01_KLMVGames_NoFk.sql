use KLMVGames;

INSERT INTO Player(playerId,isPremium,fName,lName,email,birthday) VALUES (1,false,'Gunther','Hatzar','ghatzar0@usa.gov','1990-11-12');
INSERT INTO Player(playerId,isPremium,fName,lName,email,birthday) VALUES (2,true,'Kelley','Helkin','khelkin1@webmd.com','1990-11-12');
INSERT INTO Player(playerId,isPremium,fName,lName,email,birthday) VALUES (3,true,'Lazarus','Gauden','lgauden2@prnewswire.com','1990-11-12');
INSERT INTO Player(playerId,isPremium,fName,lName,email,birthday) VALUES (4,true,'Patience','Godmer','pgodmer3@wix.com','1990-11-12');
INSERT INTO Player(playerId,isPremium,fName,lName,email,birthday) VALUES (5,true,'Penni','Cohn','pcohn4@altervista.org','1990-11-12');
INSERT INTO Player(playerId,isPremium,fName,lName,email,birthday) VALUES (6,true,'Royall','Lordon','rlordon5@joomla.org','1990-11-12');
INSERT INTO Player(playerId,isPremium,fName,lName,email,birthday) VALUES (7,false,'Marget','Boddis','mboddis6@geocities.jp','1990-11-12');
INSERT INTO Player(playerId,isPremium,fName,lName,email,birthday) VALUES (8,false,'Eirena','Scholtz','escholtz7@yale.edu','1990-11-12');
INSERT INTO Player(playerId,isPremium,fName,lName,email,birthday) VALUES (9,true,'Marabel','Saffin','msaffin8@ameblo.jp','1990-11-12');
INSERT INTO Player(playerId,isPremium,fName,lName,email,birthday) VALUES (10,false,'Cory','Jedrzejewski','cjedrzejewski9@godaddy.com','1990-11-12');

-- Insert into Tutor
INSERT INTO Tutor(tutorId,fName,lName,email,background,skill) VALUES (1,'Mason','Folcarelli','mfolcarelli0@aboutads.info','Duis bibendum. Morbi non quam nec dui luctus rutrum. Nulla tellus.',5);
INSERT INTO Tutor(tutorId,fName,lName,email,background,skill) VALUES (2,'Farley','Cobbing','fcobbing1@dedecms.com','Vestibulum quam sapien, varius ut, blandit non, interdum in, ante. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Duis faucibus accumsan odio. Curabitur convallis.',1);
INSERT INTO Tutor(tutorId,fName,lName,email,background,skill) VALUES (3,'Martyn','Blazevic','mblazevic2@psu.edu','In quis justo. Maecenas rhoncus aliquam lacus. Morbi quis tortor id nulla ultrices aliquet.',2);
INSERT INTO Tutor(tutorId,fName,lName,email,background,skill) VALUES (4,'Hugo','Fraczak','hfraczak3@liveinternet.ru','Sed ante. Vivamus tortor. Duis mattis egestas metus.',0);
INSERT INTO Tutor(tutorId,fName,lName,email,background,skill) VALUES (5,'Fred','Soggee','fsoggee4@zimbio.com','Maecenas leo odio, condimentum id, luctus nec, molestie sed, justo. Pellentesque viverra pede ac diam. Cras pellentesque volutpat dui.',2);
INSERT INTO Tutor(tutorId,fName,lName,email,background,skill) VALUES (6,'Beck','Sheirlaw','bsheirlaw5@slideshare.net','In sagittis dui vel nisl. Duis ac nibh. Fusce lacus purus, aliquet at, feugiat non, pretium quis, lectus.',5);
INSERT INTO Tutor(tutorId,fName,lName,email,background,skill) VALUES (7,'Conchita','Grumell','cgrumell6@hao123.com','Phasellus in felis. Donec semper sapien a libero. Nam dui.',4);
INSERT INTO Tutor(tutorId,fName,lName,email,background,skill) VALUES (8,'Melodee','Conrard','mconrard7@cnn.com','Duis bibendum. Morbi non quam nec dui luctus rutrum. Nulla tellus.',5);
INSERT INTO Tutor(tutorId,fName,lName,email,background,skill) VALUES (9,'Devonna','Cassley','dcassley8@barnesandnoble.com','Quisque porta volutpat erat. Quisque erat eros, viverra eget, congue eget, semper rutrum, nulla. Nunc purus.',5);
INSERT INTO Tutor(tutorId,fName,lName,email,background,skill) VALUES (10,'Ruy','Evanson','revanson9@sina.com.cn','Duis bibendum. Morbi non quam nec dui luctus rutrum. Nulla tellus.',1);

-- Insert into Tutor Session
INSERT INTO TutorSession(sessionId,tutorId,playerId,hours,rate,totalPay,notes) VALUES (1,9,2,2.2,57,125.4,'Sed ante. Vivamus tortor. Duis mattis egestas metus.');
INSERT INTO TutorSession(sessionId,tutorId,playerId,hours,rate,totalPay,notes) VALUES (2,10,1,1.4,19,26.6,'Nulla ut erat id mauris vulputate elementum. Nullam varius. Nulla facilisi.');
INSERT INTO TutorSession(sessionId,tutorId,playerId,hours,rate,totalPay,notes) VALUES (3,4,10,0.8,92,73.6,'Maecenas leo odio, condimentum id, luctus nec, molestie sed, justo. Pellentesque viverra pede ac diam. Cras pellentesque volutpat dui.');
INSERT INTO TutorSession(sessionId,tutorId,playerId,hours,rate,totalPay,notes) VALUES (4,6,9,0.1,64,6.4,'Vestibulum ac est lacinia nisi venenatis tristique. Fusce congue, diam id ornare imperdiet, sapien urna pretium nisl, ut volutpat sapien arcu sed augue. Aliquam erat volutpat.');
INSERT INTO TutorSession(sessionId,tutorId,playerId,hours,rate,totalPay,notes) VALUES (5,2,10,0.3,96,28.8,'Duis bibendum. Morbi non quam nec dui luctus rutrum. Nulla tellus.');
INSERT INTO TutorSession(sessionId,tutorId,playerId,hours,rate,totalPay,notes) VALUES (6,1,4,2.8,97,271.6,'Praesent id massa id nisl venenatis lacinia. Aenean sit amet justo. Morbi ut odio.');
INSERT INTO TutorSession(sessionId,tutorId,playerId,hours,rate,totalPay,notes) VALUES (7,1,1,0.8,77,61.6,'Quisque porta volutpat erat. Quisque erat eros, viverra eget, congue eget, semper rutrum, nulla. Nunc purus.');
INSERT INTO TutorSession(sessionId,tutorId,playerId,hours,rate,totalPay,notes) VALUES (8,3,4,2.0,38,76.0,'Nam ultrices, libero non mattis pulvinar, nulla pede ullamcorper augue, a suscipit nulla elit ac nulla. Sed vel enim sit amet nunc viverra dapibus. Nulla suscipit ligula in lacus.');
INSERT INTO TutorSession(sessionId,tutorId,playerId,hours,rate,totalPay,notes) VALUES (9,9,10,0.7,46,32.2,'Fusce posuere felis sed lacus. Morbi sem mauris, laoreet ut, rhoncus aliquet, pulvinar sed, nisl. Nunc rhoncus dui vel sem.');
INSERT INTO TutorSession(sessionId,tutorId,playerId,hours,rate,totalPay,notes) VALUES (10,2,9,2.1,13,27.3,NULL);

-- Insert into GameType
INSERT INTO GameType (gameName, rules, descrip)
VALUES
    ('Crossword', 'Letter placement puzzle game with clues', 'In Crossword, players fill in a grid with words based on clues given.'),
    ('Sudoku', 'Number placement puzzle game', 'In Sudoku, players fill in a grid with numbers so that each row, column, and sub-grid contains all of the digits from 1 to 9 without any repetition.');

-- Insert into Game
INSERT INTO Game (gameName, projectCodeName, difficulty)
VALUES
    ('Crossword', 'ProjectA', 3),
    ('Crossword', 'ProjectB', 2),
    ('Crossword', 'ProjectA', 1),
    ('Crossword', 'ProjectB', 2);