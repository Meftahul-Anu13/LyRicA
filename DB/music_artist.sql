INSERT INTO music_artist (name, bio, genre_id, followers, popularity, streams)
VALUES
    ('Arijit Singh', 'Famous playback singer in India.', (SELECT id FROM music_genre WHERE name = 'acoustic' LIMIT 1), 100000000, 95, 2000000000),
    ('Shreya Ghoshal', 'Popular playback singer in India.', (SELECT id FROM music_genre WHERE name = 'acoustic' LIMIT 1), 90000000, 93, 1800000000),
    ('Def Leppard', 'Famous rock band known for hits like Pour Some Sugar on Me.', (SELECT id FROM music_genre WHERE name = 'rock' LIMIT 1), 30000000, 90, 1500000000);

ALTER TABLE music_artist ALTER COLUMN followers TYPE BIGINT;
ALTER TABLE music_artist ALTER COLUMN streams TYPE BIGINT;

INSERT INTO music_artist (name, bio, genre_id, followers, popularity, streams)
VALUES
    ('Latto', 'American rapper and singer known for collaborations with top artists.', (SELECT id FROM music_genre WHERE name = 'hip-hop' LIMIT 1), 50000000, 90, 1000000000),
    ('Jung Kook', 'Member of the popular South Korean group BTS, known for solo work.', (SELECT id FROM music_genre WHERE name = 'pop' LIMIT 1), 150000000, 95, 3000000000),
    ('Olivia Rodrigo', 'American singer and songwriter, famous for her debut album "SOUR".', (SELECT id FROM music_genre WHERE name = 'pop' LIMIT 1), 80000000, 94, 2000000000),
    ('Taylor Swift', 'American singer-songwriter known for narrative songwriting and multiple music genres.', (SELECT id FROM music_genre WHERE name = 'pop' LIMIT 1), 200000000, 98, 5000000000),
    ('Dave', 'British rapper and songwriter known for his introspective lyrics.', (SELECT id FROM music_genre WHERE name = 'hip-hop' LIMIT 1), 10000000, 85, 800000000),
    ('Central Cee', 'British rapper who gained popularity in the drill music scene.', (SELECT id FROM music_genre WHERE name = 'hip-hop' LIMIT 1), 12000000, 88, 950000000),
    ('Myke Towers', 'Puerto Rican rapper and singer known for reggaeton and Latin trap music.', (SELECT id FROM music_genre WHERE name = 'hip-hop' LIMIT 1), 40000000, 87, 900000000),
    ('SZA', 'American R&B singer known for her breakthrough album "Ctrl".', (SELECT id FROM music_genre WHERE name = 'r&b' LIMIT 1), 60000000, 92, 1500000000),
    ('Billie Eilish', 'American singer-songwriter known for her unique pop and alternative music style.', (SELECT id FROM music_genre WHERE name = 'pop' LIMIT 1), 100000000, 97, 4000000000),
    ('Harry Styles', 'British singer, songwriter, and actor, formerly of One Direction.', (SELECT id FROM music_genre WHERE name = 'pop' LIMIT 1), 150000000, 96, 3500000000),
    ('Post Malone', 'American rapper and singer known for his eclectic style.', (SELECT id FROM music_genre WHERE name = 'pop' LIMIT 1), 100000000, 94, 2500000000),
    ('Bebe Rexha', 'American singer-songwriter known for pop hits and collaborations.', (SELECT id FROM music_genre WHERE name = 'pop' LIMIT 1), 50000000, 90, 1200000000),
    ('David Guetta', 'French DJ and music producer, famous in the EDM scene.', (SELECT id FROM music_genre WHERE name = 'dance' LIMIT 1), 100000000, 95, 4000000000),
    ('Kali Uchis', 'Colombian-American singer and songwriter known for blending soul, R&B, and pop.', (SELECT id FROM music_genre WHERE name = 'r&b' LIMIT 1), 20000000, 85, 500000000),
    ('Ariana Grande', 'American singer and actress, known for her vocal range and pop hits.', (SELECT id FROM music_genre WHERE name = 'pop' LIMIT 1), 250000000, 98, 6000000000),
    ('Ice Spice', 'American rapper known for her viral success and unique style in hip-hop.', (SELECT id FROM music_genre WHERE name = 'hip-hop' LIMIT 1), 20000000, 88, 700000000),
    ('Imagine Dragons', 'American rock band known for hits like "Radioactive".', (SELECT id FROM music_genre WHERE name = 'rock' LIMIT 1), 50000000, 90, 3000000000),
    ('OneRepublic', 'American rock band known for chart-topping singles like "Counting Stars".', (SELECT id FROM music_genre WHERE name = 'rock' LIMIT 1), 30000000, 88, 1500000000),
    ('Bruno Mars', 'American singer-songwriter and performer, known for his catchy pop and R&B hits.', (SELECT id FROM music_genre WHERE name = 'r&b' LIMIT 1), 150000000, 94, 3500000000),
    ('Ruth B.', 'Canadian singer-songwriter, known for her song "Dandelions".', (SELECT id FROM music_genre WHERE name = 'pop' LIMIT 1), 20000000, 85, 600000000),
    ('Lord Huron', 'American indie rock band known for their cinematic folk-rock sound.', (SELECT id FROM music_genre WHERE name = 'indie' LIMIT 1), 15000000, 85, 700000000),
    ('JVKE', 'American singer-songwriter known for his viral hit "golden hour".', (SELECT id FROM music_genre WHERE name = 'pop' LIMIT 1), 10000000, 88, 600000000),
    ('Chris Brown', 'American singer, songwriter, and dancer, known for his R&B and pop hits.', (SELECT id FROM music_genre WHERE name = 'r&b' LIMIT 1), 70000000, 90, 3500000000),
    ('Daddy Yankee', 'Puerto Rican reggaeton singer and music producer, known for hits like "Gasolina".', (SELECT id FROM music_genre WHERE name = 'hip-hop' LIMIT 1), 100000000, 90, 4000000000),
    ('Drake', 'Canadian rapper and singer, known for his versatile music across multiple genres.', (SELECT id FROM music_genre WHERE name = 'hip-hop' LIMIT 1), 200000000, 96, 5000000000);

