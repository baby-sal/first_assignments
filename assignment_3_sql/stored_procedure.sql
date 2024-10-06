-- Creating stored procedure to call all restaurants in Tokyo

SELECT *
FROM Restaurants;

// DELIMITER 

CREATE PROCEDURE tokyo_rest ()
BEGIN
	SELECT Restaurant_ID, Name, City, Speciality, Price_Range, Rating
    FROM Restaurants
    WHERE City = "Tokyo";
END //

DELIMITER ;

CALL tokyo_rest();