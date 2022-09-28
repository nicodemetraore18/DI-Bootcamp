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