ALTER TABLE music_artist ADD CONSTRAINT unique_name UNIQUE (name);

INSERT INTO music_artist (name, bio, genre_id, followers, popularity, streams)
VALUES   
    ('NewJeans', 'South Korean K-pop girl group.', (SELECT id FROM music_genre WHERE name = 'kpop'), 5000000, 92, 80000000),
    ('Miley Cyrus', 'American singer and actress.', (SELECT id FROM music_genre WHERE name = 'pop'), 30000000, 97, 700000000),
    ('Fifty Fifty', 'South Korean girl group.', (SELECT id FROM music_genre WHERE name = 'kpop'), 3000000, 90, 20000000),  
    ('Arctic Monkeys', 'English rock band formed in Sheffield.', (SELECT id FROM music_genre WHERE name = 'rock'), 10000000, 92, 300000000),
    ('Rema', 'Nigerian artist pioneering Afrobeat.', (SELECT id FROM music_genre WHERE name = 'afropop'), 10000000, 93, 300000000),
    ('Dua Lipa', 'English singer and songwriter.', (SELECT id FROM music_genre WHERE name = 'pop'), 30000000, 96, 600000000),
    ('Swae Lee', 'American rapper and singer.', (SELECT id FROM music_genre WHERE name = 'hip-hop'), 12000000, 90, 400000000),
    ('Nicki Minaj', 'Trinidadian-American rapper and singer.', (SELECT id FROM music_genre WHERE name = 'hip-hop'), 35000000, 97, 900000000),
    ('Aqua', 'Danish-Norwegian dance-pop group.', (SELECT id FROM music_genre WHERE name = 'electronic'), 8000000, 88, 15000000),    
    ('Glass Animals', 'British rock band.', (SELECT id FROM music_genre WHERE name = 'rock'), 8000000, 90, 35000000),    
    ('Sam Smith', 'English singer and songwriter.', (SELECT id FROM music_genre WHERE name = 'pop'), 30000000, 95, 600000000),
    ('Ed Sheeran', 'English singer and songwriter.', (SELECT id FROM music_genre WHERE name = 'pop'), 70000000, 99, 1500000000),   
    ('Eminem', 'American rapper and songwriter.', (SELECT id FROM music_genre WHERE name = 'hip-hop'), 60000000, 98, 1200000000),
    ('Lana Del Rey', 'American singer and songwriter.', (SELECT id FROM music_genre WHERE name = 'pop'), 20000000, 94, 400000000),    
    ('Lewis Capaldi', 'Scottish singer-songwriter.', (SELECT id FROM music_genre WHERE name = 'pop'), 10000000, 91, 350000000);

