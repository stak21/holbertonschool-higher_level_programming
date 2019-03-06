-- Lists all Comedy shows in the DB
-- Display tv_shows.title
-- Results ASC order by show title
SELECT tv_shows.title 
	FROM tv_show_genres 
	JOIN tv_genres 
	ON tv_genres.name = 'Comedy' AND tv_show_genres.genre_id = tv_genres.id 
	INNER JOIN tv_shows 
	ON tv_shows.id = tv_show_genres.show_id 
	ORDER BY tv_shows.title;
