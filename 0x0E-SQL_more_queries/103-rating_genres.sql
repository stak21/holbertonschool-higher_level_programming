-- List al genres by their rating
-- Display tv_genres.name - rating sum
-- DESC order by their rating
SELECT tv_genres.name AS name, SUM(tv_show_ratings.rate) AS rating
	FROM tv_show_ratings
	JOIN tv_show_genres
	ON tv_show_ratings.show_id = tv_show_genres.show_id
	JOIN tv_genres
	ON tv_show_genres.genre_id = tv_genres.id
	GROUP BY tv_genres.name
	ORDER BY SUM(tv_show_ratings.rate) DESC;
