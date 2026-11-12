USE app_db; -- Chứa các lệnh thêm dữ liệu vào app_db

INSERT IGNORE INTO orders
(order_id, total_price, fee, order_status, payment, created_at, user_id)
VALUES
(1, 45000, 10000, 'PENDING', 'CASH', '2026-11-01 09:00:00', 1),
(2, 50000, 10000, 'PENDING', 'WALLET', '2026-11-01 09:15:00', 2),

(3, 65000, 10000, 'CONFIRMED', 'CASH', '2026-11-01 10:00:00', 1),
(4, 75000, 10000, 'CONFIRMED', 'WALLET', '2026-11-01 10:20:00', 3),

(5, 90000, 10000, 'PREPARING', 'CASH', '2026-11-01 11:00:00', 2),
(6, 95000, 10000, 'PREPARING', 'WALLET', '2026-11-01 11:30:00', 1),

(7, 65000, 10000, 'SHIPPING', 'CASH', '2026-11-01 12:00:00', 3),
(8, 75000, 10000, 'SHIPPING', 'WALLET', '2026-11-01 12:20:00', 2),

(9, 50000, 10000, 'DELIVERED', 'CASH', '2026-11-01 13:00:00', 1),
(10, 65000, 10000, 'DELIVERED', 'WALLET', '2026-11-01 13:20:00', 3),

(11, 45000, 10000, 'CANCELLED', 'CASH', '2026-11-01 14:00:00', 2),
(12, 50000, 10000, 'CANCELLED', 'WALLET', '2026-11-01 14:20:00', 1);

INSERT IGNORE INTO order_details
(order_detail_id, amount, price, note, order_id, dish_id)
VALUES
(1, 1, 45000, 'It com', 1, 1),
(2, 1, 50000, NULL, 2, 2),
(3, 1, 65000, 'Khong hanh', 3, 4),
(4, 1, 50000, NULL, 4, 2),
(5, 2, 45000, NULL, 5, 1),
(6, 1, 50000, NULL, 6, 2),
(7, 1, 65000, NULL, 7, 4),
(8, 1, 45000, NULL, 8, 1),
(9, 1, 50000, NULL, 9, 2),
(10, 1, 65000, NULL, 10, 4),
(11, 1, 45000, 'Khach huy don', 11, 1),
(12, 1, 50000, 'Khach huy don', 12, 2);

INSERT IGNORE INTO order_details
(order_detail_id, amount, price, note, order_id, dish_id)
VALUES
(13, 1, 25000, NULL, 4, 6),
(14, 1, 45000, NULL, 6, 1),
(15, 1, 30000, NULL, 8, 5);

SELECT COUNT(*) AS total_users FROM users;
SELECT COUNT(*) AS total_dishes FROM dishes;