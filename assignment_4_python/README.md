## Japanese Regional Delicacy Search

This is a application that allows users to view the different delicacies of each region and read any reviews about those delicacies. The user can also delete reviews.

### How to use:
1. Import all necessary modules from the requirements.txt file
2. In the config.py file, add the details for your own host, username, password. The database should remain the same. It is important that you don't share this config file to others, so gitignore it, or remove details before pushing. 
3. Run app.py file first to establish connection to the server.
4. Run main.py and respond to the input question.
5. If deleting a review, check the database on MySQL to ensure that the value has been deleted.

##### Areas to develop further:
- Using more complex queries to get more readable results returned from the input (currently a long list of lists).
- Implementing a PUT endpoint so that reviews can also be added.
- Ability to go back to the start without rerunning the whole of main, if the end-user wanted to do more than one thing.
- Design the database better (or use a join?) so that the food name is shown when reviews are requested.


#### Assignment Checklist:
+ Implement 2 API endpoints with appropriate functionality 
  + ##### (See app.py)
+ Implement one additional endpoint of your choice (can be POST or GET but with a
different implementation) 
  + ##### (See app.py)
+ Implement client-side for each of the 3 API endpoints you have created. 
  + ##### (See main.py)
+ Create a MySQL database with at least 1 table 
  + ##### (See local_dish_db_sql)
+ Have a config file (do not leave your private information here) 
  + ##### (See config.py)
+ Have db_utils file and use exception handling 
  + ##### (See db_utils.py)
+ Use appropriate SQL queries to interact with the database in your Flask application, and
demonstrate at least two different queries. 
  + ##### (See db_utils.py)
+ In main.py have a run() function/call the functions to simulate the planned interaction
with the API, this could include welcome statements, displaying etc., 
  + ##### (See main.py)
+ Have correct but minimal imports per file (do not import things you do not use in the
file) 
  + ##### (See requirements.txt)
+ Document how to run your API in a markdown file including editing the config file, any
installation requirements up until how to run the code and what is supposed to happen. 
  + ##### (See above and requirements.txt)