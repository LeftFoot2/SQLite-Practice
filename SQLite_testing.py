# Imports SQLite library for use with python.

import sqlite3


# This will allow for a user to choose what they want to do with the data base.
choice = input(f'Type the corresponding letter for what you want to do: insert = "i", update = "u", query = "q", delete = "d", print table = "p" end = "e". ')
# Empty print statements are for looks.
print()

# Used for choices.

insert = 'i'
update = 'u'
query = 'q'
delete = 'd'
print_table = 'p'
end = 'e'


# Connects to data base
con = sqlite3.connect('people.db')

cur = con.cursor()

##############################################################################################################
### If you wish to redo the whole table you can delete the file and just uncomment the line of code below. ###
### Comment it out again after first running of the program.                                               ###
##############################################################################################################

#cur.execute('''CREATE TABLE people (ID real, name text, birthday text, age real, hair_color text, eye_color text, fav_food text)''')


# While loop allows for the changing of the database without having to rerun the program.

while choice != end:

   # Insert allows for the user to input a new person into the database.

   if choice == insert:

      ID = input('ID: ')
      name = input('Name: ')
      birthday = input('Birthdate: ')
      age = input('Age: ')
      hair_color = input('Hair Color: ')
      eye_color = input('Eye Color: ')
      fav_food = input('Favorite Food: ')

      # Each of the user inputs are put into the list so that it can be put into a row of the database.

      people_list = [(ID), (name), (birthday), (age), (hair_color), (eye_color), (fav_food)]

      # This actually does the inputting.

      cur.execute("INSERT INTO people VALUES (?,?,?,?,?,?,?)", people_list)

      con.commit()


   # This allows for the user to update each part of the table except for the ID.

   elif choice == update:

      update_choice = input('What do you want to change: name = "n", birthday = "b", age = "a", hair color = "h", eye color = "e", favorite food = "f" ')
      print()

      # Change name.

      if update_choice == 'n':
         ID = input('Which row do you wish to change: ')
         name = input('What is the new name: ')

         update_list = [(name), (ID)]

         cur.execute('''UPDATE people SET name = ? WHERE ID = ?''', update_list)

         con.commit()    

      # Change birthday.     

      elif update_choice == 'b':
         ID = input('Which row do you wish to change: ')
         birthday = input('What is the new birthday: ')

         update_list = [(birthday), (ID)]

         cur.execute('''UPDATE people SET birthday = ? WHERE ID = ?''', update_list)

         con.commit()  

      # Change age.

      elif update_choice == 'a':
         ID = input('Which row do you wish to change: ')
         age = input('What is the new age: ')

         update_list = [(age), (ID)]

         cur.execute('''UPDATE people SET age = ? WHERE ID = ?''', update_list)

         con.commit()  

      # Change hair color.

      elif update_choice == 'h':
         ID = input('Which row do you wish to change: ')
         hair_color = input('What is the new hair color: ')

         update_list = [(hair_color), (ID)]

         cur.execute('''UPDATE people SET hair_color = ? WHERE ID = ?''', update_list) 
         
         con.commit()

      # Change eye color.

      elif update_choice == 'e':
         ID = input('Which row do you wish to change: ')
         eye_color = input('What is the new eye color: ')

         update_list = [(eye_color), (ID)]

         cur.execute('''UPDATE people SET eye_color = ? WHERE ID = ?''', update_list)

         con.commit()

      # Change favorite food.

      elif update_choice == 'f':
         ID = input('Which row do you wish to change: ')
         fav_food = input('What is the new favorite food: ')

         update_list = [(fav_food), (ID)]

         cur.execute('''UPDATE people SET fav_food = ? WHERE ID = ?''', update_list)  

         con.commit()
         
   # Lets you look at rows based on the ID of the row.
   
   elif choice == query:

      choose_row = input('Which row do you want to see (use ID as chosen row): ')

      for row in cur.execute('SELECT * FROM people WHERE ID == ?', choose_row):
         print(row)


   # Deletes rows on based on the ID of the row.

   elif choice == delete:

      choose_row = input('Which row do you want to delete (use ID as chosen row): ')

      for row in cur.execute('DELETE FROM people WHERE ID == ?', choose_row):
         print(row)

   # This will simply print out the whole table that the user has created.
   
   elif choice == print_table:
      for row in cur.execute('SELECT * FROM people ORDER BY ID'):
         print(row)

   print()
   choice = input(f'Type the corresponding letter for what you want to do: insert = "i", update = "u", query = "q", delete = "d", print table = "p" end = "e". ')
   print()

# Commits changes to database and then closes the connection to the database.

con.commit()

con.close()
