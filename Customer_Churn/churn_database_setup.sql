CREATE DATABASE IF NOT EXISTS churn_db;
USE churn_db;

CREATE TABLE IF NOT EXISTS customer_metrics (
    customer_id VARCHAR(10) PRIMARY KEY,
    tenure_months INT,
    monthly_charges DECIMAL(10,2),
    total_charges DECIMAL(10,2),
    tech_support_user INT,
    contract_type VARCHAR(20),
    churned INT
);

TRUNCATE TABLE customer_metrics;

INSERT INTO customer_metrics (customer_id, tenure_months, monthly_charges, total_charges, tech_support_user, contract_type, churned) VALUES
('CUST001', 5, 65.50, 327.50, 0, 'Month-to-month', 1),
('CUST002', 24, 80.00, 1920.00, 1, 'One year', 0),
('CUST003', 1, 45.00, 45.00, 0, 'Month-to-month', 1),
('CUST004', 48, 95.20, 4569.60, 1, 'Two year', 0),
('CUST005', 12, 70.00, 840.00, 0, 'Month-to-month', 0);

SELECT * FROM customer_metrics;