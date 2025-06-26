-- View raw data
SELECT * 
FROM sales_db.raw_sales
LIMIT 10;

-- View cleaned data
SELECT * 
FROM sales_db.clean_sales
LIMIT 10;

-- Filter out nulls
SELECT * 
FROM sales_db.clean_sales
WHERE quantity IS NOT NULL;

-- Sales by product
SELECT product, SUM(quantity) AS total_quantity, AVG(price) AS avg_price
FROM sales_db.clean_sales
GROUP BY product
ORDER BY total_quantity DESC;

-- Most recent transactions
SELECT * 
FROM sales_db.clean_sales
ORDER BY timestamp DESC
LIMIT 20;
