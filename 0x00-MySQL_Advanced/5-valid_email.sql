-- creates a trigger that resets the attribute valid_email only when the email has been changed
DELIMITER $$
CREATE TRIGGER after_email_update
AFTER UPDATE ON users.email
FOR EACH ROW
BEGIN
    UPDATE users
    SET NEW.valid_email = 0
END$$
DELIMITER ;