UPDATE music_artist
SET bio = 'Scottish singer-songwriter known for his soulful voice and emotional ballads.'
WHERE name = 'Lewis Capaldi';
UPDATE music_artist
SET bio = 'South Korean K-pop girl group formed by ADOR under HYBE Corporation.'
WHERE name = 'NewJeans';
UPDATE music_artist
SET bio = 'American singer, songwriter, and actress, best known for her role in Disney’s Hannah Montana.'
WHERE name = 'Miley Cyrus';
UPDATE music_artist
SET bio = 'South Korean girl group under Attract have gained a strong international following.'
WHERE name = 'Fifty Fifty';
UPDATE music_artist
SET bio = 'English rock band known for their guitar-driven sound and lyricism.'
WHERE name = 'Arctic Monkeys';
UPDATE music_artist
SET bio = 'Nigerian singer, songwriter, and rapper, known for his fusion of Afrobeat, trap, and pop music.'
WHERE name = 'Rema';
UPDATE music_artist
SET bio = 'English singer, songwriter, and model winning multiple Grammy Awards.'
WHERE name = 'Dua Lipa';
UPDATE music_artist
SET bio = 'American rapper, singer, and songwriter, best known as a member of the hip hop duo Rae Sremmurd.'
WHERE name = 'Swae Lee';
UPDATE music_artist
SET bio = 'Trinidadian-American rapper, singer, and songwriter.'
WHERE name = 'Nicki Minaj';
UPDATE music_artist
SET bio = 'Danish-Norwegian dance-pop group best known for their 1997 hit single “Barbie Girl.”'
WHERE name = 'Aqua';
UPDATE music_artist
SET bio = 'British psychedelic pop band that emerged in the early 2010s.'
WHERE name = 'Glass Animals';
UPDATE music_artist
SET bio = 'English singer and songwriter. Known for their soulful voice and emotional ballads.'
WHERE name = 'Sam Smith';
UPDATE music_artist
SET bio = 'English singer-songwriter and musician, one of the best-selling music artists of all time.'
WHERE name = 'Ed Sheeran';
UPDATE music_artist
SET bio = 'American rapper, songwriter, and record producer.'
WHERE name = 'Eminem';
UPDATE music_artist
SET bio = 'American singer, songwriter, and record producer known for her cinematic music.'
WHERE name = 'Lana Del Rey';
UPDATE music_artist
SET bio = 'Legendary American rapper, known for hits like Lose Yourself.'
WHERE name = 'Eminem';

INSERT INTO music_artist (name, bio, genre_id, followers, popularity, streams)
VALUES
    ('Tate McRae', 'Canadian singer, songwriter, and dancer.', (SELECT id FROM music_genre WHERE name = 'pop' LIMIT 1), 20000000, 90, 1500000000),
    ('Doja Cat', 'American rapper, singer, and songwriter.', (SELECT id FROM music_genre WHERE name = 'rap' LIMIT 1), 70000000, 94, 2800000000),
    ('Sabrina Carpenter', 'American singer and actress.', (SELECT id FROM music_genre WHERE name = 'pop' LIMIT 1), 30000000, 88, 1500000000),
    ('Tyla', 'South African singer known for her Afrobeat-influenced sound.', (SELECT id FROM music_genre WHERE name = 'r&b' LIMIT 1), 15000000, 80, 200000000),
    ('Mae Stephens', 'British singer-songwriter.', (SELECT id FROM music_genre WHERE name = 'pop' LIMIT 1), 1000000, 70, 50000000),
    ('The Weeknd', 'Canadian singer and songwriter, known for his R&B and pop fusion.', (SELECT id FROM music_genre WHERE name = 'r&b' LIMIT 1), 100000000, 98, 5000000000),
    ('Edward Maya', 'Romanian DJ, known for his hit Stereo Love.', (SELECT id FROM music_genre WHERE name = 'electronic' LIMIT 1), 20000000, 90, 1200000000),
    ('Linkin Park', 'American rock band known for their nu-metal sound.', (SELECT id FROM music_genre WHERE name = 'rock' LIMIT 1), 50000000, 90, 3500000000),
    ('Travis Scott', 'American rapper and producer, known for his innovative music.', (SELECT id FROM music_genre WHERE name = 'rap' LIMIT 1), 50000000, 94, 3500000000),
    ('Libianca', 'American singer-songwriter.', (SELECT id FROM music_genre WHERE name = 'r&b' LIMIT 1), 5000000, 75, 200000000),
    ('Justin Bieber', 'Canadian singer and songwriter.', (SELECT id FROM music_genre WHERE name = 'pop' LIMIT 1), 250000000, 97, 6000000000);

