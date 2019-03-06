-- Lists all shows contained in the DB
-- Display tv_shows.title, tv_show_genres.genre_id
-- Results in asc order by tv_shows.title and tv_show_genres.genre_id
-- if a show doesn't ahve a genre display NULL
SELECT tv_shows.title 
	AS title, tv_show_genres.genre_id AS genre_id 
	FROM tv_shows
	LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
	WHERE tv_shows.id = tv_show_genres.show_id OR (tv_show_genres.show_id is NULL)
	ORDER BY tv_shows.title, tv_show_genres.genre_id;
