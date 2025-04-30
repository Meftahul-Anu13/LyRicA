-- 1. Create Trigger Function to auto-increase streams when a song is played
CREATE OR REPLACE FUNCTION increment_stream_count()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE music_song
    SET streams = streams + 1
    WHERE id = NEW.song_id;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- 2. Create Trigger on music_listen Table
DROP TRIGGER IF EXISTS after_listen_insert ON music_listen;
CREATE TRIGGER after_listen_insert
AFTER INSERT ON music_listen
FOR EACH ROW
EXECUTE FUNCTION increment_stream_count();


-- 3. Group By Artist - Total Streams
SELECT 
    music_artist.name AS artist_name, 
    SUM(music_song.streams) AS total_streams
FROM 
    music_song
JOIN 
    music_artist ON music_song.artist_id = music_artist.id
GROUP BY 
    music_artist.name
ORDER BY 
    total_streams DESC;


-- 4. Rollup by Artist
SELECT 
    music_artist.name AS artist_name, 
    SUM(music_song.streams) AS total_streams
FROM 
    music_song
JOIN 
    music_artist ON music_song.artist_id = music_artist.id
GROUP BY 
    ROLLUP (music_artist.name);


-- 5. Cube by Artist and Album
SELECT 
    music_artist.name AS artist_name, 
    music_album.title AS album_title, 
    SUM(music_song.streams) AS total_streams
FROM 
    music_song
JOIN 
    music_artist ON music_song.artist_id = music_artist.id
JOIN 
    music_album ON music_song.album_id = music_album.id
GROUP BY 
    CUBE (music_artist.name, music_album.title);


-- 6. Create a trigger function for playlist play count
CREATE OR REPLACE FUNCTION increment_playlist_play_count()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE music_playlist
    SET play_count = play_count + 1
    WHERE id = NEW.playlist_id;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- 7. Create dummy 'playlist_play' table to track plays
CREATE TABLE IF NOT EXISTS playlist_play (
    id SERIAL PRIMARY KEY,
    playlist_id INT REFERENCES music_playlist(id),
    played_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 8. Create trigger after inserting a playlist play
DROP TRIGGER IF EXISTS after_playlist_play ON playlist_play;
CREATE TRIGGER after_playlist_play
AFTER INSERT ON playlist_play
FOR EACH ROW
EXECUTE FUNCTION increment_playlist_play_count();
