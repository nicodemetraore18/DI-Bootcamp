--Exercise 1: DVD Rental

--Get a list of all film languages.
select * from language;
--2.)Get a list of all films joined with their languages – select the following details : film title, description, and language name. 
select f.title,f.description, l.name from film f inner join language l on f.language_id=l.language_id;
--3.)Create a new table called new_film with the following columns : id, name. Add some new films to the table.
/*
create table new_film(
	id serial primary key,
	name varchar(50) not null
);
*/
insert into new_film(name) values('Antitrust Tomatoes'),('Balloon Homeward'),('BadmanDawn'),('Blackout Private'),('Boogie Amelie'),('Candles Grapes'),('Cider Desire'),('Crusade Honey'),('Deep Crusade');
--4.)Create a new table called customer_review, which will contain film reviews that customers will make.
/*create table customer_review(
	review_id serial primary key,
	film_id INTEGER REFERENCES new_film(id) ON DELETE CASCADE,
	language_id INTEGER REFERENCES language(language_id) ON DELETE CASCADE,
	title_review varchar(50),
	score INTEGER,
	review_text TEXT,
	last_update DATE
);*/
--5.)Add 2 movie reviews. Make sure you link them to valid objects in the other tables.
insert into customer_review(film_id,language_id,title_review,score,review_text,last_update)
values((SELECT id from new_film where name='Crusade Honey' LIMIT 1),(select language_id from language where name='English' limit 1),'cool',8,'this film very cool.','20-09-2012');

--6.)Delete a film that has a review from the new_film table, what happens to the customer_review table?
	--on remarque que la donnée correspondant au ID dans la table customer_review est aussi supprimer


--Exercise 2 : DVD Rental

--1.)Use UPDATE to change the language of some films. Make sure that you use valid languages.
UPDATE film
set language_id=(select language_id from language where name='German')
where title ilike '%black%';

--2.)Which foreign keys (references) are defined for the customer table? How does this affect the way in which we INSERT into the customer table?
--Découvrez combien de locations sont encore en suspens (c'est-à-dire qu'elles n'ont pas encore été retournées au magasin).
select count(*) from rental where return_date is null;
--Trouvez les 30 films les plus chers qui sont exceptionnels (c'est-à-dire qui n'ont pas encore été retournés au magasin)
select f.title,f.description,f.rental_rate from film as f
join inventory as i on f.film_id=i.film_id
join rental r on r.inventory_id=i.inventory_id
where r.return_date is null
order by f.rental_rate desc LIMIT 30;


--6.)Your friend is at the store, and decides to rent a movie. He knows he wants to see 4 movies, but he can’t remember their names. Can you help him find which movies he wants to rent?

--6.1)The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.
select f.title,f.description,a.first_name,a.last_name
from film f join film_actor on f.film_id=film_actor.film_id
join actor as a on film_actor.actor_id=a.actor_id
where f.description ilike '%sumo wrestler%' and (a.first_name='Penelope' and a.last_name='Monroe');

--2.)The 2nd film : A short documentary (less than 1 hour long), rated “R”.
select title,description,rating, length from film where length = 60 and rating='R';

--3.)The 3rd film : A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental, and he returned it between the 28th of July and the 1st of August, 2005.
select f.title,f.rental_rate,r.return_date,c.first_name,c.last_name from film f
join inventory on f.film_id=inventory.film_id
join rental r on inventory.inventory_id=r.inventory_id
join customer c on r.customer_id = c.customer_id
where f.rental_rate > 4.00 and r.return_date between
'28/07/2005' and '1/08/2005' and c.first_name='Matthew'
and  c.last_name='Mahan';

--4.)Le 4ème film : Son ami Matthew Mahan a également regardé ce film. Il y avait le mot «bateau» dans le titre ou la description, et il semblait que c'était un DVD très coûteux à remplacer.
select f.title,f.description,f.replacement_cost,c.first_name,c.last_name from film f
join inventory on f.film_id=inventory.film_id
join rental r on inventory.inventory_id=r.inventory_id
join customer c on r.customer_id = c.customer_id
where c.first_name='Matthew' and  c.last_name='Mahan' and
(f.title ilike '%boat%' or f.description ilike '%boat%')
order by f.replacement_cost desc LIMIT 1;


--Exercise 2 : DVD Rental

--1.)Use UPDATE to change the language of some films. Make sure that you use valid languages.
UPDATE film
set language_id=(select language_id from language where name='German')
where title ilike '%black%';