WITH ordered_artists AS (
    SELECT id, ROW_NUMBER() OVER (ORDER BY id) AS new_id
    FROM music_artist
)
UPDATE music_artist
SET id = ordered_artists.new_id
FROM ordered_artists
WHERE music_artist.id = ordered_artists.id;
UPDATE music_artist
SET 
    id = ordered_artists.new_id,
    bio = CASE 
        WHEN music_artist.id = 44 THEN 'Canadian singer, songwriter, and dancer, known for hits like "You Broke Me First".'
        WHEN music_artist.id = 45 THEN 'American rapper, singer, and songwriter, known for her versatility across genres.'
        WHEN music_artist.id = 46 THEN 'American singer and actress, best known for her roles in Disney Channel shows and hit singles.'
        WHEN music_artist.id = 47 THEN 'South African singer known for her Afrobeat-influenced sound.'
        WHEN music_artist.id = 48 THEN 'British singer-songwriter known for her breakout hit "If We Ever Broke Up".'
        WHEN music_artist.id = 49 THEN 'Canadian singer and songwriter, widely known for his smooth R&B and pop fusion sound.'
        WHEN music_artist.id = 50 THEN 'Romanian DJ and music producer, known for his international hit "Stereo Love".'
        WHEN music_artist.id = 51 THEN 'American rock band known for their iconic nu-metal sound.'
        WHEN music_artist.id = 52 THEN 'American rapper, singer, and producer, known for his innovative music and chart-topping albums.'
        WHEN music_artist.id = 53 THEN 'American singer-songwriter known for her viral song "People" and her introspective R&B style.'
        WHEN music_artist.id = 54 THEN 'Canadian singer and songwriter, a pop sensation known for his early hits.'
        ELSE music_artist.bio
    END
FROM ordered_artists
WHERE music_artist.id = ordered_artists.id;

WITH ordered_artists AS (
    SELECT id, ROW_NUMBER() OVER (ORDER BY id) AS new_id
    FROM music_artist
)
UPDATE music_artist
SET 
    id = ordered_artists.new_id,
    bio = CASE 
         WHEN music_artist.id = 1 THEN 'Indian playback singer known for his soulful and versatile voice.'
        WHEN music_artist.id = 2 THEN 'Indian playback singer, one of the most successful and influential in Bollywood.'
        ELSE music_artist.bio
    END
FROM ordered_artists
WHERE music_artist.id = ordered_artists.id;

INSERT INTO music_artist (name, bio, genre_id, followers, popularity, streams)
VALUES
    ('Hozier', 'Irish singer-songwriter known for his soulful voice and hit "Take Me to Church".', 
        (SELECT id FROM music_genre WHERE LOWER(name) = 'indie' LIMIT 1), 
        15000000, 88, 2200000000),
    ('RAYE', 'British singer and songwriter, known for her versatility in pop and R&B.', 
        (SELECT id FROM music_genre WHERE LOWER(name) = 'pop' LIMIT 1), 
        8000000, 84, 1200000000),
    ('Alec Benjamin', 'American singer-songwriter, known for his introspective lyrics and storytelling style.', 
        (SELECT id FROM music_genre WHERE LOWER(name) = 'indie' LIMIT 1), 
        5000000, 82, 900000000),
    ('Rihanna', 'Barbadian singer, songwriter, and entrepreneur, known for her diverse music and global influence.', 
        (SELECT id FROM music_genre WHERE LOWER(name) = 'r&b' LIMIT 1), 
        300000000, 96, 7000000000);

