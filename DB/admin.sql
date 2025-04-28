INSERT INTO music_user (name, email, password, profile_picture, user_type_id, created_at) 
VALUES 
    (
        'Admin', 
        'meftahul@iut-dhaka.edu', 
        'securepassword', 
        'https://example.com/admin-profile', 
        (SELECT id FROM music_usertype WHERE user_type_name = 'admin'), 
        NOW()
    );
INSERT INTO music_user (id,name, email, password, profile_picture, user_type_id, created_at) 
VALUES 
    (
        'Admin', 
        'nabilanewaz@iut-dhaka.edu', 
        'mypassword', 
        'https://example.com/admin-profile', 
        (SELECT id FROM music_usertype WHERE user_type_name = 'ADMIN'), 
        NOW()
    );
INSERT INTO music_user (name, email, password, profile_picture, user_type_id, created_at) 
VALUES 
    (
        'Admin', 
        'hexagonteam21@gmail.com', 
        'hexagon', 
        'https://example.com/admin-profile', 
        (SELECT id FROM music_usertype WHERE user_type_name = 'Admin'), 
        NOW()
    );

