-- CREATE VIEW chron_movies_and_director AS
-- SELECT title, year_ AS release_year, concat(first_name," ",last_name) AS director
-- FROM artists 
-- JOIN casts on artists.id = casts.artist_id
-- JOIN movies on casts.movie_id = movies.id
-- WHERE role_ = "Director"
-- ORDER BY year_;

SELECT * FROM chron_movies_and_director;

-- CREATE VIEW multiple_movie_successes AS
-- SELECT concat(first_name," ",last_name) as artist,role_ as role, COUNT(*) AS works
-- FROM artists 
-- JOIN casts on artists.id = casts.artist_id
-- JOIN movies on casts.movie_id = movies.id
-- GROUP BY last_name, first_name, role_
-- HAVING works > 1
-- ORDER BY works DESC;


SELECT * FROM multiple_movie_successes;

-- DROP VIEW multiple_director_successes;
-- DROP VIEW multiple_actor_successes;

-- CREATE VIEW multiple_director_successes AS
-- SELECT concat(first_name," ",last_name) as artist,role_ as role, COUNT(*) AS works
-- FROM artists 
-- JOIN casts on artists.id = casts.artist_id
-- JOIN movies on casts.movie_id = movies.id
-- WHERE role_ = "Director"
-- GROUP BY last_name, first_name
-- HAVING works > 1
-- ORDER BY works DESC;

-- CREATE VIEW multiple_actor_successes AS
-- SELECT concat(first_name," ",last_name) as artist,role_ as role, COUNT(*) AS works
-- FROM artists 
-- JOIN casts on artists.id = casts.artist_id
-- JOIN movies on casts.movie_id = movies.id
-- WHERE role_ = "Actor"
-- GROUP BY last_name, first_name
-- HAVING works > 1
-- ORDER BY works DESC;

SELECT * FROM multiple_director_successes;

SELECT * FROM multiple_actor_successes;