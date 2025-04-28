INSERT INTO music_song (
    title, duration, file_url, album_id, artist_id, genre_id, artist_count, 
    released_year, released_month, released_day, streams, admin_id
) 
VALUES 
    (
        'Khairiyat (From "Chhichhore")', 
        280, 
        'https://example.com/khairiyat-file', 
        (SELECT id FROM music_album WHERE title = 'Chhichhore'), 
        (SELECT id FROM music_artist WHERE name = 'Arijit Singh'), 
        (SELECT id FROM music_genre WHERE name = 'acoustic'), 
        1, 2020, 6, 16, 0, 3
    ),
    (
        'Balir Shohor Female', 
        351, 
        'https://example.com/balir-shohor-file', 
        (SELECT id FROM music_album WHERE title = 'Balir Shohor'), 
        (SELECT id FROM music_artist WHERE name = 'Arijit Singh'), 
        (SELECT id FROM music_genre WHERE name = 'acoustic'), 
        2, 2020, 6, 11, 0, 3
    ),
    (
        'Let It Go', 
        283, 
        'https://example.com/let-it-go-file', 
        (SELECT id FROM music_album WHERE title = 'High ''n'' Dry'),  
        (SELECT id FROM music_artist WHERE name = 'Def Leppard'), 
        (SELECT id FROM music_genre WHERE name = 'rock'), 
        1, 1981, 7, 11, 28, 3
    )
