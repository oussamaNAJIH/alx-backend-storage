-- stored procedure ComputeAverageScoreForUser that computes and store the average score for a student
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE average DECIMAL(10, 2);
    
    -- Compute average score for the user
    SELECT AVG(score) INTO average
    FROM corrections
    WHERE user_id = user_id;
    
    -- Update average score for the user in the users table
    UPDATE users
    SET average_score = average
    WHERE id = user_id;
END$$
DELIMITER ;
