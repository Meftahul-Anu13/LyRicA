CREATE OR REPLACE FUNCTION update_status_on_upload()
RETURNS trigger AS $$
BEGIN
    IF NEW.status = 'Approved' THEN
        UPDATE music_songrequest  -- Change this to match your actual table name
        SET status = 'Approved', file_url = NEW.file_url
        WHERE id = NEW.id;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_status
AFTER UPDATE ON music_songrequest  -- Change this to match your actual table name
FOR EACH ROW
WHEN (OLD.status IS DISTINCT FROM NEW.status)
EXECUTE FUNCTION update_status_on_upload();
