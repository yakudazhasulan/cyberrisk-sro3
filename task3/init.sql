CREATE DATABASE IF NOT EXISTS cyberrisk_db;

USE cyberrisk_db;

CREATE TABLE IF NOT EXISTS security_events (
    id INT AUTO_INCREMENT PRIMARY KEY,
    event_type VARCHAR(100) NOT NULL,
    severity VARCHAR(30) NOT NULL,
    description VARCHAR(255) NOT NULL
);

INSERT INTO security_events (event_type, severity, description)
VALUES
('Login Attempt', 'Low', 'Successful login'),
('Failed Login', 'Medium', 'Incorrect password'),
('SQL Injection', 'High', 'Suspicious SQL request'),
('Port Scan', 'Medium', 'Network scanning detected'),
('Malware Alert', 'Critical', 'Suspicious file detected');