INSERT INTO music_song (
    title, duration, file_url, album_id, artist_id, genre_id, artist_count, 
    released_year, released_month, released_day, streams, admin_id
) 
VALUES 
    ('Seven (feat. Latto)', 180, 'https://example.com/seven-file', 
        (SELECT id FROM music_album WHERE title = 'Seven'), 
        (SELECT id FROM music_artist WHERE name = 'Jung Kook'), 
        (SELECT id FROM music_genre WHERE name = 'pop'), 
        2, 2023, 7, 14, 12000000, 3
    ),
    ('LALA', 195, 'https://example.com/lala-file', 
        (SELECT id FROM music_album WHERE title = 'LALA'), 
        (SELECT id FROM music_artist WHERE name = 'Myke Towers'), 
        (SELECT id FROM music_genre WHERE name = 'latin'), 
        1, 2023, 7, 7, 8000000, 3
    ),
    ('vampire', 240, 'https://example.com/vampire-file', 
        (SELECT id FROM music_album WHERE title = 'Guts'), 
        (SELECT id FROM music_artist WHERE name = 'Olivia Rodrigo'), 
        (SELECT id FROM music_genre WHERE name = 'pop'), 
        1, 2023, 6, 30, 15000000, 3
    ),
    ('Cruel Summer', 190, 'https://example.com/cruel-summer-file', 
        (SELECT id FROM music_album WHERE title = 'Lover'), 
        (SELECT id FROM music_artist WHERE name = 'Taylor Swift'), 
        (SELECT id FROM music_genre WHERE name = 'pop'), 
        1, 2019, 8, 23, 20000000, 3
    ),
    ('Sprinter', 215, 'https://example.com/sprinter-file', 
        (SELECT id FROM music_album WHERE title = 'Sprinter'), 
        (SELECT id FROM music_artist WHERE name = 'Dave'), 
        (SELECT id FROM music_genre WHERE name = 'hip-hop'), 
        2, 2023, 6, 9, 17000000, 3
    ),
    ('Super Shy', 140, 'https://example.com/super-shy-file', 
        (SELECT id FROM music_album WHERE title = 'NewJeans'), 
        (SELECT id FROM music_artist WHERE name = 'NewJeans'), 
        (SELECT id FROM music_genre WHERE name = 'kpop'), 
        1, 2023, 7, 7, 25000000, 3
    ),
    ('Flowers', 190, 'https://example.com/flowers-file', 
        (SELECT id FROM music_album WHERE title = 'Endless Summer Vacation'), 
        (SELECT id FROM music_artist WHERE name = 'Miley Cyrus'), 
        (SELECT id FROM music_genre WHERE name = 'pop'), 
        1, 2023, 1, 12, 22000000, 3
    ),
    ('As It Was', 180, 'https://example.com/as-it-was-file', 
        (SELECT id FROM music_album WHERE title = 'Fine Line'), 
        (SELECT id FROM music_artist WHERE name = 'Harry Styles'), 
        (SELECT id FROM music_genre WHERE name = 'pop'), 
        1, 2022, 4, 1, 35000000, 3
    ),
    ('Kill Bill', 160, 'https://example.com/kill-bill-file', 
        (SELECT id FROM music_album WHERE title = 'SOS'), 
        (SELECT id FROM music_artist WHERE name = 'SZA'), 
        (SELECT id FROM music_genre WHERE name = 'r&b'), 
        1, 2023, 1, 6, 30000000, 3
    ),
    ('Cupid - Twin Ver.', 170, 'https://example.com/cupid-file', 
        (SELECT id FROM music_album WHERE title = 'Cupid'), 
        (SELECT id FROM music_artist WHERE name = 'Fifty Fifty'), 
        (SELECT id FROM music_genre WHERE name = 'kpop'), 
        1, 2023, 3, 14, 25000000, 3
    ),
    ('What Was I Made For?', 180, 'https://example.com/what-was-i-made-for-file', 
        (SELECT id FROM music_album WHERE title = 'Barbie The Album'), 
        (SELECT id FROM music_artist WHERE name = 'Billie Eilish'), 
        (SELECT id FROM music_genre WHERE name = 'pop'), 
        1, 2023, 7, 21, 15000000, 3
    ),
    ('I Wanna Be Yours', 220, 'https://example.com/i-wanna-be-yours-file', 
        (SELECT id FROM music_album WHERE title = 'AM'), 
        (SELECT id FROM music_artist WHERE name = 'Arctic Monkeys'), 
        (SELECT id FROM music_genre WHERE name = 'rock'), 
        1, 2013, 9, 6, 14000000, 3
    ),
    ('Calm Down (with Selena Gomez)', 210, 'https://example.com/calm-down-file', 
        (SELECT id FROM music_album WHERE title = 'Calm Down'), 
        (SELECT id FROM music_artist WHERE name = 'Rema'), 
        (SELECT id FROM music_genre WHERE name = 'afropop'), 
        2, 2022, 8, 26, 18000000, 3
    ),
    ('Dance The Night', 200, 'https://example.com/dance-the-night-file', 
        (SELECT id FROM music_album WHERE title = 'Barbie The Album'), 
        (SELECT id FROM music_artist WHERE name = 'Dua Lipa'), 
        (SELECT id FROM music_genre WHERE name = 'pop'), 
        1, 2023, 5, 25, 20000000, 3
    ),
    ('Anti-Hero', 175, 'https://example.com/anti-hero-file', 
        (SELECT id FROM music_album WHERE title = 'Midnights'), 
        (SELECT id FROM music_artist WHERE name = 'Taylor Swift'), 
        (SELECT id FROM music_genre WHERE name = 'pop'), 
        1, 2022, 10, 21, 25000000, 3
    ),
    ('Style', 205, 'https://example.com/style-file', 
        (SELECT id FROM music_album WHERE title = '1989'), 
        (SELECT id FROM music_artist WHERE name = 'Taylor Swift'), 
        (SELECT id FROM music_genre WHERE name = 'pop'), 
        1, 2014, 10, 27, 30000000, 3
    ),
    ('Sunflower', 161, 'https://example.com/sunflower-file', 
        (SELECT id FROM music_album WHERE title = 'Spider-Man: Into the Spider-Verse Soundtrack'), 
        (SELECT id FROM music_artist WHERE name = 'Post Malone'), 
        (SELECT id FROM music_genre WHERE name = 'hip-hop'), 
        2, 2018, 10, 18, 40000000, 3
    ),
    ('I''m Good (Blue)', 177, 'https://example.com/im-good-file', 
        (SELECT id FROM music_album WHERE title = 'Endless Summer Vacation'), 
        (SELECT id FROM music_artist WHERE name = 'David Guetta'), 
        (SELECT id FROM music_genre WHERE name = 'dance'), 
        2, 2023, 3, 17, 32000000, 3
    );
