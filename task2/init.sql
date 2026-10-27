CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    role VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

INSERT INTO users (username, role, email)
VALUES
    ('admin', 'Administrator', 'admin@example.com'),
    ('aidos', 'Security Analyst', 'aidos@example.com'),
    ('dana', 'Developer', 'dana@example.com'),
    ('nurlan', 'Database Administrator', 'nurlan@example.com');