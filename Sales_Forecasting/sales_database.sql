CREATE TABLE IF NOT EXISTS product_catalog (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    unit_price DECIMAL(10, 2)
);

CREATE TABLE IF NOT EXISTS daily_sales_records (
    transaction_id VARCHAR(50) PRIMARY KEY,
    sale_date DATE,
    product_id INT,
    units_sold INT,
    store_region VARCHAR(50),
    total_revenue DECIMAL(12, 2),
    FOREIGN KEY (product_id) REFERENCES product_catalog(product_id)
);

INSERT INTO product_catalog (product_id, product_name, category, unit_price) VALUES
(101, 'Pro Laptop x1', 'Electronics', 1200.00),
(102, 'Wireless Smart Mouse', 'Electronics', 45.00),
(103, 'Ergonomic Office Chair', 'Furniture', 250.00),
(104, 'Fleece Comfort Hoodie', 'Apparel', 65.00)
ON CONFLICT (product_id) DO NOTHING;