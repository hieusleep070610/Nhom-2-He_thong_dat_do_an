DROP DATABASE IF EXISTS foodpay;
CREATE DATABASE foodpay CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE foodpay;

CREATE TABLE roles (
    id   INT PRIMARY KEY,
    name VARCHAR(30) NOT NULL UNIQUE
);

CREATE TABLE users (
    id            INT PRIMARY KEY,
    username      VARCHAR(100) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    fullname      VARCHAR(100) NOT NULL,
    phone_number  VARCHAR(20)  NOT NULL UNIQUE,
    address       VARCHAR(255) NOT NULL,
    created_at    DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    role_id       INT NOT NULL,
    FOREIGN KEY (role_id) REFERENCES roles(id)
);

CREATE TABLE wallets (
    id      INT PRIMARY KEY,
    user_id INT NOT NULL UNIQUE,
    balance BIGINT NOT NULL DEFAULT 0 CHECK (balance >= 0),
    status  VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE transactions (
    transactions_id  INT PRIMARY KEY,
    amount_money     INT,
    type_transaction VARCHAR(255),
    wallet_id        INT NOT NULL,
    FOREIGN KEY (wallet_id) REFERENCES wallets(id)
);

INSERT INTO roles (id, name) VALUES (1, 'customer'), (2, 'admin');

INSERT INTO users (id, username, password_hash, fullname, phone_number, address, role_id) VALUES
(1, 'nguyenvana', '$2b$10$examplehashstring1', 'Nguyễn Văn A', '0901234567', 'Hà Nội', 1),
(2, 'tranthib',   '$2b$10$examplehashstring2', 'Trần Thị B',   '0988888888', 'TP. Hồ Chí Minh', 2);

INSERT INTO wallets (id, user_id, balance, status) VALUES
(1, 1, 1250000, 'active'),
(2, 2, 5000000, 'active');

INSERT INTO transactions (transactions_id, amount_money, type_transaction, wallet_id) VALUES
(1, -135000, 'payment', 1),
(2,  500000, 'topup',   1),
(3,   68000, 'refund',  1),
(4,  -55000, 'payment', 1),
(5,  -85000, 'payment', 2),
(6, 1000000, 'topup',   2);
