CREATE DATABASE local_dish;

USE local_dish;

CREATE TABLE food
(food_id INT NOT NULL PRIMARY KEY ,
food_name VARCHAR(30),
region_id INT,
main_ingredient VARCHAR(30),
cooking_method VARCHAR(30),
description VARCHAR(255)
);

ALTER TABLE food
ADD FOREIGN KEY (region_id) REFERENCES region(region_id);

INSERT INTO food (food_id, food_name, region_id, main_ingredient, cooking_method, description)
VALUES
(1, 'Jingisukan', 1, 'Lamb', 'Grilled', 'Grilled lamb with vegetables on a dome-shaped grill.'),
(2, 'Towada Bara Yaki', 2, 'Beef', 'Grilled', 'Beef rib and onions grilled with soy sauce.'),
(3, 'Morioka Reimen', 3, 'Noodles', 'Simmered', 'Cold noodles served with spicy kimchi, egg, and fruit.'),
(4, 'Gyu Tan Yaki', 4,'Beef Tongue', 'Grilled', 'Grilled beef tongue seasoned with salt or sauce'),
(5, 'Kiritanpo Nabe', 5,'Rice skewers', 'Hotpot', 'Rice mashed and shaped around sticks, grilled, and served with hotpot.'),
(6, 'Imo-ni', 6, 'Taro', 'Hot pot', 'Taro root stew with soy or miso broth.'),
(7, 'Kitakata Ramen', 7, 'Noodles', 'Simmered', 'A hearty noodle dish with simmered broth.'),
(8, 'Mito Natto', 8, 'Soybeans', 'Fermented', 'Fermented soybeans with a sticky texture'),
(9, 'Utsunomiya Gyoza', 9, 'Pork', 'Fried', 'Fried pork dumplings.'),
(10,'Mizusawa Udon', 10, 'Noodles', 'Boiled', 'Thick, boiled udon noodles served simply with a dipping sauce.'),
(11, 'Hiyajiru Udon', 11, 'Noodles', 'Soup', 'Chilled udon noodles served in a cold soup, perfect for summer.'),
(12, 'Namero', 12, 'Fish', 'Raw', 'A dish of raw, minced fish seasoned with miso and herbs.'),
(13, 'Monjayaki', 13, 'Various', 'Hot plate', 'A savory pancake cooked on a hot plate'),
(14, 'Shirasu-don', 14, 'Whitebait', 'Raw', 'A rice bowl topped with raw whitebait fish.'),
(15, 'Hegi soba', 15, 'Buckwheat Noodles', 'Chilled', 'Chilled buckwheat noodles, traditionally served on a wooden tray.'),
(16, 'Toyama black ramen', 16, 'Noodles', 'Simmered', 'A distinctive noodle soup with a deep, simmered black soy sauce broth.'),
(17, 'Nodoguro', 17, 'Rockfish', 'Raw', 'Raw slices of rich and fatty rockfish, often served as sashimi.'),
(18, 'Saba sushi', 18, 'Mackerel','Sushi', 'Vinegared rice topped with slices of marinated mackerel.'),
(19, 'Hoto', 19, 'Noodles', 'Hotpot', 'Thick noodles in a miso-based broth.'),
(20, 'Shinshu soba', 20,  'Buckwheat Noodles', 'Simmered', 'Simmered buckwheat noodles from the Shinshu region.'),
(21, 'Hida Beef Steak', 21, 'Beef', 'Grilled', 'Grilled Hida beef, known for its rich marbling and flavor.'),
(22, 'Sakura Shrimp Kakiage', 22, 'Sakura Shrimp', 'Deep-fried', 'Deep-fried fritters made from sakura shrimp.'),
(23, 'Hitsumabushi', 23, 'Eel', 'Grilled', 'Grilled eel served over rice, often enjoyed with broth poured over.'),
(24, 'Matsuzaka Beef Sukiyaki', 24, 'Beef', 'Hotpot', 'A luxurious hotpot featuring thin slices of Matsuzaka beef.'),
(25, 'Omi beef', 25, 'Beef', 'Grilled', 'Grilled Omi beef, famous for its tenderness and flavor.'),
(26, 'Yu-dofu', 26, 'Tofu', 'Simmered', 'Silken tofu gently cooked in a light broth, often enjoyed with dipping sauces.'),
(27, 'Takoyaki', 27, 'Octopus', 'Fried', 'Round balls of batter filled with pieces of octopus, crispy on the outside and soft on the inside.'),
(28, 'Kobe beef steak', 28, 'Beef', 'Grilled', 'This grilled beef melts in the mouth with rich flavor.'),
(29, 'Kaki no ha sushi', 29, 'Fish', 'Sushi', 'A unique style of sushi wrapped in persimmon leaves, typically featuring seasonal fish.'),
(30, 'Wakayama Ramen', 30, 'Noodles', 'Simmered', 'A comforting noodle soup with a deep, savory broth, often featuring regional toppings.'),
(31, 'Matsuba Crab', 31, 'Crab', 'Boiled', 'Delicate crab meat boiled to retain its sweetness.'),
(32, 'Izumo Soba', 32, 'Buckwheat Noodles', 'Simmered', 'Buckwheat noodles served warm, cherished for their wholesome and hearty texture.'),
(33, 'Tsuyama Horumon Udon', 33, 'Noodles', 'Grilled', 'Noodles combined with grilled offal.'),
(34, 'Kaki', 34, 'Oysters', 'Raw', 'Freshly shucked oysters, enjoyed raw for their briny and creamy taste.'),
(35, 'Fugu', 35, 'Pufferfish', 'Raw', 'A delicacy featuring thinly sliced pufferfish, known for its unique flavor and culinary risk.'),
(36, 'Tokushina Ramen', 36, 'Noodles', 'Simmered', 'A savory noodle dish with a flavorful broth.'),
(37, 'Sanuki Udon', 37, 'Udon Noodles', 'Simmered', 'Thick, chewy noodles that are warm and comforting.'),
(38, 'Tai Meshi', 38, 'Red Sea Bream', 'Raw', 'A rice dish adorned with fresh slices of sea bream.'),
(39, 'Katsuo no Tataki', 39, 'Bonito', 'Seared', 'Seared bonito fish served with citrus and herbs'),
(40, 'Motsunabe', 40, 'Pork offal', 'Hot pot', 'A hearty hotpot featuring offal and vegetables simmered in a savory broth.'),
(41, 'Yobuko no Ika', 41, 'Squid', 'Raw', 'Fresh squid served raw.'),
(42, 'Nagasaki Champon', 42, 'Seafood', 'Simmered', 'A hearty noodle dish filled with various seafood and vegetables.'),
(43, 'Basashi', 43, 'Horsemeat', 'Raw', 'Raw horsemeat delicately sliced, often served as sashimi with dipping sauces.'),
(44, 'Toriten', 44, 'Chicken', 'Tempura', 'Crispy, fried chicken coated in a light batter.'),
(45, 'Miyazaki Jittoko', 45, 'Chicken', 'Charcoal grilled', 'Chicken grilled over charcoal, celebrated for its juicy flavor and smoky aroma.'),
(46, 'Kurobuta', 46, 'Pork', 'Hotpot', 'A pork hotpot featuring succulent cuts.'),
(47, 'Sokisoba', 47, 'Noodles', 'Simmered', 'Noodles served in a savory broth, often garnished with tender pork pieces.')
;

SELECT * FROM food;

CREATE TABLE reviews (
user_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
food_id INT, 
review_date DATE,
review VARCHAR(255),
FOREIGN KEY (food_id) REFERENCES food(food_id)
);

INSERT INTO reviews (food_id, review_date, review)
VALUES
(1, "2023-10-04", "VERY yummy!");

SELECT * FROM reviews;