
SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', 'public', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;


create extension dblink;

DO
$do$
BEGIN
   IF EXISTS (SELECT FROM pg_database WHERE datname = 'movies') THEN
      RAISE NOTICE 'Database already exists';  
   ELSE
      PERFORM dblink_exec('dbname=' || current_database()  
                        , 'CREATE DATABASE movies');
   END IF;
END
$do$;

\c movies;


create table if not exists reviews (
  	id int PRIMARY KEY,
	text text,
  	movie_id varchar(100)

);

create table if not exists meta (
	author_id varchar(255),
	author_name varchar(255),
	date timestamp,
  	review_id int ,
    CONSTRAINT review_id
      FOREIGN KEY(review_id) 
	  REFERENCES public.reviews(id)
  
);

create table if not exists reviews_likes (
    user_id varchar(255),
    date timestamp,
    review_id int,
    CONSTRAINT review_id
        FOREIGN KEY(review_id) 
	      REFERENCES public.reviews(id),
    UNIQUE (user_id, review_id)
)

