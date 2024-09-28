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

-- 1. Return all the restaurants with a $ price range in Tokyo

SELECT Name, City, Price_Range
FROM Restaurants
WHERE Price_Range = "$" AND
	City = "Tokyo";
    
-- 2. Retrieve all the restaurants that were reviewed in 2023 and their review date

SELECT r.Name, rv.Review_Date
FROM Restaurants r
JOIN Dish d
ON r.Restaurant_ID = d.Restaurant_ID
JOIN Reviews rv
ON d.Dish_ID = rv.Dish_ID
WHERE YEAR(rv.Review_Date) = 2023
ORDER BY rv.Review_Date ASC;

-- 3. What are the main ingredients from the dishes at Ninoni?

SELECT r.Name, d.Dish_Name, d.Main_Ingredient
FROM Restaurants r
JOIN Dish d
ON r.Restaurant_ID = d.Restaurant_ID
WHERE r.Name = "Ninoni";

-- 4. Total amount spend on reviews by each user

SELECT CONCAT(u.First_Name, " ", u.Last_Name) AS full_name, SUM(d.price) AS total_spent
FROM Dish d
JOIN Reviews rv
ON d.Dish_ID = rv.Dish_ID
JOIN Users u 
ON rv.User_ID = u.User_ID
GROUP BY full_name
ORDER BY total_spent DESC;

-- 5. Find the number of days since Gyoza have been reviewed

SELECT r.Name, DATEDIFF(CURDATE(),(
	SELECT MAX(rv.Review_Date)
    FROM Reviews rv
    WHERE rv.Dish_ID = d.Dish_ID
    )) AS days_since_gyoza_reviewed
FROM Dish d
JOIN Restaurants r
ON d.Restaurant_ID = r.Restaurant_ID
WHERE Dish_name = "Gyoza"
ORDER BY days_since_gyoza_reviewed DESC;

-- 6. Find the total number of reviews and money spent in 2024
SELECT CONCAT(u.First_Name, " ", u.Last_Name) AS full_name, COUNT(rv.Review_ID) AS total_reviews, SUM(d.price) as total_spent_JPY
FROM Users u
JOIN Reviews rv
ON u.User_ID = rv.User_ID
JOIN Dish d
ON rv.Dish_ID = d.Dish_ID
WHERE YEAR(rv.Review_Date) = 2024
GROUP BY u.User_ID
ORDER BY total_reviews DESC;

-- 7. Showing how to insert and delete a row after a table has been created.
INSERT INTO Restaurants (Restaurant_ID, Name, City, Speciality, Price_Range, Rating)
VALUES
(11, "Yakuniku Like", "Chiba", "Yakiniku", "$", 4);

SELECT * 
FROM Restaurants;

DELETE FROM Restaurants r
WHERE r.Restaurant_ID = 11;
