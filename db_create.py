import psycopg2

conn = psycopg2.connect("dbname='challenge_for_people' user='root' host='localhost' password='root'")
cursor = conn.cursor()
query = """
CREATE DATABASE challenges;
USE challenges;
DROP TABLE IF EXISTS challenges;
CREATE TABLE challenges(
  id_challenge SERIAL,
  name VARCHAR(100) NOT NULL,
  description TEXT,  -- NOT NULL,
  initial_date DATE,
  final_date DATE,
  donators INT DEFAULT 0,
  levying FLOAT DEFAULT 0,
  proof VARCHAR(500),
  PRIMARY KEY(id_challenge)
);
INSERT INTO challenges(name, description, donators, levying, proof) VALUES ('Run For Ebro', 'Ebro river has had problems in the last month because of the huge amount of rain. I want to help my Zaragoza friends running 30 km. Do you want to run with me? Donate!', 52, 5000, 'https://www.youtube.com/embed/HgzGwKwLmgM');
INSERT INTO challenges(name, description, donators, levying, proof) VALUES ('Hack For Ebola', 'Ebola is an important disease. Hack with me', 51042, 1500000, 'https://www.youtube.com/embed/zO6D_BAuYCI');
"""
cursor.execute(query)
conn.close()