/*
--Creating Database
CREATE DATABASE public;

--creating table items
CREATE TABLE items (
item_id  SERIAL,
item_name varchar(255),
item_price int ,
CONSTRAINT item_const PRIMARY KEY(item_id)
);

--creating table customers
CREATE TABLE customers(
customers_id SERIAL,
first_name varchar(255),
last_name varchar(255),
CONSTRAINT customers_const PRIMARY KEY(customers_id)

);

--Inserting into items table
INSERT INTO items (item_name,item_price)
VALUES ("Small Desk",100);
INSERT INTO items (item_name,item_price)
VALUES ("Large Desk",300);
INSERT INTO items (item_name,item_price)
VALUES ("Fan",80);

--Inserting into customers table
INSERT INTO customers (first_name,last_name)
VALUES ("Greg","Jones");
INSERT INTO customers (first_name,last_name)
VALUES ("Sandra","Jones");
INSERT INTO customers (first_name,last_name)
VALUES ("Scott","Scott");
INSERT INTO customers (first_name,last_name)
VALUES ("Trevor","Green");
INSERT INTO customers (first_name,last_name)
VALUES ("Melanie","Johnson");

--Fetching All the items.
SELECT * from items;

--Fetching All the items with a price above 80 (80 not included).
SELECT *from items WHERE item_price>80;

--Fetching All the items with a price below 300. (300 included)
SELECT *from items WHERE item_price<300;

--Fetching All customers whose last name is ‘Smith’ (What will be your outcome?).
SELECT *from customers WHERE last_name=="Smith";
--Outcome None


--Fetching All customers whose last name is ‘Jones’.
SELECT *from customers WHERE last_name=="Jones";

--Fetching All customers whose  first name  is not Scott.
SELECT *from customers WHERE first_name !="Scott";
*/

/*
 Exercise 1 : Items And Customers
Instructions
We will work on the public database that we created yesterday.

1Use SQL to get the following from the database:
 1.All items, ordered by price (lowest to highest).
 2.Items with a price above 80 (80 included), ordered by price (highest to lowest).
 3.The first 3 customers in alphabetical order of the first name (A-Z) – exclude the primary key column from the results.
 4.All last names (no other columns!), in reverse alphabetical order (Z-A)
 
 */

--1
SELECT * FROM items ORDER BY item_price DESC;

--2 
SELECT * FROM items WHERE item_price>=80 ORDER BY item_price DESC;

--3
SELECT first_name,last_name FROM customers ORDER BY first_name ASC LIMIT 3;

--4
SELECT last_name FROM customers ORDER BY last_name DESC;



