-- List all shows and genres linked to that show frmo the db
-- if a show doesn't have a genre display NULL
-- Display tv_shows.title - tv_genres.name
-- Results: ASC order by show title and genre name
SELECT tv_shows.title AS title, tv_genres.name AS name
	FROM tv_genres
	LEFT JOIN tv_show_genres
	ON tv_genres.id = tv_show_genres.genre_id
	RIGHT JOIN tv_shows
	ON tv_shows.id = tv_show_genres.show_id
	ORDER BY tv_shows.title, tv_genres.name;
