USE jp_food_tour;

-- Viewing data & pinning tables before querying
SELECT * 
FROM Dish;

SELECT * 
FROM Restaurants;

SELECT *
FROM Reviews;

SELECT *
FROM Users;

-- Querying

-- Return all the restaurants with a $ price range in Tokyo

SELECT Name, City, Price_Range
FROM Restaurants
WHERE Price_Range = "$" AND
	City = "Tokyo";
    
-- Retrieve all the restaurants that were reviewed in 2023 and their review date

SELECT r.Name, rv.Review_Date
FROM Restaurants r
JOIN Dish d
ON r.Restaurant_ID = d.Restaurant_ID
JOIN Reviews rv
ON d.Dish_ID = rv.Dish_ID
WHERE YEAR(rv.Review_Date) = 2023
ORDER BY rv.Review_Date ASC;

-- What are the main ingredients from the dishes at Ninoni?

SELECT r.Name, d.Dish_Name, d.Main_Ingredient
FROM Restaurants r
JOIN Dish d
ON r.Restaurant_ID = d.Restaurant_ID
WHERE r.Name = "Ninoni";

-- How much money did each user spend on reviewing food in 2024?