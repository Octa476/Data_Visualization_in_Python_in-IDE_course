# Sort data after a field.

This step will teach you how to sort your data after one or many categories.

You will use some pandas methods and classes to achive the desired order of your data.

## Pandas know how:
- you can extract a list of unique items from a field using the `.unique()` method(e.g `df["field"].unique()` return a list of unique items from **"field"**)
- `Categorical` is a class of the pandas module used to categorize fields of a dataset after a rule which is given(e.g if you have a ordered list named **"order_field"** which contains all the unique items from a field you can categorize the field by using this class)
- this category attribute of the field will be useful when we draw the actual bar plot and will be further explained in the next step

## Task:
- apply the category attribute to the given dataset fields

## Checker:
- in order to check your code run the checker3.py script

Hint: Search how the Categorical class constructor works and be aware of NaN values.