INSERT INTO music_song (
    title, duration, file_url, album_id, artist_id, genre_id, artist_count, 
    released_year, released_month, released_day, streams, admin_id
) 
VALUES 
    ('Barbie World (with Aqua) [From Barbie The Album]', 125, 'https://example.com/barbie-world-file', 
        (SELECT id FROM music_album WHERE title = 'Barbie The Album'), 
        (SELECT id FROM music_artist WHERE name = 'Nicki Minaj'), 
        (SELECT id FROM music_genre WHERE name = 'pop'), 
        3, 2023, 7, 21, 22000000, 3
    ),
    ('Angels Like You', 210, 'https://example.com/angels-like-you-file', 
        (SELECT id FROM music_album WHERE title = 'Endless Summer Vacation'), 
        (SELECT id FROM music_artist WHERE name = 'Miley Cyrus'), 
        (SELECT id FROM music_genre WHERE name = 'pop'), 
        1, 2021, 3, 7, 24000000, 3
    ),
    ('Die For You', 240, 'https://example.com/die-for-you-file', 
        (SELECT id FROM music_album WHERE title = 'Starboy'), 
        (SELECT id FROM music_artist WHERE name = 'The Weeknd'), 
        (SELECT id FROM music_genre WHERE name = 'r&b'), 
        1, 2016, 11, 25, 40000000, 3
    ),
    ('Starboy', 230, 'https://example.com/starboy-file', 
        (SELECT id FROM music_album WHERE title = 'Starboy'), 
        (SELECT id FROM music_artist WHERE name = 'The Weeknd'), 
        (SELECT id FROM music_genre WHERE name = 'r&b'), 
        2, 2016, 9, 22, 35000000, 3
    ),
    ('Die For You - Remix', 240, 'https://example.com/die-for-you-remix-file', 
        (SELECT id FROM music_album WHERE title = 'Starboy'), 
        (SELECT id FROM music_artist WHERE name = 'The Weeknd'), 
        (SELECT id FROM music_genre WHERE name = 'r&b'), 
        2, 2023, 2, 24, 33000000, 3
    ),
    ('Blinding Lights', 201, 'https://example.com/blinding-lights-file', 
        (SELECT id FROM music_album WHERE title = 'After Hours'), 
        (SELECT id FROM music_artist WHERE name = 'The Weeknd'), 
        (SELECT id FROM music_genre WHERE name = 'r&b'), 
        1, 2020, 11, 29, 50000000, 1
    ),
    ('People', 180, 'https://example.com/people-file', 
        (SELECT id FROM music_album WHERE title = 'People'), 
        (SELECT id FROM music_artist WHERE name = 'Libianca'), 
        (SELECT id FROM music_genre WHERE name = 'r&b'), 
        1, 2023, 3, 10, 20000000, 3
    ),
    ('Enchanted (Taylor''s Version)', 323, 'https://example.com/enchanted-taylors-version-file', 
        (SELECT id FROM music_album WHERE title = 'Speak Now (Taylor''s Version)'), 
        (SELECT id FROM music_artist WHERE name = 'Taylor Swift'), 
        (SELECT id FROM music_genre WHERE name = 'pop'), 
        1, 2023, 7, 7, 40000000, 3
    ),
    ('Heat Waves', 240, 'https://example.com/heat-waves-file', 
        (SELECT id FROM music_album WHERE title = 'Dreamland'), 
        (SELECT id FROM music_artist WHERE name = 'Glass Animals'), 
        (SELECT id FROM music_genre WHERE name = 'indie'), 
        1, 2020, 6, 29, 30000000, 3
    ),
    ('golden hour', 201, 'https://example.com/golden-hour-file', 
        (SELECT id FROM music_album WHERE title = 'golden hour'), 
        (SELECT id FROM music_artist WHERE name = 'JVKE'), 
        (SELECT id FROM music_genre WHERE name = 'pop'), 
        1, 2023, 1, 10, 15000000, 3
    ),
    ('Unholy (feat. Kim Petras)', 175, 'https://example.com/unholy-file', 
        (SELECT id FROM music_album WHERE title = 'Gloria'), 
        (SELECT id FROM music_artist WHERE name = 'Sam Smith'), 
        (SELECT id FROM music_genre WHERE name = 'pop'), 
        2, 2022, 9, 30, 21000000, 3
    ),
    ('Back To December (Taylor''s Version)', 290, 'https://example.com/back-to-december-file', 
        (SELECT id FROM music_album WHERE title = 'Speak Now (Taylor''s Version)'), 
        (SELECT id FROM music_artist WHERE name = 'Taylor Swift'), 
        (SELECT id FROM music_genre WHERE name = 'pop'), 
        1, 2023, 7, 7, 25000000, 3
    ),
    ('Someone You Loved', 182, 'https://example.com/someone-you-loved-file', 
        (SELECT id FROM music_album WHERE title = 'Divinely Uninspired To A Hellish Extent'), 
        (SELECT id FROM music_artist WHERE name = 'Lewis Capaldi'), 
        (SELECT id FROM music_genre WHERE name = 'indie'), 
        1, 2019, 5, 17, 38000000, 3
    );