WITH ordered_artists AS (
    SELECT id, ROW_NUMBER() OVER (ORDER BY id) AS new_id
    FROM music_artist
)
UPDATE music_artist
SET id = ordered_artists.new_id
FROM ordered_artists
WHERE music_artist.id = ordered_artists.id;

INSERT INTO music_artist (name, bio, genre_id, followers, popularity, streams)
VALUES
    ('Adele', 'English singer-songwriter known for her powerful voice and hits like "Hello".', (SELECT id FROM music_genre WHERE name = 'pop' LIMIT 1), 150000000, 95, 3500000000),
    ('Beyoncé', 'American singer, songwriter, and actress, famous for her work in pop, R&B, and hip-hop.', (SELECT id FROM music_genre WHERE name = 'r&b' LIMIT 1), 250000000, 98, 6000000000),
    ('Shakira', 'Colombian singer and dancer, famous for her Latin and pop hits.', (SELECT id FROM music_genre WHERE name = 'latin' LIMIT 1), 220000000, 93, 4000000000),
    ('Kendrick Lamar', 'American rapper known for his thought-provoking lyrics and contributions to hip-hop.', (SELECT id FROM music_genre WHERE name = 'rap' LIMIT 1), 300000000, 97, 4500000000),   
    ('Kanye West', 'American rapper, singer, and producer, known for his influential albums and fashion.', (SELECT id FROM music_genre WHERE name = 'rap' LIMIT 1), 400000000, 99, 7500000000),
	('Lil Nas X', 'American rapper and singer, known for his breakthrough hit "Old Town Road".', (SELECT id FROM music_genre WHERE name = 'rap' LIMIT 1), 160000000, 92, 3500000000),
    ('Halsey', 'American singer and songwriter, known for her blend of pop, alternative, and indie rock.', (SELECT id FROM music_genre WHERE name = 'pop' LIMIT 1), 130000000, 90, 3000000000),
    ('Coldplay', 'British rock band known for their anthemic pop-rock sound and global hits.', (SELECT id FROM music_genre WHERE name = 'rock' LIMIT 1), 200000000, 95, 5000000000),
	('Rahat Fateh Ali Khan', 'Pakistani qawwali singer, known for his Sufi music and Bollywood playback singing.', (SELECT id FROM music_genre WHERE name = 'acoustic' LIMIT 1), 100000000, 91, 2500000000),
    ('Armaan Malik', 'Indian playback singer known for his soulful and romantic ballads in Hindi and other languages.', (SELECT id FROM music_genre WHERE name = 'pop' LIMIT 1), 120000000, 85, 1500000000),
    ('Neha Kakkar', 'Indian playback singer, known for her high-pitched voice and numerous Bollywood hits.', (SELECT id FROM music_genre WHERE name = 'pop' LIMIT 1), 300000000, 90, 3500000000),
    ('Monali Thakur', 'Indian playback singer, known for her work in Bollywood music and Bengali films.', (SELECT id FROM music_genre WHERE name = 'pop' LIMIT 1), 50000000, 80, 1000000000),
    ('Atif Aslam', 'Pakistani playback singer and actor known for his romantic ballads in Bollywood and Pakistan.', (SELECT id FROM music_genre WHERE name = 'pop' LIMIT 1), 150000000, 92, 2500000000),
	('Pritam Hasan', 'Bangladeshi singer-songwriter known for his popular pop and rock music.', (SELECT id FROM music_genre WHERE name = 'pop' LIMIT 1), 8000000, 85, 300000000),
	('James', 'Bangladeshi rock and playback singer, widely regarded as one of the pioneers of the Bangladeshi rock music scene.', (SELECT id FROM music_genre WHERE name = 'rock' LIMIT 1), 100000000, 92, 2000000000),
    ('Habib Wahid', 'Bangladeshi singer, composer, and producer, known for blending traditional Bangladeshi music with modern genres.', (SELECT id FROM music_genre WHERE name = 'pop' LIMIT 1), 30000000, 90, 1800000000),
    ('Armeen Musa', 'Bangladeshi singer-songwriter, known for her folk and pop songs in Bengali.', (SELECT id FROM music_genre WHERE name = 'acoustic' LIMIT 1), 1500000, 75, 200000000),
    ('Tahsan Rahman Khan', 'Bangladeshi singer, actor, and musician known for his work in pop and rock music.', (SELECT id FROM music_genre WHERE name = 'pop' LIMIT 1), 50000000, 88, 1200000000),
    ('Shafin Ahmed', 'Bangladeshi singer and musician, known for his work in both rock and folk music.', (SELECT id FROM music_genre WHERE name = 'rock' LIMIT 1), 20000000, 80, 900000000),
    ('Miles', 'Bangladeshi rock band, known for their alternative and progressive rock sound.', (SELECT id FROM music_genre WHERE name = 'rock' LIMIT 1), 15000000, 75, 500000000),
    ('Sabrina Rifat', 'Bangladeshi playback singer, known for her performances in Bengali television and movies.', (SELECT id FROM music_genre WHERE name = 'acoustic' LIMIT 1), 1000000, 70, 50000000),
    ('Anupam Roy', 'Indian singer-songwriter, who is known for his work in Bengali films and popular music in Bangladesh.', (SELECT id FROM music_genre WHERE name = 'pop' LIMIT 1), 10000000, 85, 800000000),
	('Warfaze', 'Pioneering Bangladeshi heavy metal band, known for its contributions to rock and metal music.', (SELECT id FROM music_genre WHERE name = 'rock' LIMIT 1), 25000000, 85, 1800000000);

