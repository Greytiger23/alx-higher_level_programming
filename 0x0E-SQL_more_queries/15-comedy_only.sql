-- Lists all Comedy shows in the database hbtn_0d_tvshows
SELECT tv_shows.title
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genres_id = tv_genres.id
WHERE tv_shows.name = 'Comedy'
ORDER BY tv_shows.title ASC;
