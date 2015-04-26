import psycopg2
import os
import urlparse

#host = os.environ['DATABASE_URL']

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["DATABASE_URL"])

conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)

cursor = conn.cursor()
query="DROP TABLE IF EXISTS challenges;"
cursor.execute(query)
conn.commit()
query="""CREATE TABLE challenges(
  id_challenge SERIAL,
  name VARCHAR(100) NOT NULL,
  description TEXT,  -- NOT NULL,
  initial_date DATE,
  final_date DATE,
  donators INT DEFAULT 0,
  levying FLOAT DEFAULT 0,
  proof VARCHAR(500),
  charrllenger_name TEXT, -- NOT NULL,
  challenger_photo TEXT, -- NOT NULL,
  longitud FLOAT,
  latitud  FLOAT, 
  PRIMARY KEY(id_challenge)
);
"""
conn.commit()
cursor.execute(query)
query="INSERT INTO challenges(name, description, donators, levying, proof, charrllenger_name,challenger_photo, longitud, latitud) VALUES ('Running against the current', 'Last months rains and the melting of the snow has caused floods in the riverside of the Ebro in Zaragoza. The farmers of that zone are now in a very bad situation and they need our help. I will be running a 10 kilometers for every 100 euros we raise, giving all the money that I get thanks to sponsors and prizes to help them.', 52, 5000, 'http://embed.bambuser.com/broadcast/5462014', 'Oliver Atom', 'http://images.teinteresa.es/deportes/Oliver-realiza-disparo_TINIMA20120619_0426_18.jpg', 41.39, 0.52);"
cursor.execute(query)
query="NSERT INTO challenges(name, description, donators, levying, proof, charrllenger_name,challenger_photo) VALUES ('Hack For Ebola', 'The Ebola upbreak in Africa has already cost thousands of lifes. Join me in my next hackathon and I will give all tha money you have donated ro de Red Cross', 51042, 1500000, 'http://embed.bambuser.com/broadcast/5462014', 'Borja Espejo', 'https://pbs.twimg.com/profile_images/572892628094423040/sja06mu9_400x400.jpeg');"
cursor.execute(query)
query="INSERT INTO challenges(name, description, donators, levying) VALUES ('Solidarity Karaoke', '', 51042, 1500000);"
cursor.execute(query)
query="INSERT INTO challenges(name, description, donators, levying) VALUES ('Baking for the Homeless', '', 51042, 1500000);"
cursor.execute(query)
query="INSERT INTO challenges(name, description, donators, levying) VALUES ('Climbing the Everest', '', 51042, 1500000);"
cursor.execute(query)
query="INSERT INTO challenges(name, description, donators, levying) VALUES ('Raising Smiles', '', 51042, 1500000)"
cursor.execute(query)
query="INSERT INTO challenges(name, description, donators, levying) VALUES ('Ice Bucket Challenge', '', 51042, 1500000);"
cursor.execute(query)
query="INSERT INTO challenges(name, description, donators, levying) VALUES ('24 hours of coding', '', 51042, 1500000);"
cursor.execute(query)
conn.commit()
conn.close()