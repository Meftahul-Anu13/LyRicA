INSERT INTO music_album (title, release_date, artist_id)
VALUES
    ('Seven', '2024-11-01', (SELECT id FROM music_artist WHERE name = 'Jung Kook' LIMIT 1)),
    ('LALA', '2024-10-15', (SELECT id FROM music_artist WHERE name = 'Myke Towers' LIMIT 1)),
    ('Guts', '2024-09-14', (SELECT id FROM music_artist WHERE name = 'Olivia Rodrigo' LIMIT 1)),
    ('Lover', '2024-06-25', (SELECT id FROM music_artist WHERE name = 'Taylor Swift' LIMIT 1)),
    ('Sprinter', '2024-09-09', (SELECT id FROM music_artist WHERE name = 'Dave' LIMIT 1)),
    ('NewJeans', '2024-08-23', (SELECT id FROM music_artist WHERE name = 'NewJeans' LIMIT 1)),
    ('Endless Summer Vacation', '2024-03-10', (SELECT id FROM music_artist WHERE name = 'Miley Cyrus' LIMIT 1)),
    ('Fine Line', '2024-07-21', (SELECT id FROM music_artist WHERE name = 'Harry Styles' LIMIT 1)),
    ('SOS', '2024-01-10', (SELECT id FROM music_artist WHERE name = 'SZA' LIMIT 1)),
    ('Cupid', '2024-07-18', (SELECT id FROM music_artist WHERE name = 'Fifty Fifty' LIMIT 1)),
    ('Barbie The Album', '2024-05-23', (SELECT id FROM music_artist WHERE name = 'Billie Eilish' LIMIT 1)),
    ('AM', '2024-07-12', (SELECT id FROM music_artist WHERE name = 'Arctic Monkeys' LIMIT 1)),
    ('Calm Down', '2024-05-30', (SELECT id FROM music_artist WHERE name = 'Rema' LIMIT 1)),
    ('Spider-Man: Into the Spider-Verse Soundtrack', '2024-06-22', (SELECT id FROM music_artist WHERE name = 'Post Malone' LIMIT 1)),
    ('Starboy', '2024-05-10', (SELECT id FROM music_artist WHERE name = 'The Weeknd' LIMIT 1)),
    ('People', '2024-08-30', (SELECT id FROM music_artist WHERE name = 'Libianca' LIMIT 1)),
    ('Speak Now (Taylor''s Version)', '2024-07-07', (SELECT id FROM music_artist WHERE name = 'Taylor Swift' LIMIT 1)),
    ('Dreamland', '2024-06-17', (SELECT id FROM music_artist WHERE name = 'Glass Animals' LIMIT 1)),
    ('golden hour', '2024-08-11', (SELECT id FROM music_artist WHERE name = 'JVKE' LIMIT 1)),
    ('Gloria', '2024-09-05', (SELECT id FROM music_artist WHERE name = 'Sam Smith' LIMIT 1)),
    ('Justice', '2024-06-18', (SELECT id FROM music_artist WHERE name = 'Justin Bieber' LIMIT 1)),
    ('Divinely Uninspired To A Hellish Extent', '2024-08-08', (SELECT id FROM music_artist WHERE name = 'Lewis Capaldi' LIMIT 1)),
    ('Born To Die', '2024-08-28', (SELECT id FROM music_artist WHERE name = 'Lana Del Rey' LIMIT 1)),
    ('Safe Haven', '2024-08-23', (SELECT id FROM music_artist WHERE name = 'Ruth B.' LIMIT 1)),
    ('Mercury - Act 1', '2024-07-30', (SELECT id FROM music_artist WHERE name = 'Imagine Dragons' LIMIT 1)),
    ('Divide', '2024-07-10', (SELECT id FROM music_artist WHERE name = 'Ed Sheeran' LIMIT 1)),
    ('Evolve', '2024-08-04', (SELECT id FROM music_artist WHERE name = 'Imagine Dragons' LIMIT 1)),
    ('Native', '2024-07-29', (SELECT id FROM music_artist WHERE name = 'OneRepublic' LIMIT 1)),
    ('Breezy', '2024-09-11', (SELECT id FROM music_artist WHERE name = 'Chris Brown' LIMIT 1)),
    ('Barrio Fino', '2024-07-04', (SELECT id FROM music_artist WHERE name = 'Daddy Yankee' LIMIT 1)),
    ('Views', '2024-06-12', (SELECT id FROM music_artist WHERE name = 'Drake' LIMIT 1)),
    ('Strange Trails', '2024-06-27', (SELECT id FROM music_artist WHERE name = 'Lord Huron' LIMIT 1)),
    ('Talk That Talk', '2024-07-22', (SELECT id FROM music_artist WHERE name = 'Rihanna' LIMIT 1)),
    ('Narrated For You', '2024-08-14', (SELECT id FROM music_artist WHERE name = 'Alec Benjamin' LIMIT 1)),
    ('Night Visions', '2024-06-16', (SELECT id FROM music_artist WHERE name = 'Imagine Dragons' LIMIT 1)),
    ('1989', '2024-06-20', (SELECT id FROM music_artist WHERE name = 'Taylor Swift' LIMIT 1)),
    ('Four', '2024-08-25', (SELECT id FROM music_artist WHERE name = 'One Direction' LIMIT 1)),
    ('Doo-Wops & Hooligans', '2024-07-08', (SELECT id FROM music_artist WHERE name = 'Bruno Mars' LIMIT 1)),
    ('Hozier', '2024-06-11', (SELECT id FROM music_artist WHERE name = 'Hozier' LIMIT 1)),
    ('Fearless', '2024-07-06', (SELECT id FROM music_artist WHERE name = 'Taylor Swift' LIMIT 1)),
    ('Escapism', '2024-08-05', (SELECT id FROM music_artist WHERE name = 'RAYE' LIMIT 1));

