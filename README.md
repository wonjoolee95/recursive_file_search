# recursive_file_search
Searches files and folders recursive to do various actions on them.

Download the ' run_interface.py ' file and run it. This program does some interesting things with files and folders. Given a valid root directory, the program prompts the user the choose a way to choose files (by matching names, particular extension, or miniumun size in KB). The program then prompts the user one more time to choose from some actions to be done on the chosen file(s).

Sample interaction (note the input):


```

This program will do some interesting things,
    primarily searching & modifying files
    and folders of your computer.

Given a root directory, this program finds all files that:
    1. Match the name exactly
    2. End in a particular extension
    3. Exceed the given size in bytes
    

First, you need to provide a correct & valid
    root path to a directory.
    
    In Windows system, such directory will
    look something like: C:\Desktop or C:\Program Files

    In Mac, such directory will
    look something like: /Users/Won_Lee/Desktop

Plese enter your desired working root directory: 

    Path: /Users/Won_Lee/Downloads

Root directory successfully set up!

   Your current root directory: /Users/Won_Lee/Downloads

   How do you like to look for your files?
       1. Matching exact name
         (extension must be included; i.e. practice.txt)
       2. Ending in a particular extension
       3. Exceeding a specific size
       4. QUIT

   Choose and enter 1, 2, 3, or 4: 
   2
   You selected the option to find files that
   end in a particular extension.
     Enter the extension: .zip

   Following files were found:
     /Users/Won_Lee/Downloads/attachments (1).zip
     /Users/Won_Lee/Downloads/attachments (2).zip
     /Users/Won_Lee/Downloads/attachments (3).zip
     /Users/Won_Lee/Downloads/attachments (4).zip
     /Users/Won_Lee/Downloads/attachments.zip
     /Users/Won_Lee/Downloads/Database_Scripts.zip
     /Users/Won_Lee/Downloads/Files 2/pattis_ile1submissions.zip
     /Users/Won_Lee/Downloads/Files 2/pattis_program1solution.zip
     /Users/Won_Lee/Downloads/Files 2/pattis_program2solution.zip
     /Users/Won_Lee/Downloads/Files 2/pattis_program3solution.zip
     /Users/Won_Lee/Downloads/Files 2/pattis_program4solution.zip
     /Users/Won_Lee/Downloads/Files 2/pattis_q1solution.zip
     /Users/Won_Lee/Downloads/Files 2/pattis_q2solution.zip
     /Users/Won_Lee/Downloads/Files 2/pattis_q3solution.zip
     /Users/Won_Lee/Downloads/Files 2/pattis_q4solution.zip
     /Users/Won_Lee/Downloads/Files 2/pattis_q5solution.zip
     /Users/Won_Lee/Downloads/Files 2/pattis_q6solution.zip
     /Users/Won_Lee/Downloads/ics33win16grades (1).zip
     /Users/Won_Lee/Downloads/ics33win16grades (2).zip
     /Users/Won_Lee/Downloads/ics33win16grades (3).zip
     /Users/Won_Lee/Downloads/ics33win16grades (4).zip
     /Users/Won_Lee/Downloads/ics33win16grades (5).zip
     /Users/Won_Lee/Downloads/ics33win16grades (6).zip
     /Users/Won_Lee/Downloads/ics33win16grades (7).zip
     /Users/Won_Lee/Downloads/ics33win16grades (8).zip
     /Users/Won_Lee/Downloads/ics33win16grades.zip
     /Users/Won_Lee/Downloads/ile1gradesstudents.zip
     /Users/Won_Lee/Downloads/ile2gradesstudents.zip
     /Users/Won_Lee/Downloads/linkedlist.zip
     /Users/Won_Lee/Downloads/Music/[HULKPOP.COM][Album] Roy Kim - Vol.2 HOME/[HULKPOP.COM][Album] Roy Kim - Vol.2 HOME.zip
     /Users/Won_Lee/Downloads/pattis_q1solution.zip
     /Users/Won_Lee/Downloads/piltest.zip
     /Users/Won_Lee/Downloads/program1.zip
     /Users/Won_Lee/Downloads/program2.zip
     /Users/Won_Lee/Downloads/program3 (1).zip
     /Users/Won_Lee/Downloads/program3.zip
     /Users/Won_Lee/Downloads/program4.zip
     /Users/Won_Lee/Downloads/program5 (1).zip
     /Users/Won_Lee/Downloads/program5 (2).zip
     /Users/Won_Lee/Downloads/program5.zip
     /Users/Won_Lee/Downloads/program5helper.zip
     /Users/Won_Lee/Downloads/project0d.zip
     /Users/Won_Lee/Downloads/q4helper.zip
     /Users/Won_Lee/Downloads/q5helper.zip
     /Users/Won_Lee/Downloads/q6helper.zip
     /Users/Won_Lee/Downloads/q8helper.zip
     /Users/Won_Lee/Downloads/quiz8gradesstudents.zip
     /Users/Won_Lee/Downloads/SMORS.zip
     /Users/Won_Lee/Downloads/Solutions (1).zip
     /Users/Won_Lee/Downloads/Solutions (2).zip
     /Users/Won_Lee/Downloads/Solutions.zip
     /Users/Won_Lee/Downloads/tree.zip
     /Users/Won_Lee/Downloads/unittests.zip


   What do you want to do with these files?
       1. Read the file (only for .txt files)
       2. Create a duplicate
       3. Touch the file
         (update the last modified timestamp)

   Choose and enter 1, 2, or 3: 3
   File(s) successfully touched!

   Your current root directory: /Users/Won_Lee/Downloads

   How do you like to look for your files?
       1. Matching exact name
         (extension must be included; i.e. practice.txt)
       2. Ending in a particular extension
       3. Exceeding a specific size
       4. QUIT

   Choose and enter 1, 2, 3, or 4: 
   4
   You are about the quit the program.
   Are you sure? (yes/no): yes

```
