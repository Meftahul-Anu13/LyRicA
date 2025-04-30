CREATE OR REPLACE FUNCTION update_followers_on_follow() 
RETURNS TRIGGER AS $$
BEGIN
    -- Increase the followers count by 1
    UPDATE music_artist
    SET followers = followers + 1
    WHERE id = NEW.artist_id;

    -- Return the new row (important for triggers)
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER update_followers_on_artist_follow
AFTER INSERT ON music_artistfollow
FOR EACH ROW
EXECUTE FUNCTION update_followers_on_follow();


CREATE OR REPLACE FUNCTION update_followers_on_unfollow()
RETURNS TRIGGER AS $$
BEGIN
    -- Decrease the followers count of the artist by 1
    UPDATE music_artist
    SET followers = followers - 1
    WHERE id = OLD.artist_id;
    RETURN OLD;  -- Return the old row because it's a DELETE trigger
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER update_followers_on_artist_unfollow
AFTER DELETE ON music_artistfollow
FOR EACH ROW
EXECUTE FUNCTION update_followers_on_unfollow();