DELETE FROM music_album WHERE artist_id = 109;

WITH ordered_albums AS (
    SELECT id, ROW_NUMBER() OVER (ORDER BY id) AS new_id
    FROM music_album
)
UPDATE music_album
SET id = ordered_albums.new_id
FROM ordered_albums
WHERE music_album.id = ordered_albums.id;

INSERT INTO music_album (title, release_date, artist_id)
VALUES
    ('Meteora', '2003-03-25', (SELECT id FROM music_artist WHERE name = 'Linkin Park' LIMIT 1)),
    ('The Eminem Show', '2002-05-26', (SELECT id FROM music_artist WHERE name = 'Eminem' LIMIT 1)),
    ('Future Nostalgia', '2020-03-27', (SELECT id FROM music_artist WHERE name = 'Dua Lipa' LIMIT 1)),
    ('Ctrl', '2017-06-09', (SELECT id FROM music_artist WHERE name = 'SZA' LIMIT 1)),
    ('21', '2011-01-24', (SELECT id FROM music_artist WHERE name = 'Adele' LIMIT 1)),
    ('X', '2014-06-20', (SELECT id FROM music_artist WHERE name = 'Ed Sheeran' LIMIT 1)),
    ('Folklore', '2020-07-24', (SELECT id FROM music_artist WHERE name = 'Taylor Swift' LIMIT 1)),
    ('Midnights', '2022-10-21', (SELECT id FROM music_artist WHERE name = 'Taylor Swift' LIMIT 1)),
    ('The College Dropout', '2004-02-10', (SELECT id FROM music_artist WHERE name = 'Kanye West' LIMIT 1)),
    ('After Hours', '2020-03-20', (SELECT id FROM music_artist WHERE name = 'The Weeknd' LIMIT 1)),
    ('Lemonade', '2016-04-23', (SELECT id FROM music_artist WHERE name = 'Beyoncé' LIMIT 1));

INSERT INTO music_album (title, release_date, artist_id)
VALUES
    ('Abar Hashimukh', '2020-08-15', (SELECT id FROM music_artist WHERE name = 'James' LIMIT 1)),
    ('Meghbalika', '2018-07-20', (SELECT id FROM music_artist WHERE name = 'Tahsan Rahman Khan' LIMIT 1)),
    ('Chandrabindu', '2016-10-10', (SELECT id FROM music_artist WHERE name = 'Habib Wahid' LIMIT 1)),
    ('Tum Hi Ho', '2013-04-15', (SELECT id FROM music_artist WHERE name = 'Arijit Singh' LIMIT 1)),
    ('Barso Re', '2007-08-20', (SELECT id FROM music_artist WHERE name = 'Shreya Ghoshal' LIMIT 1)),
    ('Madhubala', '2022-06-01', (SELECT id FROM music_artist WHERE name = 'Neha Kakkar' LIMIT 1));

WITH ordered_albums AS (
    SELECT id, ROW_NUMBER() OVER (ORDER BY id) AS new_id
    FROM music_album
)
UPDATE music_album
SET id = ordered_albums.new_id
FROM ordered_albums
WHERE music_album.id = ordered_albums.id;

INSERT INTO music_album (title, release_date, artist_id)
VALUES
    ('Chromatica', '2020-05-29', (SELECT id FROM music_artist WHERE name = 'Lady Gaga' LIMIT 1)),
	('Four', '2024-08-25', (SELECT id FROM music_artist WHERE name = 'One Direction' LIMIT 1)),
    ('Goodbye & Good Riddance', '2018-05-23', (SELECT id FROM music_artist WHERE name = 'Juice WRLD' LIMIT 1)),
    ('American Idiot', '2004-09-21', (SELECT id FROM music_artist WHERE name = 'Green Day' LIMIT 1)),
    ('Random Access Memories', '2013-05-17', (SELECT id FROM music_artist WHERE name = 'Daft Punk' LIMIT 1));

WITH ordered_albums AS (
    SELECT id, ROW_NUMBER() OVER (ORDER BY id) AS new_id
    FROM music_album
)
UPDATE music_album
SET id = ordered_albums.new_id
FROM ordered_albums
WHERE music_album.id = ordered_albums.id;

SELECT * FROM public.music_album
ORDER BY id ASC
