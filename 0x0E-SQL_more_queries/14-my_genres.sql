-- list all genres of the show Dexter
-- display tv_genres.name
-- Results: ASC by genre name
SELECT DISTINCT tv_genres.name as name
	FROM tv_show_genres 
	INNER JOIN tv_shows 
	ON tv_show_genres.show_id = (
		SELECT tv_shows.id 
		FROM tv_shows 
		WHERE tv_shows.title = 'Dexter') 
	RIGHT JOIN tv_genres 
	ON tv_genres.id = tv_show_genres.genre_id 
	WHERE tv_show_genres.genre_id IS NOT NULL 
	ORDER BY tv_genres.name ASC;
