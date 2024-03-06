[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/3ygqAX-S)
## Table of Contents

1. [Linux](#linux)
2. [Github](#github)
3. [Python](#python)

## Linux

1. Navigate to the "Documents" directory and create a new file named "notes.txt." and write “important” in it.
2. List all files in the "Downloads" directory that have a ".pdf" extension.
3. Create a new directory called "backup" inside the "Documents" directory.
4. Copy the file "notes.txt" from the "Documents" to the "backup" directory.
5. Change the permissions of the file "notes.txt" to allow read and write for the owner.
6. Search for all files in the home directory that contain the word "important" in their content.
7. Remove the directory "backup" and its contents from the Documents.
8. Display a list of running processes on your system using the ps command.
9. Rename the file "notes.txt" to "new_notes.txt" in the Documents.

## Github

1. Go to github.com
2. Create a new repo called <your-github-id>.github.io. Review https://docs.github.com/en/pages/quickstart for additional help and instructions.
3. Clone the repo on your local machine
4. Add _config.yml and update it per https://docs.github.com/en/pages/quickstart#changing-the-title-and-description. 
    - The title should be "<first_name> <last_name> | 1E9 Advisors"
    - The description can be whatever you want. It has to be work appropriate.
5. Add a file called README.md
6. Create a directory called journal
7. Add one file for each day of training. Call the file day_n.md. n must be a 0 padded 3 digit string. 
    - Day 1 will become day_001.md. 
    - Day 2 will become day_002.md. 
    - Day 34 will become day_034.md.
    - etc.
8. Write 5 things you learned on each day in the appropriate file. The 5 things each day must be unique, and cannot be a repetition of any of the days prior to it.
9. Commit the README.md file and journal directory with all the day_00n.md files in it.

## Python

### Functions

Define functions in utils.py to do the following things
1. evenify(input_numbers): return a sorted list of even numbers in input_numbers.
2. foo_max(items): find and return the maximum element in the list (items); you may not use the built-in max() function.
3. sautee(sentence): take a sentence and return the sentence with the words in reverse order.
4. flambe(sentence): returns a new list with the words sorted by their length.
5. poach(dt: datetime.datetime): return True if datetime is in a leap year and False if not
6. heron(a, b, c): return the area of a triangle given the lengths of its three sides (Heron's formula).

  ```
  s = (a + b + c) / 2
  area = √(s * (s - a) * (s - b) * (s - c))
  ```

### Multiplication Tables
7. Define a function in tables.py that takes n and prints the multiplication table for up to 20 x n.
  - The formatting of the print must be perfect. All columns must be correctly aligned.
    
    ```
    [1]: mtables(5)
    Out: Multiplication Table for 5
    
    5 x  1 =   5
    5 x  2 =  10
    5 x  3 =  15
    5 x  4 =  20
    5 x  5 =  25
    ...
    5 x 20 = 100
    ```

### File IO and formats

8. JSON to CSV
  - Define a function in utils.py that takes the path to a json file
  - Read the json file
  - Write to a csv file that has the same name as the json file but has a new extension of csv instead
  - Do not clobber an existing file with the same name
  - Return the name of the csv file

```
[2]: json_to_csv("abcd.json")
Out: abcd.csv
```

9. CSV to JSON
  - Define a function in utils.py that takes the path to a csv file
  - Read the csv file
  - Write to a json file that has the same name as the json file but has a new extension of json instead
  - Do not clobber an existing file with the same name

```
[3]: csv_to_json("abcd.csv")
Out: abcd.json
```
