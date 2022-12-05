-- Exercise1

--Find out how many films there are for each rating.
SELECT rating ,count(film_id) FROM film GROUP BY rating;
--Get a list of all the movies that have a rating of G or PG-13.
SELECT  film_id,title,description,rating FROM film WHERE rating IN ('G','PG-13') AND (film.length/60)<2 AND rental_rate<3 ORDER BY title ASC;
--Find a customer in the customer table, and change his/her details to your details, using SQL UPDATE.
UPDATE customer SET first_name='Nicodeme',last_name='Traore',email='nicodemetraore18@gmail.com',last_update=CURRENT_DATE WHERE customer_id=1;
--Now find the customer’s address, and use UPDATE to change the address to your address (or make one up).
UPDATE address SET address='29 Belle ville' WHERE  address_id=(SELECT address_id FROM customer WHERE customer_id=1);

--Exercise2
-- Database: bootcamp


--UPDATE
--‘Lea Benichou’ and ‘Marc Benichou’ are twins, they should have the same birth_dates. Update both their birth_dates to 02/11/1998.
UPDATE students SET birth_date='02/11/1998' WHERE last_name='Benichou';
--Change the last_name of David from ‘Grez’ to ‘Guez’.
UPDATE students SET last_name='Guez' WHERE first_name='David';

--DELETE
--Delete the student named ‘Lea Benichou’ from the table.
DELETE FROM students WHERE last_name='Benichou' AND first_name='Lea';

--COUNT
--Count how many students are in the table.
SELECT COUNT(*) FROM students;
--Count how many students were born after 1/01/2000.
SELECT COUNT(*) FROM students WHERE birth_date > '1/01/2000';
--Add a column to the student table called math_grade.
ALTER TABLE students ADD COLUMN math_grade INTEGER ;
--Add 80 to the student which id is 1.
UPDATE students SET math_grade=80 WHERE id_students=1;
--Add 90 to the students which have ids of 2 or 4.
UPDATE students SET math_grade=90 WHERE id_students IN (1,4);
--Add 40 to the student which id is 6.
UPDATE students SET math_grade=40 WHERE id_students=6;
--Count how many students have a grade bigger than 83
SELECT COUNT(*) FROM students WHERE math_grade>83;
--Add another student named ‘Omer Simpson’ with the same birth_date as the one already in the table. Give him a grade of 70.
INSERT INTO students VALUES(6,'Omer', 'Simpson', (SELECT birth_date FROM students WHERE last_name='Simpson' AND first_name='Omer'),70);
/*Bonus: Count how many grades each student has.
Tip: You should display the first_name, last_name and the number of grades of each student. If you followed the instructions above correctly, all the students should have 1 math grade, except Omer Simpson which has 2.
Tip : Use an alias called total_grade to fetch the grades.
Hint : Use GROUP BY. */
SELECT first_name,last_name ,COUNT(math_grade) as total_grade FROM students GROUP BY first_name,last_name ;
--Find the sum of all the students grades.
SELECT SUM(math_grade) as SumNote FROM students;

--Exercise3

-- Database: public

--Create a table named purchases. It should have 3 columns 
CREATE TABLE purchases (
 	purchases_id SERIAL PRIMARY KEY NOT NULL,
	customer_id INTEGER NOT NULL,
	items_id INTEGER NOT NULL,
	quantity_purchased INTEGER NOT NULL,
	FOREIGN KEY(customer_id) REFERENCES customers(id_customers),
	FOREIGN KEY(items_id) REFERENCES items(id_items)
);

--Insert purchases for the customers, use subqueries:
--Scott Scott bought one fan
INSERT INTO purchases(customer_id,items_id,quantity_purchased) VALUES((SELECT id_customers FROM customers WHERE last_name='Scott' AND first_name='Scott'),(SELECT id_items FROM items WHERE libelle='fan' ),1);
--Melanie Johnson bought ten large desks
INSERT INTO purchases(customer_id,items_id,quantity_purchased) VALUES((SELECT id_customers FROM customers WHERE last_name='Johnson' AND first_name='Melanie'),(SELECT id_items FROM items WHERE libelle='large desk' ),10);
--Greg Jones bougth two small desks
INSERT INTO purchases(customer_id,items_id,quantity_purchased) VALUES((SELECT id_customers FROM customers WHERE last_name='Jones' AND first_name='Greg'),(SELECT id_items FROM items WHERE libelle='small desk' ),2);

--Use SQL to get the following from the database:
--All purchases. Is this information useful to us?
SELECT * FROM purchases;
--All purchases, joining with the customers table.
SELECT * FROM purchases pu INNER JOIN customers cu ON pu.customer_id=cu.id_customers;
--Purchases of the customer with the ID equal to 5.
SELECT * FROM purchases WHERE customer_id=5;
--Purchases for a large desk AND a small desk
SELECT * FROM purchases pu INNER JOIN items i ON pu.items_id=i.id_items  WHERE i.libelle IN ('large desk','small desk');

--Use SQL to show all the customers who have made a purchase. Show the following fields/columns:
--Customer first name,Customer ,last name,Item name
SELECT cu.first_name,cu.last_name, i.libelle FROM customers cu INNER JOIN purchases pu ON cu.id_customers=pu.customer_id  INNER JOIN items i ON pu.items_id=i.id_items;

--Add a row which references a customer by ID, but does not reference an item by ID (leave it blank). Does this work? Why/why not?
INSERT INTO purchases(customer_id,item_id,quantity_purchased) VALUES((SELECT id_customers FROM customers WHERE last_name='Jones' AND first_name='Sandra'),2);
--  It doesn't work beacause item_id is define to not null