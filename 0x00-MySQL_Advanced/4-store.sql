-- trigger that decreases the quantity of an item after adding a new order
DELIMITER $$
CREATE TRIGGER after_new_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = item_name
END$$
DELIMITER ;