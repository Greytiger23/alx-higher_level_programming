-- Lists all Comedy shows in the database hbtn_0d_tvshows
SELECT title
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genres_id = tv_genres.id
WHERE name = 'Comedy'
ORDER BY title ASC;
