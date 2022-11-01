import sqlite3
import os

# Creates scores.sqlite

db = \
"""
PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE Scores (username TEXT, subject TEXT, score INTEGER);
INSERT INTO Scores VALUES('joe','biology-22', 80);
INSERT INTO Scores VALUES('joe','japanese-22', 75);
INSERT INTO Scores VALUES('joe','math-22', 99);
COMMIT;
"""

if os.path.exists('scores.sqlite'):
	print('tasks.sqlite already exists')
else:
	conn = sqlite3.connect('scores.sqlite')
	conn.cursor().executescript(db)
	conn.commit()
