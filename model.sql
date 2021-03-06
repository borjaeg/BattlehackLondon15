CREATE DATABASE challenge_for_people;

USE challenge_for_people;
DROP TABLE IF EXISTS challenges;
CREATE TABLE challenges(
  id_challenge INT UNSIGNED AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  description TEXT,  -- NOT NULL,
  initial_date DATE,
  final_date DATE,
  donators INT UNSIGNED DEFAULT 0,
  levying FLOAT DEFAULT 0,
  proof VARCHAR(500),
  PRIMARY KEY(id_challenge)
);

-- dummy data
INSERT INTO challenges(name, description, donators, levying, proof) VALUES ('Hack For Ebro', 'Ebro river has had problems in the last month because of the huge amount of rain. I want to help my Zaragoza friends running 30 km. Do you want to run with me? Donate!', 52, 5000, 'https://www.youtube.com/embed/HgzGwKwLmgM');
INSERT INTO challenges(name, description, donators, levying, proof) VALUES ('Hack For Ebro', 'Ebola is an important disease. Hack with me', 51042, 1500000, 'https://www.youtube.com/embed/zO6D_BAuYCI');
