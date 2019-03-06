-- lists all shows contained in hbtn_0d_tvshows that ahve at least one genre
-- linked
-- display tv_shows.title - tv_show_genres.genre_id
-- result: asc order by tv_shows.title and tv_show_genres.genre_id
SELECT tv_shows.title AS title, tv_show_genres.genre_id AS genre_id 
	FROM tv_shows 
	JOIN tv_show_genres 
	WHERE tv_shows.id = tv_show_genres.show_id 
	ORDER BY tv_shows.title ASC, tv_show_genres.genre_id;