WITH ordered_artists AS (
    SELECT id, ROW_NUMBER() OVER (ORDER BY id) AS new_id
    FROM music_artist
)
UPDATE music_artist
SET id = ordered_artists.new_id
FROM ordered_artists
WHERE music_artist.id = ordered_artists.id;

INSERT INTO music_artist (name, bio, genre_id, followers, popularity, streams)
VALUES
    ('One Direction', 'British boy band formed on The X Factor, known for hits like "What Makes You Beautiful".', 
    (SELECT id FROM music_genre WHERE name = 'pop' LIMIT 1), 250000000, 90, 4000000000)
ON CONFLICT (name) DO NOTHING;

WITH ordered_artists AS (
    SELECT id, ROW_NUMBER() OVER (ORDER BY id) AS new_id
    FROM music_artist
)
UPDATE music_artist
SET id = ordered_artists.new_id
FROM ordered_artists
WHERE music_artist.id = ordered_artists.id;

DELETE FROM music_artist WHERE id = 109;

INSERT INTO music_artist (id, name, bio, genre_id, followers, popularity, streams)
VALUES
    (82, 'One Direction', 'British boy band formed on The X Factor, known for hits like "What Makes You Beautiful".', 
    (SELECT id FROM music_genre WHERE name = 'pop' LIMIT 1), 250000000, 90, 4000000000);

INSERT INTO music_artist (id, name, bio, genre_id, followers, popularity, streams)
VALUES
    (83, 'Lady Gaga', 'American singer, songwriter, and actress known for her versatility and theatrical performances.', 
    (SELECT id FROM music_genre WHERE name = 'pop' LIMIT 1), 300000000, 95, 4500000000),
    (84, 'Daft Punk', 'French electronic music duo known for their innovative sound and iconic helmets.', 
    (SELECT id FROM music_genre WHERE name = 'electronic' LIMIT 1), 150000000, 91, 5000000000),
    (85, 'Juice WRLD', 'American rapper and singer-songwriter known for his emo-influenced hip-hop.', 
    (SELECT id FROM music_genre WHERE name = 'hip-hop' LIMIT 1), 200000000, 92, 4200000000),
    (86, 'Green Day', 'American rock band known for their punk rock anthems and hits like "American Idiot".', 
    (SELECT id FROM music_genre WHERE name = 'rock' LIMIT 1), 180000000, 89, 3900000000);

SELECT * FROM public.music_artist
ORDER BY id ASC 
