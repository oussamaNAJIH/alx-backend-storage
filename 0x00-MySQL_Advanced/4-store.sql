-- trigger that decreases the quantity of an item after adding a new order
DELIMITER $$
CREATE TRIGGER after_new_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET NEW.quantity = OLD.quantity - NEW.number
    WHERE items.name = orders.item_name
END$$
DELIMITER ;