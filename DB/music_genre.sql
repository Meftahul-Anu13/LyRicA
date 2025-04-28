INSERT INTO music_genre (name) 
VALUES
    ('acoustic'),
    ('rock');
INSERT INTO music_genre (name) 
VALUES
    ('pop'),
    ('rap'),
    ('electronic'),
    ('r&b'),
    ('indie');
INSERT INTO music_genre (name) 
VALUES  
    ('hip-hop'),
    ('dance');
INSERT INTO music_genre (name) 
VALUES
    ('latin'),
    ('kpop'),
    ('afropop')
INSERT INTO music_genre (name) 
VALUES
    ('jazz'),
    ('country'),
    ('classical'),
    ('metal'),
    ('punk'),
    ('funk'),
    ('alternative');

SELECT * FROM public.music_genre
ORDER BY id ASC 