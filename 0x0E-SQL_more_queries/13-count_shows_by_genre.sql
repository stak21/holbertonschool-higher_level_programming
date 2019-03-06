-- Lists all genres from hbtn_0d_tvshows and display the number of shows linked
-- to each
-- Display <TV Show genre> - <number of shows linked to this genre>
-- genre -- number_of shows
-- Don't display genre that doesn't have a show linked
-- Results: order by desc on number of shows linked
SELECT tv_genres.name AS genre, COUNT(*) AS number_of_shows FROM tv_genres
	JOIN tv_show_genres
	WHERE tv_genres.id = tv_show_genres.genre_id
	GROUP BY tv_genres.name
	ORDER BY COUNT(*) DESC;
