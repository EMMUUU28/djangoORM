Django ORM Queries:
Used Mysql For Database 

Created APIS Using Django ORM 
Added Data to database from CSV File from mysql CLI 

Note: First must create models in django with the necessary fields, then must add the csv data to the table using the command - 

    LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/dbtest.csv" INTO TABLE product.shopapp_product
    FIELDS TERMINATED BY ','
    LINES TERMINATED BY '\n'
    IGNORE 1 LINES
    (PRODUCT_ID, PRODUCT_NAME, PRODUCT_CATEGORY, @cost_price, @selling_price, SALES_DATA, QUANTITY_SOLD, SEASON, @profit_margin, RATING, SPACE_OCCUPIED, NO_OF_DAYS_LEFT)
    SET 
        COST_PRICE = REPLACE(@cost_price, '$', ''),
        SELLING_PRICE = REPLACE(@selling_price, '$', ''),
        PROFIT_MARGIN = REPLACE(@profit_margin, '%', '') / 100;



Created the following APIS for data Analysis
  1. Total profit for each product API - http://127.0.0.1:8000/shopapp/product-profit/
  2. Total sales for each product API - http://127.0.0.1:8000/shopapp/product-sales/
  3. Top selling products by category API - http://127.0.0.1:8000/shopapp/top-selling-products/
  4. Average profit margin by season API - http://127.0.0.1:8000/shopapp/average-profit-margin/
  5. Low stock and high demand products API - http://127.0.0.1:8000/shopapp/low-stock-high-demand-products/


