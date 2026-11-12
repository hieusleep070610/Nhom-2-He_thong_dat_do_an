USE app_db;

SELECT
    COUNT(*) AS total_orders
FROM orders
WHERE order_id BETWEEN 1 AND 12;

SELECT
    COUNT(*) AS total_order_details
FROM order_details;

SELECT
    order_status,
    COUNT(*) AS total
FROM orders BETWEEN 1 AND 12
GROUP BY order_status
ORDER BY order_status;

SELECT
    o.order_id,
    o.order_status,
    COUNT(od.order_detail_id) AS total_dishes
FROM orders o
LEFT JOIN order_details od
    ON o.order_id = od.order_id
GROUP BY o.order_id, o.order_status
ORDER BY o.order_id;

SELECT
    o.order_id,
    o.total_price,
    COALESCE(SUM(od.amount * od.price), 0) AS calculated_price,
    CASE
        WHEN o.total_price = COALESCE(SUM(od.amount * od.price), 0)
        THEN 'PASS'
        ELSE 'FAIL'
    END AS test_result
FROM orders o
LEFT JOIN order_details od
    ON o.order_id = od.order_id
GROUP BY o.order_id, o.total_price
ORDER BY o.order_id;

SELECT
    o.order_id,
    o.order_status
FROM orders o
LEFT JOIN order_details od
    ON o.order_id = od.order_id
WHERE od.order_detail_id IS NULL;
