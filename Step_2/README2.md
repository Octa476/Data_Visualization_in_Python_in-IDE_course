# Eliminate the unnecessary rows from the data.

In this step you will learn you to delete all the rows from your data that are redundant for your analysis.
You will use pandas for this job.

## Useful commands
- every DataFrame object created has an atribute index(e.g df has df.index) that is a special kind of list 
which contains all the indexes of every row
- df.loc[row_index, field] is a method that returns the information stored at the row_index-th cell of the "field" column
- df.drop(row_index, inplace = True) method deletes the row_index-th row from the dataframe df

Task:
- you need to delete some rows from the given .csv file and print the cleaned DataFrame to stdout
- more details will be provided in the task2.py file

Checker:
- in order to check your code run the checker2.py script