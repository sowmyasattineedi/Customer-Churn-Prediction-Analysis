CREATE DATABASE IF NOT EXISTS fraud_detection_db;
USE fraud_detection_db;

DROP TABLE IF EXISTS transaction_logs;

CREATE TABLE transaction_logs (
    transaction_id VARCHAR(50) PRIMARY KEY,
    timestamp DATETIME NOT NULL,
    account_id VARCHAR(50) NOT NULL,
    transaction_amount DECIMAL(10, 2) NOT NULL,
    merchant_category VARCHAR(50) NOT NULL,
    risk_score DECIMAL(5, 2) NOT NULL,
    is_fraud TINYINT(1) NOT NULL,
    status VARCHAR(20) NOT NULL
);

INSERT INTO transaction_logs (transaction_id, timestamp, account_id, transaction_amount, merchant_category, risk_score, is_fraud, status) VALUES
('TXN-90001', '2026-06-26 10:15:00', 'ACC-4412', 1250.00, 'Online Retail', 84.50, 1, 'Blocked'),
('TXN-90002', '2026-06-26 10:18:22', 'ACC-9821', 45.20, 'Groceries', 12.10, 0, 'Approved'),
('TXN-90003', '2026-06-26 11:02:11', 'ACC-3345', 890.00, 'Electronics', 76.00, 1, 'Flagged'),
('TXN-90004', '2026-06-26 11:45:30', 'ACC-1102', 12.99, 'Coffee Shop', 5.00, 0, 'Approved'),
('TXN-90005', '2026-06-26 12:01:05', 'ACC-6754', 2100.50, 'Luxury Goods', 91.20, 1, 'Blocked'),
('TXN-90006', '2026-06-26 12:30:15', 'ACC-9821', 115.00, 'Gas Station', 18.40, 0, 'Approved');