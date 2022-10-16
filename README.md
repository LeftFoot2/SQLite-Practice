# Overview

This a python program written so that the user can create a database and populate it will data. The data that it is made for is people; with several different attributes you would find
for a person, age, eye color, etc. There will be an empty database by default, but you can delete that file and recreate it by uncommenting the "create table" line of code. There is a big
comment that will show you where that is in the code. You will be given options to insert, update, query, delete, or print the table. Each insert will do one person. You can update each persons
record in ever category but their ID. You can print out specific rows of the database by using the ID of that row. You can also delete rows based on ID. You can end your interaction
with the data base by pressing 'e'.

This program was written to give me some experience in working with SQL databases.

[SQLite in Python](https://youtu.be/FaoDXlP0O-8)

# Relational Database

I used SQLite.

The table is made of row of an ID, name, birthday, age, hair color, eye color, favorite food.

# Development Environment

I used VScode and wrote in python. The sqlite3 library to write this software.

# Useful Websites

* [Data to Fish](https://datatofish.com/update-records-sql-server/)
* [Python](https://docs.python.org/3.8/library/sqlite3.html)

# Future Work

* I would like to make it so that if a row is deleted then all the ID's would change to keep sequential ID's in the table.
* I would like to make the table printing out look more professional.
* I would like to add an ability to query specific columns.