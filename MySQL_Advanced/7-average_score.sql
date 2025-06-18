-- Write a SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student. Note: An average score can be a decimal
DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(IN p_user_id INT)
BEGIN
    DECLARE average_score FLOAT;

    SELECT AVG(score) INTO average_score FROM corrections
    WHERE user_id = p_user_id;

    UPDATE users
    SET average_score = IFNULL(average_score, 0)
    WHERE id = p_user_id;
END$$

DELIMITER ;