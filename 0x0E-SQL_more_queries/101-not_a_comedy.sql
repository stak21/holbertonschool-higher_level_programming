-- Lists all shows without the genre Comedy
-- Display tv_shows.title
-- ASC order by the show title
-- SELECT TWICE
SELECT tv_shows.title FROM tv_shows WHERE tv_shows.id NOT IN (
	SELECT tv_show_genres.show_id FROM tv_show_genres 
	JOIN tv_genres
	ON tv_show_genres.genre_id = tv_genres.id
	AND tv_genres.name = 'Comedy')
	ORDER BY tv_shows.title ASC;
