CREATE DATABASE jp_food_tour;

USE jp_food_tour;

CREATE TABLE Restaurants 
(Restaurant_ID INT NOT NULL PRIMARY KEY, 
Name VARCHAR(40), 
City VARCHAR(40), 
Speciality VARCHAR(40), 
Price_Range VARCHAR(5), 
Rating INT NOT NULL
);

INSERT INTO Restaurants (Restaurant_ID, Name, City, Speciality, Price_Range, Rating)
VALUES
(1, "Sushiro", "Tokyo", "Sushi", "$", 3),
(2, "Yonyonkazoku", "Kumamoto", "Samgyeopsal","$", 5),
(3, "Ninoni", "Fukuoka", "Gyoza", "$", 3),
(4, "Mizuno", "Osaka", "Okonomiyaki", "$$", 4),
(5, "Takamaru Denki", "Tokyo", "Gyoza", "$$$", 5),
(6, "Yamunashi", "Tokyo", "Tamagoyaki", "$$$", 5),
(7, "Pizza Slice", "Sapporo", "Pizza", "$", 3),
(8, "Tata", "Osaka", "Pasta", "$$", 2),
(9, "Haidilao", "Tokyo", "Hotpot", "$$", 5),
(10, "Fuuki Noodle", "Kumamoto", "Ramen", "$$$", 4);

CREATE TABLE Speciality_Dish
(Dish_ID INT NOT NULL PRIMARY KEY,
Restaurant_ID INT NOT NULL,
Dish_Name VARCHAR(40),
Main_Ingredient VARCHAR(30),
Price DECIMAL,
Spice_Level INT,
FOREIGN KEY(Restaurant_ID) REFERENCES Restaurants(Restaurant_ID)
);

-- Modifying the datatype as JPY doesn't use decimals -- 
ALTER TABLE Speciality_Dish
MODIFY COLUMN Price INT;

INSERT INTO Speciality_Dish (Dish_ID, Restaurant_ID, Dish_Name, Main_Ingredient, Price, Spice_Level)
VALUES
(1, 1, "Seafood Salad Gunkan", "Seafood", "100", 0),
(2, 1, "Tuna Nigiri", "Tuna", "150", 0),
(3, 1, "Shrimp Avocado Nigiri", "Shrimp", "200", 0),
(4, 2, "Samgyeopsal", "Pork", "1700", 3),
(5, 2, "Bibimbap", "Rice", "800", 3),
(6, 2, "Kimchijeon", "Kimchi", "900", 4),
(7, 3, "Gyoza", "Pork", "750", 1),
(8, 3, "Century Egg", "Egg", 1000, 0),
(9, 3, "Fried Rice", "Rice", 500, 2),
(10, 4, "Okonomiyaki", "Batter", 2000, 1),
(11, 5, "Gyoza", "Pork", 1500, 1),
(12, 5, "Yakisoba", "Noodles", 1000, 2),
(13, 5, "Tamagoyaki", "Egg", 900, 1),
(14, 6, "Tamagoyaki", "Egg", 1000, 1),
(15, 6, "Oden", "Radish", 700, 1),
(16, 6, "Gyukatsu", "Beef", 2000, 1),
(17, 7, "Cheese Pizza", "Cheese", 750, 1),
(18, 7, "Mushroom Pizza", "Mushroom", 800, 1),
(19, 8, "Carbonara", "Pasta", 1500, 1),
(20, 9, "Hotpot", "Meats", 3000, 5),
(21, 10, "Ramen", "Noodles", 2000, 1),
(22, 10, "Soba", "Noodles", 2500, 3);

-- Changing table name as it's too long and misleading
ALTER TABLE Speciality_Dish
RENAME TO Dish;

-- Adding a UNIQUE constraint so that the same dish name cannot be added for the same restaurant
ALTER TABLE Dish
ADD CONSTRAINT Unique_Dish UNIQUE(Restaurant_ID, Dish_ID);

CREATE TABLE Reviews 
(Review_ID INT NOT NULL PRIMARY KEY,
User_ID INT,
Dish_ID INT,
Review_Date DATE,
Star_Rating INT,
FOREIGN KEY(Dish_ID) REFERENCES Dish(Dish_ID));

INSERT INTO Reviews (Review_ID, Dish_ID, User_ID, Review_Date, Star_Rating)
VALUES
(1, 1, 1, "2020-10-13", 4),
(2, 2, 2, "2023-11-14", 3),
(3, 3, 1, "2020-10-13", 5),
(4, 4, 1, "2022-01-01", 5),
(5, 5, 3, "2024-05-08", 5),
(6, 5, 2, "2023-11-14", 5),
(7, 7, 1, "2024-03-24", 4),
(8, 8, 1, "2024-03-24", 1),
(9, 9, 3, "2023-07-12", 3),
(10, 10, 2, "2021-04-23", 4),
(11, 11, 3, "2024-09-23", 5),
(12, 12, 1, "2023-11-12", 2),
(13, 12, 1, "2024-02-14", 4),
(14, 12, 2, "2023-05-09", 3),
(15, 13, 3, "2022-04-04", 5),
(16, 14, 2, "2023-11-20", 0),
(17, 15, 1, "2024-04-05", 1),
(18, 16, 2, "2024-01-27", 5),
(19, 17, 3, "2022-12-09", 4),
(20, 18, 2, "2024-07-08", 5),
(21, 19, 1, "2023-09-21", 3),
(22, 20, 2, "2024-06-20", 1),
(23, 21, 1, "2023-10-14", 2),
(24, 22, 2, "2022-10-02", 4),
(25, 17, 3, "2023-10-04", 5),
(26, 19, 1, "2022-11-14", 3),
(27, 3, 3, "2023-01-24", 5),
(28, 11, 2, "2023-05-14", 1),
(29, 22, 1, "2022-10-27", 5),
(30, 22, 2, "2023-11-14", 4);


CREATE TABLE Users 
(User_ID INT NOT NULL PRIMARY KEY,
First_Name VARCHAR(25),
Last_Name VARCHAR(40),
Age INT,
Country VARCHAR(30));

INSERT INTO Users (User_ID, First_Name, Last_Name, Age, Country)
VALUES 
(1, "Sally", "Dee", 28, "UK"),
(2, "Suzuka", "Murasato", 45, "Japan"),
(3, "Melissa", "Jay", 22, "Canada");

