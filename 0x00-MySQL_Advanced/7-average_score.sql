-- stored procedure ComputeAverageScoreForUser that computes and store the average score for a student

DELIMITER $$
CREATE PROCEDURE omputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE average DECIMAL(10, 2);
    SELECT AVG(score) INTO average
    FROM corrections
    WHERE user_id = user_id;
    UPDATE users
    SET average_score = average
    WHERE id = user_id;
END$
DELIMITER ;