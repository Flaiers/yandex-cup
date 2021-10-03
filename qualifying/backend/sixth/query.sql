SELECT tg.track_id, tg.genre_id, t.name AS track_name, g.name AS genre_name
FROM track_genre AS tg
INNER JOIN track AS t ON t.id = tg.track_id
INNER JOIN genre AS g ON g.id = tg.genre_id;