--2.)Which foreign keys (references) are defined for the customer table? How does this affect the way in which we INSERT into the customer table?
--Découvrez combien de locations sont encore en suspens (c'est-à-dire qu'elles n'ont pas encore été retournées au magasin).
select count(*) from rental where return_date is null;
--Trouvez les 30 films les plus chers qui sont exceptionnels (c'est-à-dire qui n'ont pas encore été retournés au magasin)
select f.title,f.description,f.rental_rate from film as f
join inventory as i on f.film_id=i.film_id
join rental r on r.inventory_id=i.inventory_id
where r.return_date is null
order by f.rental_rate desc LIMIT 30;


--6.)Your friend is at the store, and decides to rent a movie. He knows he wants to see 4 movies, but he can’t remember their names. Can you help him find which movies he wants to rent?

--6.1)The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.
select f.title,f.description,a.first_name,a.last_name
from film f join film_actor on f.film_id=film_actor.film_id
join actor as a on film_actor.actor_id=a.actor_id
where f.description ilike '%sumo wrestler%' and (a.first_name='Penelope' and a.last_name='Monroe');

--2.)The 2nd film : A short documentary (less than 1 hour long), rated “R”.
select title,description,rating, length from film where length = 60 and rating='R';

--3.)The 3rd film : A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental, and he returned it between the 28th of July and the 1st of August, 2005.
select f.title,f.rental_rate,r.return_date,c.first_name,c.last_name from film f
join inventory on f.film_id=inventory.film_id
join rental r on inventory.inventory_id=r.inventory_id
join customer c on r.customer_id = c.customer_id
where f.rental_rate > 4.00 and r.return_date between
'28/07/2005' and '1/08/2005' and c.first_name='Matthew'
and  c.last_name='Mahan';

--4.)Le 4ème film : Son ami Matthew Mahan a également regardé ce film. Il y avait le mot «bateau» dans le titre ou la description, et il semblait que c'était un DVD très coûteux à remplacer.
select f.title,f.description,f.replacement_cost,c.first_name,c.last_name from film f
join inventory on f.film_id=inventory.film_id
join rental r on inventory.inventory_id=r.inventory_id
join customer c on r.customer_id = c.customer_id
where c.first_name='Matthew' and  c.last_name='Mahan' and
(f.title ilike '%boat%' or f.description ilike '%boat%')
order by f.replacement_cost desc LIMIT 1;


--Exercise 2 : DVD Rental

--1.)Use UPDATE to change the language of some films. Make sure that you use valid languages.
UPDATE film
set language_id=(select language_id from language where name='German')
where title ilike '%black%';

--2.)Which foreign keys (references) are defined for the customer table? How does this affect the way in which we INSERT into the customer table?
--Découvrez combien de locations sont encore en suspens (c'est-à-dire qu'elles n'ont pas encore été retournées au magasin).
select count(*) from rental where return_date is null;
--Trouvez les 30 films les plus chers qui sont exceptionnels (c'est-à-dire qui n'ont pas encore été retournés au magasin)
select f.title,f.description,f.rental_rate from film as f
join inventory as i on f.film_id=i.film_id
join rental r on r.inventory_id=i.inventory_id
where r.return_date is null
order by f.rental_rate desc LIMIT 30;


--6.)Your friend is at the store, and decides to rent a movie. He knows he wants to see 4 movies, but he can’t remember their names. Can you help him find which movies he wants to rent?

--6.1)The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.
select f.title,f.description,a.first_name,a.last_name
from film f join film_actor on f.film_id=film_actor.film_id
join actor as a on film_actor.actor_id=a.actor_id
where f.description ilike '%sumo wrestler%' and (a.first_name='Penelope' and a.last_name='Monroe');

--2.)The 2nd film : A short documentary (less than 1 hour long), rated “R”.
select title,description,rating, length from film where length = 60 and rating='R';

--3.)The 3rd film : A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental, and he returned it between the 28th of July and the 1st of August, 2005.
select f.title,f.rental_rate,r.return_date,c.first_name,c.last_name from film f
join inventory on f.film_id=inventory.film_id
join rental r on inventory.inventory_id=r.inventory_id
join customer c on r.customer_id = c.customer_id
where f.rental_rate > 4.00 and r.return_date between
'28/07/2005' and '1/08/2005' and c.first_name='Matthew'
and  c.last_name='Mahan';

--4.)Le 4ème film : Son ami Matthew Mahan a également regardé ce film. Il y avait le mot «bateau» dans le titre ou la description, et il semblait que c'était un DVD très coûteux à remplacer.
select f.title,f.description,f.replacement_cost,c.first_name,c.last_name from film f
join inventory on f.film_id=inventory.film_id
join rental r on inventory.inventory_id=r.inventory_id
join customer c on r.customer_id = c.customer_id
where c.first_name='Matthew' and  c.last_name='Mahan' and
(f.title ilike '%boat%' or f.description ilike '%boat%')
order by f.replacement_cost desc LIMIT 1;

