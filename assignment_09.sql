--query to create table
CREATE TABLE products(
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50),
    product_category VARCHAR(50),
    product_price FLOAT
)

--query to insert multiple items
INSERT INTO products(product_id,product_name,product_category,product_price)
VALUES
(1, 'Bread', 'food', 15.00),
(2, 'Washing Powder','toiletries', 50.00),
(3, 'Fantastic Beast', 'stationery',45.00),
(4, 'Soap', 'toiletries' 20.00),
(5, 'Detergent', 'toiletries', 45.00);


--query to create sales table
CREATE TABLE sales(
    sale_id INT PRIMARY KEY,
    product_id INT,
    quantity_sold INT,
    sale_date DATE
    total_price FLOAT
);

--query to insert multiple items
INSERT INTO sales (sale_id, product_id, quantity_sold, sale_date, total_price) 
VALUES 
(1, 101, 5, '2023-10-01', 99.95),
(2, 102, 2, '2023-10-02', 49.98),
(3, 103, 10, '2023-10-03', 199.90),
(4, 104, 1, '2023-10-04', 29.99),
(5, 105, 8, '2023-10-05', 159.92);

--query to retrive all data from products table
SELECT * FROM products

--query  to retrieve product_name and price from product table
SELECT product_name, product_price FROM products

--query to retrieve 2 records from sales table
SELECT * FROM sales LIMIT 2

--query to retrieve sales that have total_price more than 100
SELECT * FROM sales WHERE total_price > 100

--query to products that have the same category
SELECT * FROM products WHERE product_category = 'toiletries'

--query to get the total number of products
SELECT COUNT(*) FROM products

--query to get sum of total sales
SELECT SUM(total_price) FROM sales

--query to get avg of product price
SELECT AVG(product_price) FROM products