INSERT INTO music_song (
    title, duration, file_url, album_id, artist_id, genre_id, artist_count, 
    released_year, released_month, released_day, streams, admin_id
) 
VALUES 
    ('Ghost', 152, 'https://example.com/ghost-file', 
        (SELECT id FROM music_album WHERE title = 'Justice'), 
        (SELECT id FROM music_artist WHERE name = 'Justin Bieber'), 
        (SELECT id FROM music_genre WHERE name = 'pop'), 
        1, 2021, 3, 19, 35000000, 1
    ),
    ('Under The Influence', 200, 'https://example.com/under-the-influence-file', 
        (SELECT id FROM music_album WHERE title = 'Breezy'), 
        (SELECT id FROM music_artist WHERE name = 'Chris Brown'), 
        (SELECT id FROM music_genre WHERE name = 'r&b'), 
        1, 2022, 6, 24, 40000000, 1
    ),
    ('Gasolina', 196, 'https://example.com/gasolina-file', 
        (SELECT id FROM music_album WHERE title = 'Barrio Fino'), 
        (SELECT id FROM music_artist WHERE name = 'Daddy Yankee'), 
        (SELECT id FROM music_genre WHERE name = 'latin'), 
        1, 2004, 7, 13, 55000000, 1
    ),
    ('One Dance', 173, 'https://example.com/one-dance-file', 
        (SELECT id FROM music_album WHERE title = 'Views'), 
        (SELECT id FROM music_artist WHERE name = 'Drake'), 
        (SELECT id FROM music_genre WHERE name = 'hip-hop'), 
        3, 2016, 4, 5, 60000000, 1
    ),
    ('Enchanted', 401, 'https://example.com/enchanted-file', 
        (SELECT id FROM music_album WHERE title = 'Speak Now (Taylor''s Version)'), 
        (SELECT id FROM music_artist WHERE name = 'Taylor Swift'), 
        (SELECT id FROM music_genre WHERE name = 'pop'), 
        1, 2023, 7, 7, 70000000, 1
    ),
    ('Save Your Tears', 215, 'https://example.com/save-your-tears-file', 
        (SELECT id FROM music_album WHERE title = 'After Hours'), 
        (SELECT id FROM music_artist WHERE name = 'The Weeknd'), 
        (SELECT id FROM music_genre WHERE name = 'r&b'), 
        1, 2020, 3, 20, 65000000, 1
    ),
    ('The Night We Met', 232, 'https://example.com/the-night-we-met-file', 
        (SELECT id FROM music_album WHERE title = 'Strange Trails'), 
        (SELECT id FROM music_artist WHERE name = 'Lord Huron'), 
        (SELECT id FROM music_genre WHERE name = 'indie'), 
        1, 2015, 4, 7, 45000000, 1
    ),
    ('We Found Love', 213, 'https://example.com/we-found-love-file', 
        (SELECT id FROM music_album WHERE title = 'Talk That Talk'), 
        (SELECT id FROM music_artist WHERE name = 'Rihanna'), 
        (SELECT id FROM music_genre WHERE name = 'pop'), 
        2, 2011, 9, 22, 70000000, 1
    ),
    ('Let Me Down Slowly', 197, 'https://example.com/let-me-down-slowly-file', 
        (SELECT id FROM music_album WHERE title = 'Narrated For You'), 
        (SELECT id FROM music_artist WHERE name = 'Alec Benjamin'), 
        (SELECT id FROM music_genre WHERE name = 'indie'), 
        1, 2018, 11, 16, 50000000, 1
    ),
    ('Do I Wanna Know?', 272, 'https://example.com/do-i-wanna-know-file', 
        (SELECT id FROM music_album WHERE title = 'AM'), 
        (SELECT id FROM music_artist WHERE name = 'Arctic Monkeys'), 
        (SELECT id FROM music_genre WHERE name = 'rock'), 
        1, 2013, 9, 9, 60000000, 1
    ),
    ('Demons', 176, 'https://example.com/demons-file', 
        (SELECT id FROM music_album WHERE title = 'Night Visions'), 
        (SELECT id FROM music_artist WHERE name = 'Imagine Dragons'), 
        (SELECT id FROM music_genre WHERE name = 'rock'), 
        1, 2013, 3, 17, 65000000, 1
    ),
    ('Reminder', 238, 'https://example.com/reminder-file', 
        (SELECT id FROM music_album WHERE title = 'Starboy'), 
        (SELECT id FROM music_artist WHERE name = 'The Weeknd'), 
        (SELECT id FROM music_genre WHERE name = 'r&b'), 
        1, 2016, 11, 25, 58000000, 1
    ),
    ('Shake It Off', 242, 'https://example.com/shake-it-off-file', 
        (SELECT id FROM music_album WHERE title = '1989'), 
        (SELECT id FROM music_artist WHERE name = 'Taylor Swift'), 
        (SELECT id FROM music_genre WHERE name = 'pop'), 
        1, 2014, 10, 27, 75000000, 1
    ),
    ('Why''d You Only Call Me When You''re High?', 212, 'https://example.com/why-d-you-only-call-file', 
        (SELECT id FROM music_album WHERE title = 'AM'), 
        (SELECT id FROM music_artist WHERE name = 'Arctic Monkeys'), 
        (SELECT id FROM music_genre WHERE name = 'rock'), 
        1, 2013, 9, 9, 40000000, 1
    ),
    ('Shape of You', 263, 'https://example.com/shape-of-you-file', 
        (SELECT id FROM music_album WHERE title = 'Divide'), 
        (SELECT id FROM music_artist WHERE name = 'Ed Sheeran'), 
        (SELECT id FROM music_genre WHERE name = 'pop'), 
        1, 2017, 1, 6, 80000000, 1
    ),
    ('Night Changes', 239, 'https://example.com/night-changes-file', 
        (SELECT id FROM music_album WHERE title = 'Four'), 
        (SELECT id FROM music_artist WHERE name = 'One Direction'), 
        (SELECT id FROM music_genre WHERE name = 'pop'), 
        1, 2014, 11, 17, 45000000, 1
    ),
    ('Just The Way You Are', 221, 'https://example.com/just-the-way-you-are-file', 
        (SELECT id FROM music_album WHERE title = 'Doo-Wops & Hooligans'), 
        (SELECT id FROM music_artist WHERE name = 'Bruno Mars'), 
        (SELECT id FROM music_genre WHERE name = 'r&b'), 
        1, 2010, 7, 20, 60000000, 1
    ),
    ('Take Me To Church', 241, 'https://example.com/take-me-to-church-file', 
        (SELECT id FROM music_album WHERE title = 'Hozier'), 
        (SELECT id FROM music_artist WHERE name = 'Hozier'), 
        (SELECT id FROM music_genre WHERE name = 'indie'), 
        1, 2013, 9, 13, 70000000, 1
    ),
    ('You Belong With Me', 230, 'https://example.com/you-belong-with-me-file', 
        (SELECT id FROM music_album WHERE title = 'Fearless'), 
        (SELECT id FROM music_artist WHERE name = 'Taylor Swift'), 
        (SELECT id FROM music_genre WHERE name = 'pop'), 
        1, 2008, 11, 11, 68000000, 1
    ),
    ('Escapism.', 270, 'https://example.com/escapism-file', 
        (SELECT id FROM music_album WHERE title = 'Escapism'), 
        (SELECT id FROM music_artist WHERE name = 'RAYE'), 
        (SELECT id FROM music_genre WHERE name = 'r&b'), 
        2, 2022, 11, 12, 40000000, 1
    );
WITH ordered_songs AS (
    SELECT id, ROW_NUMBER() OVER (ORDER BY id) AS new_id
    FROM music_song
)
UPDATE music_song
SET id = ordered_songs.new_id
FROM ordered_songs
WHERE music_song.id = ordered_songs.id;

SELECT * FROM public.music_song
ORDER BY id ASC
