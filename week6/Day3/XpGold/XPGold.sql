--Exercise1
-- Database: dvdrental
	
--Get a list of all rentals which are out (have not been returned). How do we identify these films in the database?
SELECT * FROM rental WHERE return_date IS NULL;
--Get a list of all customers who have not returned their rentals. Make sure to group your results.
SELECT * FROM customer cu INNER JOIN rental r ON r.customer_id=cu.customer_id WHERE r.return_date IS NULL;
--Get a list of all the Action films with Joe Swank.
SELECT f.title FROM film f INNER JOIN film_category fc ON f.film_id=fc.film_id INNER JOIN film_actor fa ON fa.film_id=f.film_id 
WHERE fc.category_id=(SELECT category_id FROM category WHERE name='Action')
AND fa.actor_id=(SELECT actor_id FROM actor WHERE last_name='Swank' AND first_name='Joe');

--Exercise2
-- Database: dvdrental	
--How many stores there are, and in which city and country they are located.
SELECT COUNT(s.store_id) as Nombre, ci.city,co.country FROM store s INNER JOIN address ad ON s.address_id=ad.address_id INNER JOIN city ci ON
ci.city_id=ad.city_id INNER JOIN country co ON co.country_id=ci.country_id GROUP BY ci.city,co.country ;

--How many hours of viewing time there are in total in each store – in other words, the sum of the length of every inventory item in each store.
SELECT SUM(f.length), i.store_id FROM film f INNER JOIN inventory i ON f.film_id=i.film_id GROUP BY i.store_id;

--A list of all customers in the cities where the stores are located.
SELECT cu.first_name,cu.last_name ,ci.city FROM customer cu INNER JOIN address ad ON cu.address_id=ad.address_id INNER JOIN city ci ON ci.city_id=ad.city_id
INNER JOIN store s ON cu.store_id=s.store_id WHERE cu.address_id=s.address_id;
--A list of all customers in the countries where the stores are located.

--Some people will be frightened by watching scary movies while zombies walk the streets. Create a ‘safe list’ of all movies which do not include the ‘Horror’ category, or contain the words ‘beast’, ‘monster’, ‘ghost’, ‘dead’, ‘zombie’, or ‘undead’ in their titles or descriptions… Get the sum of their viewing time (length).
--Hint : use the CHECK contraint

--For both the ‘general’ and the ‘safe’ lists above, also calculate the time in hours and days (not just minutes).