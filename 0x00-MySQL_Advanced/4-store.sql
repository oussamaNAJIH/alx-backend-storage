-- trigger that decreases the quantity of an item after adding a new order
DELIMITER $$
CREATE TRIGGER after_new_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    IF name = item_name THEN
        SET NEW.quantity = OLD.quantity - number;
    END IF;
END$$
DELIMITER ;