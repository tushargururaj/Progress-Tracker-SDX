# STUDX PRO 1.0
#### Video Demo: to be updated.
#### Description:
This program is designed to help users manage and track their goals related to chapter completion. It offers a variety of functionalities including setting a goal, tracking progress, adding chapters, deleting completed chapters, resetting goals, clearing records, and exiting the program.

Main Menu
The main menu provides the following options:

Set a Goal: Allows the user to set the maximum number of chapters that can be added.
Progress: Displays the current progress towards the goal, including the number of chapters completed, remaining, and the percentage of progress made.
Add to List: Enables the user to add chapters to the list, provided a goal is set.
Chapter Completion: Allows the user to mark chapters as completed and removes them from the list.
Goal Reset: Resets the current goal.
Clear: Clears both the goal and the chapter list.
Exit: Exits the program.
Detailed Functionality
main()
This function runs an infinite loop that displays the main menu and prompts the user to choose an option. Based on the user's input, it calls the respective function to perform the chosen task. It also handles invalid inputs and prompts the user accordingly.

number_of_lines(file)
This utility function counts and returns the number of lines in a given file.

set_goal()
Prompts the user to set a goal, which is the maximum number of chapters that can be added. The goal is stored in the Goal.txt file.

goal()
Reads and returns the current goal from the Goal.txt file.

add()
Allows the user to add chapters to the Records.csv file. It checks if a goal is set and if the number of chapters added is less than the goal. It prompts the user to input chapter details and stores them in the CSV file.

clear(file)
Clears the contents of the specified file by opening it in write mode and closing it immediately.

delete()
Enables the user to delete a completed chapter from the list. It reads the chapters from the Records.csv file, displays them using the tabulate module, and prompts the user to specify which chapter to remove. It then updates the CSV file accordingly. If all chapters are completed, it also clears the goal.

progress()
Displays the current progress towards the goal by showing the list of chapters, the number of chapters completed, remaining, and the percentage of progress. It also randomly displays a motivational quote from the quotes.txt file.

Summary
This program provides a comprehensive solution for managing and tracking chapter completion goals. By allowing users to set goals, add chapters, mark them as completed, and monitor progress, it ensures that users stay organized and motivated throughout their journey. The use of CSV files for storing chapters and goals ensures that the data is persistent across sessions, while the tabulate module enhances the readability of the displayed information.

