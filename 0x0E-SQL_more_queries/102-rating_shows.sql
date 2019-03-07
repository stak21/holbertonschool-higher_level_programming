-- List all shows by their rating
-- Display tv_shows.title - rating sum
-- DESC order by rating
SELECT tv_shows.title AS title, SUM(tv_show_ratings.rate) AS rating
	FROM tv_show_ratings
	JOIN tv_shows
	ON tv_shows.id = tv_show_ratings.show_id
	GROUP BY tv_show_ratings.show_id
	ORDER BY SUM(tv_show_ratings.rate) DESC;
