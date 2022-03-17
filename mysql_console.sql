USE eshop;

SELECT * FROM products;
SELECT * FROM customers;
SELECT * FROM orders;
SELECT * FROM order_status;
SELECT * FROM order_lines;

INSERT INTO order_status(status)
VALUES
('Pending Approval'),
('Approved'),
('Processing'),
('Sent'),
('Delivered');


INSERT INTO customers(customer_first_name, customer_last_name, customer_email, customer_mobile_phone)
VALUES
('Anna', 'Andersson', 'anna@email.com', '123456789'),
('Bosse', 'Bengtsson', 'bosse@email.com', '987654321');

INSERT INTO orders (order_date, order_status_id, customer_id)
VALUES
('2022-01-14', 2, 1),
('2022-02-23', 4, 2);

INSERT INTO order_lines(product_id, order_id, amount_ordered)
VALUES
(1, 1, 10),
(2, 1, 1),
(3, 2, 5);
