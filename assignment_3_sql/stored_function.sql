USE jp_food_tour;

-- Viewing data & pinning tables before querying
-- SELECT * 
-- FROM Dish;

-- SELECT * 
-- FROM Restaurants;

-- SELECT *
-- FROM Reviews;

-- SELECT *
-- FROM Users;

-- Creating stored function that measures the cost performance of each restaurant

DELIMITER //

CREATE FUNCTION cost_per(
	Price_Range VARCHAR(5),
    Rating INT)
RETURNS VARCHAR(100)
DETERMINISTIC
BEGIN
	DECLARE Performance VARCHAR(100);
    IF Price_Range = "$" AND Rating >= 4 THEN
		SET Performance = "BARGAIN!";
	ELSEIF Price_Range = "$$" AND Rating = 5 THEN
		SET Performance = "OK";
	ELSEIF Price_Range = "$$$" AND Rating = 5 THEN
		SET Performance = "You get what you pay for";
	ELSEIF Price_Range = "$$$" AND Rating < 5 THEN
		SET Performance = "Proceed with caution";
	ELSE 
		SET Performance = "Hmmm";
	END IF;
    RETURN (performance);
    END //
    
-- Had to drop and rewrite the function several times to get it right!
-- DROP FUNCTION cost_per;

SELECT * FROM Restaurants;
    
SELECT Name, Speciality, cost_per(Price_Range, Rating) AS Cost_Performance
FROM Restaurants
ORDER BY Cost_Performance;
    