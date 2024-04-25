-- trigger that decreases the quantity of an item after adding a new order
DELIMITER $$
CREATE TRIGGER after_new_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    IF OLD.email != NEW.email THEN
        SET NEW.valid_email = 0;
    END IF;
END$$
DELIMITER ;