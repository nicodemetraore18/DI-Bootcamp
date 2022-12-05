select * from customer;
select CONCAT(first_name, ' ',last_name) as full_name from customer;
select DISTINCT create_date from customer;
select * from customer order by first_name desc;
select film_id,title,description,release_year,rental_rate from film order by rental_rate asc;
select address,phone from address where district='Texas';
select * from film where film_id=15 or film_id= 150;
select film_id,title,description,length,rental_rate from film where title='Academy Dinosaur';
select film_id,title,description,length,rental_rate from film where title ilike 'at%';
select film_id,title,length,replacement_cost from film order by replacement_cost asc LIMIT 10;
select film_id,title,length,replacement_cost from film order by replacement_cost asc offset 10 Limit 10;
--12.Écrivez une requête qui joindra les données de la table des clients et de la table des paiements. Vous souhaitez obtenir le montant et la date de chaque paiement effectué par un client, classé par son identifiant (de 1 à…).
select CONCAT(c.first_name, ' ',c.last_name) as full_name,p.amount,p.payment_date from customer as c inner join payment as p on c.customer_id=p.customer_id;
--13.)You need to check your inventory. Write a query to get all the movies which are not in inventory.
select f.film_id,f.title from film as f where f.film_id not in (select film_id from inventory where inventory_id = 4);
--14.) Write a query to find which city is in which country.
select c.city,t.country from city c inner join country t on c.country_id=t.country_id;
--15")Write a query to get the customer’s id, names (first and last), the amount and the date of payment ordered by the id of the staff member who sold them the dvd.
select c.customer_id,CONCAT(c.first_name, ' ',c.last_name) as full_name,p.amount,p.payment_date,p.staff_id from customer c inner join payment p on c.customer_id=p.customer_id order by p.staff_id;

