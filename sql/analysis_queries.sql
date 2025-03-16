-- Count total records
SELECT COUNT(*) FROM movies;

-- 1️⃣ Create a table for high-rated movies (rating > 8.5)
DROP TABLE IF EXISTS high_rated_movies;
CREATE TABLE high_rated_movies AS
SELECT * FROM movies WHERE rating > 8.5;

-- 2️⃣ Create a table for action movies
DROP TABLE IF EXISTS action_movies;
CREATE TABLE action_movies AS
SELECT * FROM movies WHERE genre = 'action';

-- 3️⃣ Create a table for sci-fi movies
DROP TABLE IF EXISTS sci_fi_movies;
CREATE TABLE sci_fi_movies AS
SELECT * FROM movies WHERE genre = 'sci-fi';

-- 4️⃣ Create a genre summary table (average rating per genre)
DROP TABLE IF EXISTS genre_summary;
CREATE TABLE genre_summary AS
SELECT genre, COUNT(*) AS total_movies, AVG(rating) AS avg_rating
FROM movies
GROUP BY genre;

-- 5️⃣ Get the top 5 highest-rated movies
SELECT title, rating FROM movies ORDER BY rating DESC LIMIT 5;

-- 6️⃣ Get the most popular genres (by movie count)
SELECT genre, COUNT(*) AS total_movies FROM movies GROUP BY genre ORDER BY total_movies DESC;

-- 7️⃣ Get the oldest movies in the dataset
SELECT title, year FROM movies ORDER BY year ASC LIMIT 5;
