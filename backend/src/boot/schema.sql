CREATE TABLE IF NOT EXISTS question (
  questionid INTEGER PRIMARY KEY AUTOINCREMENT,
  question TEXT NOT NULL,
  dataset TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS procedure (
  procedureid INTEGER PRIMARY KEY AUTOINCREMENT,
  questionid INTEGER NOT NULL,
  status TEXT NOT NULL,
  accurancy INTEGER,
  model TEXT,
  FOREIGN KEY(questionid) REFERENCES question(questionid)
);

CREATE TABLE IF NOT EXISTS input (
  inputid INTEGER PRIMARY KEY AUTOINCREMENT,
  procedureid INTEGER NOT NULL,
  name TEXT NOT NULL,
  FOREIGN KEY(procedureid) REFERENCES procedure(procedureid)
);

CREATE TABLE IF NOT EXISTS output (
  outputid INTEGER PRIMARY KEY AUTOINCREMENT,
  procedureid INTEGER NOT NULL,
  name TEXT NOT NULL,
  FOREIGN KEY(procedureid) REFERENCES procedure(procedureid)
);
